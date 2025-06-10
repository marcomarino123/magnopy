# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2025 Magnopy Team
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

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def _cubic_interpolation(alpha_l, alpha_h, f_l, f_h, fp_l, fp_h):
    r"""
    Computes the minimum of a cubic interpolation for the function f(alpha) with
    values f_l, f_h and derivatives fp_l, fp_h at the points alpha_l, alpha_h.

    Parameters
    ----------
    alpha_l : float
        Lower bound of the interval.
    alpha_h : float
        Upper bound of the interval.
    f_l : float
        Value of the function at alpha_l.
    f_h : float
        Value of the function at alpha_h.
    fp_l : float
        Derivative of the function at alpha_l.
    fp_h : float
        Derivative of the function at alpha_h.

    Returns
    -------
    alpha_min : float
        Position of the minimum of the cubic interpolation for the function f(alpha).
    """

    d_1 = fp_l + fp_h - 3 * (f_l - f_h) / (alpha_l - alpha_h)

    if d_1**2 - fp_l * fp_h < 0:
        return alpha_h

    d_2 = np.sign(alpha_h - alpha_l) * np.sqrt(d_1**2 - fp_l * fp_h)

    return alpha_h - (alpha_h - alpha_l) * (fp_h + d_2 - d_1) / (fp_h - fp_l + 2 * d_2)


def _rotate_sd(reference_directions, rotation):
    r"""

    Parameters
    ----------
    reference_directions : (M, 3) :numpy:`ndarray`
        Reference direction of the spin vectors.
    rotation : (M*3,) :numpy:`ndarray`
        Rotation of the spin vectors parameterized with the skew-symmetric matrix.

    Returns
    -------
    directions : (I, 3) :numpy:`ndarray`
        Rotated set of direction vectors.
    """

    directions = reference_directions.copy()

    ax = rotation[::3]
    ay = rotation[1::3]
    az = rotation[2::3]

    thetas = np.sqrt(ax**2 + ay**2 + az**2)

    r = []
    for alpha in range(len(thetas)):
        theta = thetas[alpha]

        if theta < np.finfo(float).eps:
            continue

        r = np.array([ax[alpha], ay[alpha], az[alpha]]) / theta

        directions[alpha] = (
            np.cos(theta) * directions[alpha]
            + np.sin(theta) * np.cross(r, directions[alpha])
            + (1 - np.cos(theta)) * r * (r @ directions[alpha])
        )

    return directions


def _zoom(
    spin_directions,
    search_direction,
    func,
    grad,
    func_0,
    grad_0,
    alpha_lo,
    alpha_hi,
    c1,
    c2,
):
    r"""
    Zoom function for the line search with strong Wolfe conditions.

    Parameters
    ----------
    true_variables_k : ...
        Current true variables. Form and type depends on the ground state sub-type.
        Calls of ``func(true_variables_k)``, ``grad(true_variables_k)`` have to be valid.
    search_direction : :numpy:`ndarray`
        Search direction.
    func : callable
        Energy function. The call ``func(true_variables_k)`` has to be valid.
    grad : callable
        Gradient of the energy function. The call ``grad(true_variables_k)`` has
        to be valid.
    update : callable
        Function that update the true variables to the new state defined by the
        :math:`\boldsymbol{x}` vector.
    func_0 : float
        Energy at the current state: ``func(true_variables_k)``.
    grad_0 : :numpy:`ndarray`
        Gradient of the energy at the current state: ``grad(true_variables_k)``.
    alpha_lo : float
        Lower bound of the step length.
    alpha_hi : float
        Upper bound of the step length.
    c1 : float
        Parameter for the Wolfe conditions.
    c2 : float
        Parameter for the Wolfe conditions.
    """

    f_0 = func_0
    fp_0 = grad_0 @ search_direction

    spin_directions_lo = _rotate_sd(
        reference_directions=spin_directions, rotation=alpha_lo * search_direction
    )
    spin_directions_hi = _rotate_sd(
        reference_directions=spin_directions, rotation=alpha_hi * search_direction
    )

    f_lo = func(spin_directions_lo)
    fp_lo = grad(spin_directions_lo).flatten() @ search_direction
    f_hi = func(spin_directions_hi)
    fp_hi = grad(spin_directions_hi).flatten() @ search_direction
    f_j_min = None
    trial_steps = 0

    while True:
        if abs(alpha_hi - alpha_lo) < np.finfo(float).eps:
            return alpha_lo

        alpha_j = _cubic_interpolation(
            alpha_l=alpha_lo,
            alpha_h=alpha_hi,
            f_l=f_lo,
            f_h=f_hi,
            fp_l=fp_lo,
            fp_h=fp_hi,
        )

        spin_directions_j = _rotate_sd(
            reference_directions=spin_directions, rotation=alpha_j * search_direction
        )

        f_j = func(spin_directions_j)
        fp_j = grad(spin_directions_j).flatten() @ search_direction

        if f_j_min is None:
            f_j_min = f_j
        else:
            if f_j < f_j_min:
                trial_steps = 0
                f_j_min = f_j
            elif trial_steps >= 10:
                print(f"Trial steps > 10")
                return alpha_j
            else:
                trial_steps += 1

        if f_j > f_0 + c1 * alpha_j * fp_0 or f_j >= f_lo:
            alpha_hi = alpha_j
            f_hi = f_j
            fp_hi = fp_j
        else:
            if abs(fp_j) <= -c2 * fp_0:
                return alpha_j

            if fp_j * (alpha_hi - alpha_lo) >= 0:
                alpha_hi = alpha_lo
                f_hi = f_lo
                fp_hi = fp_lo

            alpha_lo = alpha_j
            f_lo = f_j
            fp_lo = fp_j


def _line_search(
    spin_directions,
    search_direction,
    func,
    grad,
    func_0,
    grad_0,
    c1=1e-4,
    c2=0.9,
    max_iterations=10000,
    alpha_max=3.0,
):
    r"""
    Computes step length via line search with strong Wolfe conditions.

    Parameters
    ----------
    true_variables_k : ...
        Current true variables. Form and type depends on the ground state sub-type.
        Calls of ``func(true_variables_k)``, ``grad(true_variables_k)`` have to be valid.
    search_direction : :numpy:`ndarray`
        Search direction.
    func : callable
        Energy function. The call ``func(true_variables_k)`` has to be valid.
    grad : callable
        Gradient of the energy function. The call ``grad(true_variables_k)`` has
        to be valid.
    func_0 : float
        Energy at the current state: ``func(true_variables_k)``.
    grad_0 : :numpy:`ndarray`
        Gradient of the energy at the current state: ``grad(true_variables_k)``.
    c1 : float, default 1e-4
        Parameter for the Wolfe conditions.
    c2 : float, default 0.9
        Parameter for the Wolfe conditions.
    max_iterations : int, default 10000
        Maximum number of iterations.
    alpha_max: float, default 3.0
        Maximum step length.
    """

    alpha_im1 = 0
    alpha_i = 1.1
    f_0 = func_0
    fp_0 = grad_0 @ search_direction
    f_im1 = f_0

    spin_directions_max = _rotate_sd(
        reference_directions=spin_directions, rotation=alpha_max * search_direction
    )
    f_max = func(spin_directions_max)
    fp_max = grad(spin_directions_max).flatten() @ search_direction

    for i in range(1, max_iterations):
        print(f"line search: {i}")
        spin_directions_i = _rotate_sd(
            reference_directions=spin_directions, rotation=alpha_i * search_direction
        )
        f_i = func(spin_directions_i)

        if f_i > f_0 + c1 * alpha_i * fp_0 or (i > 1 and f_i >= f_im1):
            print("ls1")
            return _zoom(
                spin_directions=spin_directions,
                search_direction=search_direction,
                func=func,
                grad=grad,
                func_0=func_0,
                grad_0=grad_0,
                alpha_lo=alpha_im1,
                alpha_hi=alpha_i,
                c1=c1,
                c2=c2,
            )

        fp_i = grad(spin_directions_i).flatten() @ search_direction

        if abs(fp_i) <= -c2 * fp_0:
            print("ls2")
            return alpha_i

        if fp_i >= 0:
            print("ls3")
            return _zoom(
                spin_directions=spin_directions,
                search_direction=search_direction,
                func=func,
                grad=grad,
                func_0=func_0,
                grad_0=grad_0,
                alpha_lo=alpha_i,
                alpha_hi=alpha_im1,
                c1=c1,
                c2=c2,
            )

        if abs(alpha_i - alpha_im1) < np.finfo(float).eps:
            print("ls4")
            return alpha_i

        alpha_ip1 = _cubic_interpolation(
            alpha_l=alpha_i,
            alpha_h=alpha_max,
            f_l=f_i,
            f_h=f_max,
            fp_l=fp_i,
            fp_h=fp_max,
        )

        if alpha_im1 > alpha_max:
            print("ls5")
            return alpha_max

        alpha_im1 = alpha_i
        f_im1 = f_i

        alpha_i = alpha_ip1

    raise ValueError(f"Line search failed after {max_iterations} iterations.")


class Energy:
    r"""
    Ground state energy of the given spin Hamiltonian.

    This class is optimized for the computation of the energy for any spin
    directions for the given Hamiltonian.

    If the spin Hamiltonian is modified, then a new instance of the energy class
    should be created from it.

    Parameters
    ----------
    spinham : py:class:.SpinHamiltonian`
        Spin Hamiltonian for the calculation of energy.
    """

    def __init__(self, spinham):
        initial_convention = spinham.convention

        magnopy_convention = initial_convention.get_modified(
            spin_normalized=False, multiple_counting=False
        )

        spinham.convention = magnopy_convention

        self.spins = np.array(spinham.magnetic_atoms.spins, dtype=float)
        self.M = spinham.M

        ########################################################################
        #                               One spin                               #
        ########################################################################

        self.J_1 = np.zeros((spinham.M, 3), dtype=float)

        for atom, parameter in spinham.p1:
            alpha = spinham.map_to_magnetic[atom]

            self.J_1[alpha] += spinham.convention.c1 * parameter

        ########################################################################
        #                               Two spins                              #
        ########################################################################

        self.J_21 = np.zeros((spinham.M, 3, 3), dtype=float)

        for atom, parameter in spinham.p21:
            alpha = spinham.map_to_magnetic[atom]

            self.J_21[alpha] += spinham.convention.c21 * parameter

        self.J_22 = {}

        for atom1, atom2, _, parameter in spinham.p22:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]

            if (alpha, beta) not in self.J_22:
                self.J_22[(alpha, beta)] = np.zeros((3, 3), dtype=float)

            self.J_22[(alpha, beta)] += spinham.convention.c22 * parameter

        ########################################################################
        #                              Three spins                             #
        ########################################################################

        self.J_31 = np.zeros((spinham.M, 3, 3, 3), dtype=float)

        for atom, parameter in spinham.p31:
            alpha = spinham.map_to_magnetic[atom]

            self.J_31[alpha] += spinham.convention.c31 * parameter

        self.J_32 = {}

        for atom1, atom2, _, parameter in spinham.p32:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]

            if (alpha, beta) not in self.J_32:
                self.J_32[(alpha, beta)] = np.zeros((3, 3, 3), dtype=float)

            self.J_32[(alpha, beta)] += spinham.convention.c32 * parameter

        self.J_33 = {}

        for atom1, atom2, atom3, _, _, parameter in spinham.p33:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]
            gamma = spinham.map_to_magnetic[atom3]

            if (alpha, beta, gamma) not in self.J_33:
                self.J_33[(alpha, beta, gamma)] = np.zeros((3, 3, 3), dtype=float)

            self.J_33[(alpha, beta, gamma)] += spinham.convention.c33 * parameter

        ########################################################################
        #                              Four spins                              #
        ########################################################################

        self.J_41 = np.zeros((spinham.M, 3, 3, 3, 3), dtype=float)

        for atom, parameter in spinham.p41:
            alpha = spinham.map_to_magnetic[atom]

            self.J_41[alpha] += spinham.convention.c41 * parameter

        self.J_421 = {}

        for atom1, atom2, _, parameter in spinham.p421:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]

            if (alpha, beta) not in self.J_421:
                self.J_421[(alpha, beta)] = np.zeros((3, 3, 3, 3), dtype=float)

            self.J_421[(alpha, beta)] += spinham.convention.c421 * parameter

        self.J_422 = {}

        for atom1, atom2, _, parameter in spinham.p422:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]

            if (alpha, beta) not in self.J_422:
                self.J_422[(alpha, beta)] = np.zeros((3, 3, 3, 3), dtype=float)

            self.J_422[(alpha, beta)] += spinham.convention.c422 * parameter

        self.J_43 = {}

        for atom1, atom2, atom3, _, _, parameter in spinham.p43:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]
            gamma = spinham.map_to_magnetic[atom3]

            if (alpha, beta, gamma) not in self.J_43:
                self.J_43[(alpha, beta, gamma)] = np.zeros((3, 3, 3, 3), dtype=float)

            self.J_43[(alpha, beta, gamma)] += spinham.convention.c43 * parameter

        self.J_44 = {}

        for atom1, atom2, atom3, atom4, _, _, _, parameter in spinham.p44:
            alpha = spinham.map_to_magnetic[atom1]
            beta = spinham.map_to_magnetic[atom2]
            gamma = spinham.map_to_magnetic[atom3]
            epsilon = spinham.map_to_magnetic[atom4]

            if (alpha, beta, gamma, epsilon) not in self.J_44:
                self.J_44[(alpha, beta, gamma, epsilon)] = np.zeros(
                    (3, 3, 3, 3), dtype=float
                )

            self.J_44[(alpha, beta, gamma, epsilon)] += (
                spinham.convention.c44 * parameter
            )

        spinham.convention = initial_convention

    def E_0(self, spin_directions) -> float:
        r"""

        Parameters
        ----------
        spin_directions : (M, 3) |array-like|_
            Directions of spin vectors. Only directions of vectors are used,
            modulus is ignored. ``M`` is the amount of magnetic atoms in the
            Hamiltonian. The order of spin directions is the same as the order
            of magnetic atoms in ``spinham.magnetic_atoms.spins``.

        Returns
        -------
        E_0 : float
            Classic energy of state with ``spin_directions``.
        """

        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions = (
            spin_directions / np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        )
        spins = spin_directions * self.spins[:, np.newaxis]

        energy = 0

        energy += np.diag(self.J_1 @ spins.T).sum()

        energy += np.einsum("mij,mi,mj->m", self.J_21, spins, spins).sum()

        energy += np.einsum("miju,mi,mj,mu->m", self.J_31, spins, spins, spins).sum()

        energy += np.einsum(
            "mijuv,mi,mj,mu,mv->m", self.J_41, spins, spins, spins, spins
        ).sum()

        for alpha, beta in self.J_22:
            energy += spins[alpha] @ self.J_22[(alpha, beta)] @ spins[beta]

        for alpha, beta in self.J_32:
            energy += np.einsum(
                "iju,i,j,u",
                self.J_32[(alpha, beta)],
                spins[alpha],
                spins[alpha],
                spins[beta],
            )

        for alpha, beta in self.J_421:
            energy += np.einsum(
                "ijuv,i,j,u,v",
                self.J_421[(alpha, beta)],
                spins[alpha],
                spins[alpha],
                spins[alpha],
                spins[beta],
            )

        for alpha, beta in self.J_422:
            energy += np.einsum(
                "ijuv,i,j,u,v",
                self.J_422[(alpha, beta)],
                spins[alpha],
                spins[alpha],
                spins[beta],
                spins[beta],
            )

        for alpha, beta, gamma in self.J_33:
            energy += np.einsum(
                "iju,i,j,u",
                self.J_33[(alpha, beta, gamma)],
                spins[alpha],
                spins[beta],
                spins[gamma],
            )

        for alpha, beta, gamma in self.J_43:
            energy += np.einsum(
                "ijuv,i,j,u,v",
                self.J_43[(alpha, beta, gamma)],
                spins[alpha],
                spins[alpha],
                spins[beta],
                spins[gamma],
            )

        for alpha, beta, gamma, epsilon in self.J_44:
            energy += np.einsum(
                "ijuv,i,j,u,v",
                self.J_44[(alpha, beta, gamma, epsilon)],
                spins[alpha],
                spins[beta],
                spins[gamma],
                spins[epsilon],
            )

        return float(energy)

    def gradient(self, spin_directions):
        r"""

        Parameters
        ----------
        spin_directions : (M, 3) |array-like|_
            Directions of spin vectors. Only directions of vectors are used,
            modulus is ignored. ``M`` is the amount of magnetic atoms in the
            Hamiltonian. The order of spin directions is the same as the order
            of magnetic atoms in ``spinham.magnetic_atoms.spins``.

        Returns
        -------
        gradient : (M, 3) :numpy:`ndarray`
            Gradient of energy.

            .. code-block:: python

                [
                    [ dE/dz1x, dE/dz1y, dE/dz1z ],
                    [ dE/dz2x, dE/dz2y, dE/dz2z ],
                    ...
                    [ dE/dzMx, dE/dzMy, dE/dzMz ]
                ]
        """

        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions = (
            spin_directions / np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        )

        gradient = np.zeros((self.M, 3), dtype=float)

        gradient += self.J_1 * self.spins[:, np.newaxis]

        gradient += np.einsum(
            "mtj,mj,m->mt", self.J_21, spin_directions, self.spins**2
        )

        gradient += np.einsum(
            "mtju,mj,mu,m->mt",
            self.J_31,
            spin_directions,
            spin_directions,
            self.spins**3,
        )

        gradient += np.einsum(
            "mtjuv,mj,mu,mv,m->mt",
            self.J_41,
            spin_directions,
            spin_directions,
            spin_directions,
            self.spins**4,
        )

        for alpha, beta in self.J_22:
            gradient[alpha] += (
                self.J_22[(alpha, beta)]
                @ spin_directions[beta]
                * self.spins[alpha]
                * self.spins[beta]
            )

        for alpha, beta in self.J_32:
            gradient[alpha] += (
                np.einsum(
                    "tju,j,u->t",
                    self.J_32[(alpha, beta)],
                    spin_directions[alpha],
                    spin_directions[beta],
                )
                * self.spins[alpha] ** 2
                * self.spins[beta]
            )

        for alpha, beta in self.J_421:
            gradient[alpha] += (
                np.einsum(
                    "tjuv,j,u,v->t",
                    self.J_421[(alpha, beta)],
                    spin_directions[alpha],
                    spin_directions[alpha],
                    spin_directions[beta],
                )
                * self.spins[alpha] ** 3
                * self.spins[beta]
            )

        for alpha, beta in self.J_422:
            gradient[alpha] += (
                np.einsum(
                    "tjuv,j,u,v->t",
                    self.J_422[(alpha, beta)],
                    spin_directions[alpha],
                    spin_directions[beta],
                    spin_directions[beta],
                )
                * self.spins[alpha] ** 2
                * self.spins[beta] ** 2
            )

        for alpha, beta, gamma in self.J_33:
            gradient[alpha] += (
                np.einsum(
                    "tju,j,u->t",
                    self.J_33[(alpha, beta, gamma)],
                    spin_directions[beta],
                    spin_directions[gamma],
                )
                * self.spins[alpha]
                * self.spins[beta]
                * self.spins[gamma]
            )

        for alpha, beta, gamma in self.J_43:
            gradient[alpha] += (
                np.einsum(
                    "tjuv,j,u,v->t",
                    self.J_43[(alpha, beta, gamma)],
                    spin_directions[beta],
                    spin_directions[gamma],
                )
                * self.spins[alpha] ** 2
                * self.spins[beta]
                * self.spins[gamma]
            )

        for alpha, beta, gamma, epsilon in self.J_44:
            gradient[alpha] += (
                np.einsum(
                    "tjuv,j,u,v->t",
                    self.J_44[(alpha, beta, gamma, epsilon)],
                    spin_directions[beta],
                    spin_directions[gamma],
                    spin_directions[epsilon],
                )
                * self.spins[alpha]
                * self.spins[beta]
                * self.spins[gamma]
                * self.spins[epsilon]
            )

        return gradient

    def torque(self, spin_directions):
        r"""
        Computes torque on each spin.

        Parameters
        ----------
        spin_directions : (M, 3) |array-like|_
            Directions of spin vectors. Only directions of vectors are used,
            modulus is ignored. ``M`` is the amount of magnetic atoms in the
            Hamiltonian. The order of spin directions is the same as the order
            of magnetic atoms in ``spinham.magnetic_atoms.spins``.

        Returns
        -------
        torque : (M, 3) :numpy:`ndarray`

            .. code-block:: python

                [
                    [ t1x, t1y, t1z ],
                    [ t2x, t2y, t2z ],
                    ...
                    [ tMx, tMy, tMz ]
                ]
        """
        return np.cross(spin_directions, self.gradient(spin_directions=spin_directions))

    def _hessian(self, spin_directions):
        h = 1e-6

        hessian = np.zeros((self.M * 3, self.M * 3), dtype=float)

        for i in range(self.M * 3):
            for j in range(self.M * 3):
                x_pp = np.zeros(self.M * 3, dtype=float)
                x_pm = np.zeros(self.M * 3, dtype=float)
                x_mp = np.zeros(self.M * 3, dtype=float)
                x_mm = np.zeros(self.M * 3, dtype=float)

                x_pp[i] += h
                x_pp[j] += h

                x_pm[i] += h
                x_pm[j] -= h

                x_mp[i] -= h
                x_mp[j] += h

                x_mm[i] -= h
                x_mm[j] -= h

                spin_directions_pp = _rotate_sd(
                    reference_directions=spin_directions, rotation=x_pp
                )
                spin_directions_pm = _rotate_sd(
                    reference_directions=spin_directions, rotation=x_pm
                )
                spin_directions_mp = _rotate_sd(
                    reference_directions=spin_directions, rotation=x_mp
                )
                spin_directions_mm = _rotate_sd(
                    reference_directions=spin_directions, rotation=x_mm
                )

                hessian[i, j] = (
                    (
                        self.E_0(spin_directions=spin_directions_pp)
                        - self.E_0(spin_directions=spin_directions_pm)
                        - self.E_0(spin_directions=spin_directions_mp)
                        + self.E_0(spin_directions=spin_directions_mm)
                    )
                    / 4
                    / h
                    / h
                )
        return hessian

    def optimize(
        self, initial_guess=None, energy_tolerance=1e-5, torque_tolerance=1e-5
    ):
        r"""
        Optimize the energy with respect to the directions of spins in the unit cell.

        Parameters
        ----------
        initial_guess : (M, 3) or (3,) |array-like|_, optional
            Initial guess for the direction of the spin vectors.
        energy_tolerance : float, default 1e-5
            Energy tolerance for the two consecutive steps of the optimization.
        torque_tolerance : float, default 1e-5
            Torque tolerance for the two consecutive steps of the optimization.

        Returns
        -------
        optimized_directions : (M, 3) :numpy:`ndarray`
            Optimized direction of the spin vectors.
        """

        if initial_guess is None:
            initial_guess = np.random.uniform(low=-1, high=1, size=(self.M, 3))

        spin_directions = (
            initial_guess / np.linalg.norm(initial_guess, axis=1)[:, np.newaxis]
        )

        tolerance = np.array([energy_tolerance, torque_tolerance])
        difference = 2 * tolerance

        # hessian_inv = np.linalg.inv(self._hessian(spin_directions=spin_directions))
        hessian_inv = np.eye(self.M * 3, dtype=float)

        func = self.E_0(spin_directions=spin_directions)
        grad = self.torque(spin_directions=spin_directions).flatten()

        step_counter = 0
        first_run = True

        while (difference >= tolerance).any():
            search_direction = -hessian_inv @ grad

            alpha = _line_search(
                spin_directions=spin_directions,
                search_direction=search_direction,
                func=self.E_0,
                grad=self.torque,
                func_0=func,
                grad_0=grad,
            )

            s = alpha * search_direction
            spin_directions_next = _rotate_sd(
                reference_directions=spin_directions, rotation=s
            )

            grad_next = self.torque(spin_directions=spin_directions_next).flatten()
            func_next = self.E_0(spin_directions=spin_directions_next)

            difference = np.array(
                [
                    abs(func_next - func),
                    np.linalg.norm(grad_next.reshape(self.M, 3), axis=1).max(),
                ]
            )

            step_counter += 1

            if (difference < tolerance).all():
                break

            y = grad_next - grad

            print(f"s@y: {alpha} {s @ y}")
            rho = 1 / (y @ s)

            EYE = np.eye(self.M * 3, dtype=float)
            OUTER = np.outer(y, s)

            if first_run:
                first_run = False
                hessian_inv = (y @ s) / (y @ y) * hessian_inv

            hessian_inv = (EYE - rho * OUTER.T) @ hessian_inv @ (
                EYE - rho * OUTER
            ) + rho * np.outer(s, s)

            grad = grad_next
            func = func_next
            spin_directions = spin_directions_next

            print(difference[0], difference[1])

        return spin_directions_next


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir


if __name__ == "__main__":
    from magnopy.examples import ivuzjo

    spinham = ivuzjo(N=10)

    energy = Energy(spinham=spinham)

    optimized_sd = energy.optimize()
