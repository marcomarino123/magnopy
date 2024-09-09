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

from typing import Iterable, Tuple

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
    r"""
    Energy of the :py:class:`.SpinHamiltonian`.

    Includes methods for energy optimization for three main types of the ground state
    and for the computation of the energy with the given spin arrangements.

    Being created from a given :py:class:`.SpinHamiltonian` it is completely independent
    from it. i.e. changes in the instance of the :py:class:`.SpinHamiltonian` class do
    not affect the instance of the :py:class:`.Energy` class.
    """

    def __init__(self, spinham: SpinHamiltonian):
        # Parameters of the Hamiltonian, private
        self._factor = spinham.exchange_factor
        self._atom_indices = dict(
            [(atom, i) for i, atom in enumerate(spinham.magnetic_atoms)]
        )

        # Parameters of the Hamiltonian, exposed to public as properties
        self._g_factors = [atom.g_factor for atom in spinham.magnetic_atoms]
        self._spins = [atom.spin for atom in spinham.magnetic_atoms]

        # Force double counting notation
        previous_dc = spinham.double_counting
        spinham.double_counting = True

        # Get all bonds of the Hamiltonian.
        self._bonds = []
        for atom1, atom2, R, J in spinham.exchange_like:
            i = self._atom_indices[atom1]
            j = self._atom_indices[atom2]
            d = spinham.get_distance(atom1, atom2, R)
            self._bonds.append([i, j, d, J])

        # Return original noatation of SpinHamiltonian
        spinham.double_counting = previous_dc

        # Minimisation settings, exposed to public as properties
        self._m = 10
        # Minimisation settings, private
        # Gradient size depends on the expected ground state: 3*I for Ferromagnetic, FIXME
        self._gradient_size = None

        # External physical conditions
        self._magnetic_field = None

        # To be sorted
        self.d_vec = np.zeros((self._m, 3 * len(self._spins)), dtype=float)
        self.y_vec = np.zeros((self._m, 3 * len(self._spins)), dtype=float)
        self.rho = np.zeros((self._m), dtype=float)
        self.gamma = np.zeros((self._m), dtype=float)

    ################################################################################
    #                             Minimization settings                            #
    ################################################################################

    @property
    def m(self) -> int:
        r"""
        Amount of steps to keep in memory for the estimation of the Hessian matrix in
        L-BFGS algorithm.

        Returns
        -------
        m : int
        """

        return self._m

    @m.setter
    def m(self, new_value):
        try:
            new_m = int(m)
        except:
            raise ValueError(
                "New size of memory storage for L-BFGS is not "
                f"an integer:{new_value}."
            )
        self._m = new_m

    ################################################################################
    #                         External physical conditions                         #
    ################################################################################

    @property
    def magnetic_field(self):
        r"""
        External magnetic field. Given in the units of Tesla.

        Returns
        =======
        magnetic_field : (3,) :numpy:`ndarray` or ``None``
            magnetic_field :math:`\boldsymbol{H}`.
        """
        return self._magnetic_field

    @magnetic_field.setter
    def magnetic_field(self, new_value):
        if new_value is None:
            self._magnetic_field = None
        else:
            try:
                new_field = np.array(new_vector, dtype=float)
            except:
                raise ValueError(f"New magnetic field is not array-like: {new_field}")

            if new_field.shape != (3,):
                raise ValueError(
                    "New magnetic field has to be a 3 component vector, "
                    f"got {new_field.shape}"
                )

            self._magnetic_field = new_field

    ################################################################################
    #                         Parameters of the Hamiltonian                        #
    ################################################################################

    @property
    def g_factors(self):
        r"""
        g factor for all magnetic atoms.

        Returns
        -------
        g_factors : (I,) :numpy:`ndarray`
            Order is the same as in :py:attr:`.Energy.spins`.
        """
        return self._g_factors

    @g_factors.setter
    def g_factors(self, new_value):
        if not isinstance(Iterable):
            raise ValueError(f"New g factors must be an Iterable: {new_value}")

        if not len(new_value) == len(self._spins):
            raise ValueError(
                f"Expecten {len(self._spins)} g factors, got {len(new_value)}"
            )

        for i, g_factor in enumerate(new_value):
            try:
                new_value[i] = int(g_factor)
            except:
                raise ValueError(
                    f"One of the new g_factors (index {i}) is not "
                    f"an integer:{g_factor}."
                )
        self._g_factors = new_value

    @property
    def spins(self):
        r"""
        Value of spin for all magnetic atoms.

        Returns
        -------
        spins : (I,) :numpy:`ndarray`
            Order is the same as in :py:attr:`.SpinHamiltonian.magnetic_atoms`.
        """
        return self._spins

    @spins.setter
    def spins(self, new_value):
        if not isinstance(Iterable):
            raise ValueError(f"New spins must be an Iterable: {new_value}")

        if not len(new_value) == len(self._spins):
            raise ValueError(f"Expected {len(self._spins)} spins, got {len(new_value)}")

        for i, spin in enumerate(new_value):
            try:
                new_value[i] = int(spin)
            except:
                raise ValueError(
                    f"One of the new spins (index {i}) is not " f"an integer:{spin}."
                )
        self._spins = new_value

    ################################################################################
    #                              Gradients of energy                             #
    ################################################################################

    def _ferro_grad(self, spin_orientation, gradient_vector=None, torques=None):
        if gradient_vector is None:
            gradient_vector = np.zeros((3 * len(self._spins)), dtype=float)
        if torques is None:
            torques = np.zeros((len(self._spins), 3), dtype=float)

        for i in range(len(spin_orientation)):
            h = 1e-4
            gradient = []
            for j in range(3):
                spin_orientation[i][j] -= h
                f_minus_h = self.ferro(spin_orientation)
                spin_orientation[i][j] += 2 * h
                f_plus_h = self.ferro(spin_orientation)
                gradient.append((f_plus_h - f_minus_h) / 2 / h)
                spin_orientation[i][j] -= h

            t = np.cross(spin_orientation[i], gradient)
            for j in range(0, 3):
                torques[i][j] = t[j]
            gradient_vector[3 * i] = t[2]
            gradient_vector[3 * i + 1] = -t[1]
            gradient_vector[3 * i + 2] = t[0]

        return gradient_vector, torques

    def _antiferro_grad(self):
        raise NotImplementedError

    def _spiral_grad(self):
        raise NotImplementedError

    ################################################################################
    #                                    Energy                                    #
    ################################################################################

    def ferro(self, spin_orientation):
        r"""
        Computes energy of the generalized ferromagnetic state for given
        ``spin_orientation``.

        Parameters
        ----------
        spin_orientation : (I, 3) or (3,) |array-like|_
            Orientation of the spin vectors.
            If ``I = 1``, then both ``(1,3)`` and ``(3,)`` shaped inputs are accepted.

        Returns
        -------
        energy :  float.
            Energy of the Hamiltonian for the given ``spin_orientation``
        """

        # Check that the input is correct
        try:
            spin_orientation = np.array(spin_orientation, dtype=float)
        except:
            raise ValueError(f"spin_orientation is not array-like: {spin_orientation}")

        if spin_orientation.shape[-1] != 3:
            raise ValueError(
                f"spin_orientation has to have the last dimension of "
                f"size 3, got {spin_orientation.shape[-1]}"
            )

        # Make the input array have (I,3) shape for I = 1
        if len(self._spins) == 1 and spin_orientation.shape == (3,):
            spin_orientation = np.array([spin_orientation])

        if len(self._spins) != spin_orientation.shape[0]:
            raise ValueError(
                f"Expected {len(self._spins)} spin orientations, "
                f"got {spin_orientation.shape[0]}"
            )

        energy = 0

        # Compute exchange and single-ion-like anisotropy energy
        for i, j, _, J in self._bonds:
            energy += (
                self._factor
                * self._spins[i]
                * self._spins[j]
                * np.einsum(
                    "i,ij,j", spin_orientation[i], J.matrix, spin_orientation[j]
                )
            )

        # Compute zeeman energy
        if self.magnetic_field is not None:
            energy += BOHR_MAGNETON * np.einsum(
                "i,j,ij", self._g_factors, self.magnetic_field, spin_orientation
            )

        return energy

    def antiferro(self):
        raise NotImplementedError

    def spiral(self):
        raise NotImplementedError

    ################################################################################
    #                             Optimization routines                            #
    ################################################################################

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
            spin_orientation = np.random.random((len(self._spins), 3))
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
        torques = np.zeros((len(self._spins), 3), dtype=float)
        gradient_vector = np.zeros((3 * len(self._spins)), dtype=float)
        search_direction = np.zeros((3 * len(self._spins)), dtype=float)
        tmp_stopper = 0
        while torque_max > tol_torque or abs(energy_diff) > tol_energy:
            energy_prev = self.ferro(spin_orientation)

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
            energy_current = self.ferro(spin_orientation)
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

    def optimize_antiferro(self):
        raise NotImplementedError

    def optimize_spiral(self):
        raise NotImplementedError

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
        n = k % self._m

        if k == 0:
            self.d_vec = np.zeros((self._m, 3 * len(self._spins)), dtype=float)
            self.y_vec = np.zeros((self._m, 3 * len(self._spins)), dtype=float)
            self.rho = np.zeros((self._m), dtype=float)
            self.gamma = np.zeros((self._m), dtype=float)
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

            for l in range(self._m - 1, -1):
                j = (l + n + 1) % self._m
                self.gamma[j] = self.rho[j] * (self.d_vec[j] @ q)
                q = q - self.gamma[j] * self.y_vec[j]
            search_direction = q / self.rho[n] / (np.linalg.norm(self.y_vec[n]))
            for l in range(0, self._m):
                if k < self._m:
                    j = l
                else:
                    j = (l + n + 1) % self._m
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
        fx = self.ferro(spin_orientation)
        x_new = update_spin_directions(spin_orientation, search_direction, a)
        nabla_new = self._ferro_grad(x_new)[0]
        nabla = self._ferro_grad(spin_orientation)[0]
        i = 0
        while (
            self.ferro(x_new) >= fx + (c1 * a * nabla.T @ search_direction)
            or nabla_new.T @ search_direction <= c2 * nabla.T @ search_direction
        ):
            a *= 0.5
            x_new = update_spin_directions(spin_orientation, search_direction, a)
            nabla_new = self._ferro_grad(x_new)[0]
            if i > iter_max:
                raise ValueError("Wolfe failed")
            i += 1
        return a


if __name__ == "__main__":
    from magnopy.io import load_spinham_txt

    spinham = load_spinham_txt("/Users/rybakov.ad/Codes/magnopy/tmp/easy-along-x.txt")
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
            data[i][j] = energy.ferro(
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
