# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2024 Magnopy Team
#
# e-mail: anry@uv.es, web: magnopy.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize, shgo
from wulfric import TORADIANS, absolute_to_relative

from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.units.inside import ENERGY
from magnopy.units.si import BOHR_MAGNETON

__all__ = ["Energy"]

# Convert to the internal units of energy
BOHR_MAGNETON /= ENERGY


def update_spin_directions(spin_directions, search_direction, step=1):
    spin_directions = spin_directions.copy()
    a12 = search_direction[::3] * step
    a13 = search_direction[1::3] * step
    a23 = search_direction[2::3] * step

    thetas = np.sqrt(a12**2 + a13**2 + a23**2)

    r = []
    for i in range(len(thetas)):
        theta = thetas[i]

        if theta < np.finfo(float).eps:
            continue

        r = (np.array([-a23[i], a13[i], -a12[i]])) / theta

        spin_directions[i] = (
            np.cos(theta) * spin_directions[i]
            + np.sin(theta) * np.cross(r, spin_directions[i])
            + (1 - np.cos(theta)) * r * (r @ spin_directions[i])
        )

    return spin_directions


class Energy:
    def __init__(self, spinham: SpinHamiltonian):
        self.g_factors = [atom.g_factor for atom in spinham.magnetic_atoms]
        self.spins = [atom.spin for atom in spinham.magnetic_atoms]
        self.factor = spinham.exchange_factor
        self.atom_indices = dict(
            [(atom, i) for i, atom in enumerate(spinham.magnetic_atoms)]
        )

        # Force double counting notation
        spinham.double_counting = True

        self.bonds = []
        for atom1, atom2, R, J in spinham.exchange_like:
            i = self.atom_indices[atom1]
            j = self.atom_indices[atom2]
            d = spinham.get_distance(atom1, atom2, R)
            self.bonds.append([i, j, d, J])

        self.m = 10

        self.d_vec = np.zeros((self.m, 3 * len(self.spins)), dtype=float)
        self.y_vec = np.zeros((self.m, 3 * len(self.spins)), dtype=float)
        self.rho = np.zeros((self.m), dtype=float)
        self.gamma = np.zeros((self.m), dtype=float)
        self.magnetic_field = None

    def _ferro_grad(self, spin_orientation, gradient_vector=None, torques=None):
        if gradient_vector is None:
            gradient_vector = np.zeros((3 * len(self.spins)), dtype=float)
        if torques is None:
            torques = np.zeros((len(self.spins), 3), dtype=float)

        for i in range(len(spin_orientation)):
            h = 1e-4
            gradient = []
            for j in range(3):
                spin_orientation[i][j] -= h
                f_minus_h = self._ferro_func(spin_orientation)
                spin_orientation[i][j] += 2 * h
                f_plus_h = self._ferro_func(spin_orientation)
                gradient.append((f_plus_h - f_minus_h) / 2 / h)
                spin_orientation[i][j] -= h

            t = np.cross(spin_orientation[i], gradient)
            for j in range(0, 3):
                torques[i][j] = t[j]
            gradient_vector[3 * i] = t[2]
            gradient_vector[3 * i + 1] = -t[1]
            gradient_vector[3 * i + 2] = t[0]

        return gradient_vector, torques

    def compute_search_direction(
        self,
        k,
        gradient_vector,
        previous_lambda=None,
        previous_gradient_vector=None,
        previous_search_direction=None,
    ):
        if k != 0 and (
            previous_gradient_vector is None
            or previous_search_direction is None
            or previous_lambda is None
        ):
            raise ValueError("need info about previous gradient and search direction")
        n = k % self.m

        if k == 0:
            self.d_vec = np.zeros((self.m, 3 * len(self.spins)), dtype=float)
            self.y_vec = np.zeros((self.m, 3 * len(self.spins)), dtype=float)
            self.rho = np.zeros((self.m), dtype=float)
            self.gamma = np.zeros((self.m), dtype=float)
            search_direction = gradient_vector
        else:
            self.d_vec[n] = previous_lambda * previous_search_direction
            self.y_vec[n] = gradient_vector - previous_gradient_vector
            self.rho[n] = 1 / (self.d_vec[n] @ self.y_vec[n])

            if self.rho[n] < 0:
                return (
                    0,
                    self.compute_search_direction(0, gradient_vector=gradient_vector)[
                        1
                    ],
                )

            q = gradient_vector.copy()

            for l in range(self.m - 1, -1):
                j = (l + n + 1) % self.m
                self.gamma[j] = self.rho[j] * (self.d_vec[j] @ q)
                q = q - self.gamma[j] * self.y_vec[j]
            search_direction = q / self.rho[n] / (np.linalg.norm(self.y_vec[n]))
            for l in range(0, self.m):
                if k < self.m:
                    j = l
                else:
                    j = (l + n + 1) % self.m
                search_direction = search_direction + self.d_vec[j] * (
                    self.gamma[j] - self.rho[j] * (self.y_vec[j] @ search_direction)
                )

        return k, search_direction

    def compute_lambda(self, spin_orientation, search_direction):
        # theta_max = 0.1 / 180 * np.pi

        # a12 = search_direction[::3]
        # a13 = search_direction[1::3]
        # a23 = search_direction[2::3]

        # thetas = np.sqrt(a12**2 + a13**2 + a23**2)

        # theta_rms = np.sqrt(np.sum(thetas**2) / thetas.size)

        # if theta_rms > theta_max:
        #     step = theta_max / theta_rms
        # else:
        #     step = 1
        # print(step)

        # return step

        iter_max = 10000
        a = 1
        c1 = 1e-4
        c2 = 0.9
        fx = self._ferro_func(spin_orientation)
        x_new = update_spin_directions(spin_orientation, search_direction, a)
        nabla_new = self._ferro_grad(x_new)[0]
        nabla = self._ferro_grad(spin_orientation)[0]
        i = 0
        while (
            self._ferro_func(x_new) >= fx + (c1 * a * nabla.T @ search_direction)
            or nabla_new.T @ search_direction <= c2 * nabla.T @ search_direction
        ):
            a *= 0.5
            x_new = update_spin_directions(spin_orientation, search_direction, a)
            nabla_new = self._ferro_grad(x_new)[0]
            if i > iter_max:
                raise ValueError("Wolfe failed")
            i += 1
        return a

    def optimize_ferro(self, initial_guess=None, tol_torque=1e-5, tol_energy=1e-5):
        r"""
        Find minima of the energy assuming generalized ferromagnetic alignment.

        Parameters
        ----------
        initial_guess : (I, 3) |array-like|_, optional
            Initial guess for the orientation of spin vectors.
            If none provided, then random initial guess is chosen.
        """

        if initial_guess is None:
            spin_orientation = np.random.random((len(self.spins), 3))
        else:
            spin_orientation = initial_guess.copy() * 1.0

        for i in range(len(spin_orientation)):
            spin_orientation[i] /= np.linalg.norm(spin_orientation[i])

        tmp_history = [spin_orientation]
        tmp_targets = []

        torque_max = 2 * tol_torque
        energy_diff = 2 * tol_energy
        k = 0
        previous_lambda = None
        previous_gradient_vector = None
        previous_search_direction = None
        torques = np.zeros((len(self.spins), 3), dtype=float)
        gradient_vector = np.zeros((3 * len(self.spins)), dtype=float)
        search_direction = np.zeros((3 * len(self.spins)), dtype=float)
        tmp_stopper = 0
        while torque_max > tol_torque or abs(energy_diff) > tol_energy:
            energy_prev = self._ferro_func(spin_orientation)

            self._ferro_grad(
                spin_orientation=spin_orientation,
                gradient_vector=gradient_vector,
                torques=torques,
            )

            torque_max = np.linalg.norm(torques, axis=1).max()
            if torque_max < tol_torque:
                break

            k, search_direction = self.compute_search_direction(
                k,
                gradient_vector=gradient_vector,
                previous_lambda=previous_lambda,
                previous_gradient_vector=previous_gradient_vector,
                previous_search_direction=previous_search_direction,
            )

            current_lambda = self.compute_lambda(spin_orientation, search_direction)

            spin_orientation = update_spin_directions(
                spin_orientation, search_direction, current_lambda
            )
            energy_current = self._ferro_func(spin_orientation)
            energy_diff = abs(energy_prev - energy_current)
            # print(k, torque_max, tol_torque, energy_diff, tol_energy)
            print(
                f"{energy_diff:.6f}",
                f"{torque_max:.6f}",
                spin_orientation[0],
            )

            tmp_history.append(spin_orientation)
            tmp_stopper += 1
            tmp_targets.append([energy_current, torque_max])

            k += 1
            previous_lambda = current_lambda
            previous_gradient_vector = gradient_vector.copy()
            previous_search_direction = search_direction.copy()

        return spin_orientation, np.array(tmp_history), tmp_targets

    def _ferro_func(self, spin_orientation):
        r"""
        Computes energy of the generalized ferromagnetic state.
        intra-cell rotation matrices are parametrized with the skew-symmetric matrices:

        .. code-block:: text

           0  a b
          -a  0 c
          -b -c 0

        Parameters
        ----------
        spin_orientation : (I, 3) |array-like|_, optional
            Orientation of the spin vectors.
        """

        spin_orientation = np.array(spin_orientation)

        energy = 0

        # Compute exchange and single-ion-like anisotropy energy
        for i, j, d, J in self.bonds:
            if i >= spin_orientation.shape[0] or j >= spin_orientation.shape[0]:
                print(i, j, spin_orientation.shape)
            energy += (
                self.factor
                * self.spins[i]
                * self.spins[j]
                * np.einsum(
                    "i,ij,j", spin_orientation[i], J.matrix, spin_orientation[j]
                )
            )

        # Compute zeeman energy
        if self.magnetic_field is not None:
            for i in range(len(self.spins)):
                energy += (
                    BOHR_MAGNETON
                    * self.g_factors[i]
                    * self.magnetic_field
                    @ spin_orientation[i]
                )

        return energy


if __name__ == "__main__":
    from magnopy.io import load_spinham_txt

    spinham = load_spinham_txt("/Users/rybakov.ad/Codes/magnopy/tmp/easy-along-z.txt")
    # spinham = load_spinham_txt(
    #     "/Users/rybakov.ad/Codes/magnopy/tmp/crsbr-mono-grogu.txt"
    # )
    energy = Energy(spinham)
    # energy.magnetic_field = np.array([1, 0, 15])

    result = energy.optimize_ferro()
    print(result)

    print(result[0])

    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)

    data = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            data[i][j] = energy._ferro_func(
                [
                    [
                        np.cos(phi[j]) * np.sin(theta[i]),
                        np.sin(phi[j]) * np.sin(theta[i]),
                        np.cos(theta[i]),
                    ]
                ]
            )

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # fig, axs = plt.subplots(2, 1)
    # targets = np.array(result[2]).T
    # x = np.linspace(0, len(targets[0]) - 1, len(targets[0]))
    # axs[0].plot(x, targets[0], color="black", lw=2)
    # axs[1].plot(x, targets[1], color="black", lw=2)
    # axs[0].set_xlabel("Iteration step", fontsize=20)
    # axs[0].set_ylabel("Energy", fontsize=20)
    # axs[1].set_xlabel("Iteration step", fontsize=20)
    # axs[1].set_ylabel("Max torque", fontsize=20)
    # plt.savefig("test-targets.png", dpi=300, bbox_inches="tight")
    # plt.close()

    fig, ax = plt.subplots()
    ax.imshow(data, origin="lower", extent=[0, 2 * np.pi, 0, np.pi], cmap="bwr")
    ax.set_xlabel(R"$\phi$", fontsize=20)
    ax.set_ylabel(R"$\theta$", fontsize=20)
    ax.set_xticks(
        [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        [R"$0$", R"$\frac{\pi}{2}$", R"$\pi$", R"$\frac{3\pi}{2}$", R"$2\pi$"],
    )
    ax.set_yticks(
        [0, np.pi / 2, np.pi],
        [R"$0$", R"$\frac{\pi}{2}$", R"$\pi$"],
    )
    ax.grid("on")
    ax.set_aspect(1)

    cmap = mpl.colormaps["magma"]
    norm = mpl.colors.Normalize(vmin=0, vmax=len(result[1]) - 1)

    scattered = []
    for i, so in enumerate(result[1]):
        so = so[0]

        xy = np.sqrt(so[0] ** 2 + so[1] ** 2)
        if xy == 0:
            phi = 0
            if so[z] > 0:
                theta = 0
            else:
                theta = np.pi
        else:
            theta = np.arctan2(np.sqrt(so[0] ** 2 + so[1] ** 2), so[2])
            if theta < 0:
                theta *= 1
            phi = np.arctan2(so[1], so[0])
            if phi < 0:
                phi = 2 * np.pi + phi
        if theta is not None and phi is not None:
            scattered.append([phi, theta, i])
    scattered = np.array(scattered)
    phi = scattered[:, 0]
    theta = scattered[:, 1]
    i = scattered[:, 2]
    ax.scatter(phi, theta, zorder=10, ec="black", lw=1, fc=cmap(norm(i)), s=20)

    plt.savefig("test.png", dpi=300, bbox_inches="tight")
    plt.close()
