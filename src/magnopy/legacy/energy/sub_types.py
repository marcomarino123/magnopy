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


import logging

import numpy as np

from magnopy.energy.checkers import _check_directions
from magnopy.energy.optimize import _bfgs as _optimize
from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.units.inside import ENERGY
from magnopy.units.si import BOHR_MAGNETON

_logger = logging.getLogger(__name__)

__all__ = ["C1", "C2", "C5"]  # , "C3", "C4"]

# Convert to the internal units of energy
BOHR_MAGNETON = BOHR_MAGNETON / ENERGY


class _Energy:
    r"""
    Generic energy class.
    """

    def __init__(self, spinham: SpinHamiltonian):
        self._magnetic_field = None
        # Parameters of the Hamiltonian, private
        self._atom_indices = dict(
            [(atom, i) for i, atom in enumerate(spinham.magnetic_atoms)]
        )
        self._g_factors = [atom.g_factor for atom in spinham.magnetic_atoms]
        self._spins = [atom.spin for atom in spinham.magnetic_atoms]

        self._I = len(self._spins)

        self._cell = spinham.cell

        # Force double counting notation
        previous_dc = spinham.double_counting
        previous_factor = spinham.exchange_factor
        previous_spin_normalized = spinham.spin_normalized
        spinham.double_counting = True
        spinham.exchange_factor = 0.5
        spinham.spin_normalized = True

        # Get all bonds of the Hamiltonian.
        self._bonds = []
        for atom1, atom2, R, J in spinham.exchange_like:
            i = self._atom_indices[atom1]
            j = self._atom_indices[atom2]
            d = R @ spinham.cell
            self._bonds.append([i, j, d, J])

        # Return original notation of SpinHamiltonian
        spinham.double_counting = previous_dc
        spinham.exchange_factor = previous_factor
        spinham.spin_normalized = previous_spin_normalized

    @property
    def magnetic_field(self):
        r"""
        Magnetic field vector.
        """
        return self._magnetic_field

    @magnetic_field.setter
    def magnetic_field(self, new_value):
        # Check that the input is array-like and convertible to floats
        try:
            new_value = np.array(new_value, dtype=float)
        except:
            raise ValueError(f"Magnetic field is not array-like: {new_value}.")

        # Check that the shape and size are correct
        if new_value.shape != (3,):
            raise ValueError(
                f"Magnetic field has to have shape (3,), got {new_value.shape}."
            )

        self._magnetic_field = new_value

    @property
    def spiral_vector(self):
        raise RuntimeError(
            f"Discrete spiral vector is not defined for the energy type "
            f"{self.__class__.__name__}."
        )

    @spiral_vector.setter
    def spiral_vector(self, new_value):
        raise RuntimeError(
            f"Discrete spiral vector is not defined for the energy type "
            f"{self.__class__.__name__}."
        )

    def energy(*args, **kwargs):
        raise NotImplementedError

    def gradient(*args, **kwargs):
        raise NotImplementedError

    def _F(*args, **kwargs):
        raise NotImplementedError

    def _grad_F(*args, **kwargs):
        raise NotImplementedError

    def _to_x(true_variables):
        raise NotImplementedError

    def _update(true_variables, x):
        raise NotImplementedError

    def _update_difference(func_k, func_kp1, grad_kp1):
        raise NotImplementedError

    def optimize(*args, **kwargs):
        raise NotImplementedError


class C1(_Energy):
    def __init__(self, spinham: SpinHamiltonian):
        super().__init__(spinham)

        self.J = np.zeros((self._I, self._I, 3, 3), dtype=float)

        for i, j, _, J in self._bonds:
            self.J[i, j] += J.matrix

    def energy(self, directions, check_input=True) -> float:
        r"""
        Compute the energy of the system with respect to the provided directions of
        spins. Computed according to the formula FIXME of FIXME.

        Parameters
        ----------
        directions : (I, 3) or (3,) |array-like|_
            Orientation of the spin vectors.
            If ``I = 1``, then both ``(1,3)`` and ``(3,)`` shaped inputs are accepted.
            The vectors are normalized to one, i.e. only the direction of the vectors
            is important.
        check_input : bool, default=True
            Whether to check the correctness of the input. Better keep it ``True``
            always, unless you need to compute energy thousands of times and you control
            the input correctness externally.

        Returns
        -------
        energy : float
            Energy of the system.
        """

        if check_input:
            directions = _check_directions(self._I, directions)

        energy = 0

        # Compute exchange and single-ion-like anisotropy energy
        energy += 0.5 * np.einsum(
            "i,j,ix,jy,ijxy",
            self._spins,
            self._spins,
            directions,
            directions,
            self.J,
        )

        # Compute zeeman energy
        if self.magnetic_field is not None:
            energy += BOHR_MAGNETON * np.einsum(
                "i,i,j,ij",
                self._g_factors,
                self._spins,
                self.magnetic_field,
                directions,
            )

        return energy

    def gradient(self, directions, check_input=True) -> np.ndarray:
        r"""
        Compute the gradient of the energy with respect to the provided directions of
        spins. Computed according to the formula FIXME of FIXME.

        Parameters
        ----------
        directions : (I, 3) or (3,) |array-like|_
            Orientation of the spin vectors.
            If ``I = 1``, then both ``(1,3)`` and ``(3,)`` shaped inputs are accepted.
            The vectors are normalized to one, i.e. only the direction of the vectors
            is important.
        check_input : bool, default=True
            Whether to check the correctness of the input. Better keep it ``True``
            always, unless you need to compute energy thousands of times and you control
            the input correctness externally.

        Returns
        -------
        gradient : (I,3) :numpy:`ndarray`
            Gradient of the energy. Form:

            .. code-block:: python

                [
                    [ dE/de1x, dE/de1y, dE/de1z ],
                    [ dE/de2x, dE/de2y, dE/de2z ],
                    ...
                    [ dE/deIx, dE/deIy, dE/deIz ]
                ]
        """

        if check_input:
            directions = _check_directions(self._I, directions)

        gradient = np.zeros_like(directions, dtype=float)

        # Derivative of the Zeeman term
        if self.magnetic_field is not None:
            gradient += BOHR_MAGNETON * np.einsum(
                "b,b,x->bx",
                self._g_factors,
                self._spins,
                self.magnetic_field,
            )

        # Derivative of bilinear term
        gradient += np.einsum(
            "ak,a,b,abkx->bx",
            directions,
            self._spins,
            self._spins,
            self.J,
        )

        return gradient

    def _F(self, true_variables) -> float:
        # Remove input check as this function is specific for the minimization procedure
        return self.energy(true_variables, check_input=False)

    def _grad_F(self, true_variables) -> np.ndarray:
        r"""
        Compute the gradient of the energy as a function of
        :math:`(a^x_1, a^y_1, a^z_1, ..., a^x_I, a^y_I, a^z_I)` for the C1 sub-type.

        Parameters
        ----------
        true_variables : (I, 3) :numpy:`ndarray`
            Directions of the spin vectors.

        Returns
        -------
        gradient : (I*3,) :numpy:`ndarray`
            Gradient of the energy. Form:

            .. code-block:: python

                [ dF/da1x, dF/da1y, dF/da1z, ..., dF/daIx, dF/daIy, dF/daIz ]
        """

        directions = true_variables

        # Remove input check as this function is specific for the minimization procedure
        gradient = self.gradient(directions, check_input=False)

        torque = np.cross(directions, gradient)

        return torque.flatten()

    def _to_x(self, true_variables):
        r"""

        Parameters
        ----------
        true_variables : (I, 3) :numpy:`ndarray`
            Original direction of the spin vectors.

        Returns
        -------
        x : (I*3,) :numpy:`ndarray`
            Direction of the spin vectors parameterized with the skew-symmetric matrix.
        """

        return np.zeros(true_variables.size, dtype=float)

    def _update(self, true_variables, x):
        r"""

        Parameters
        ----------
        true_variables : (I, 3) :numpy:`ndarray`
            Original direction of the spin vectors.
        x : (I*3,) :numpy:`ndarray`
            Direction of the spin vectors parameterized with the skew-symmetric matrix.

        Returns
        -------
        directions : (I, 3) :numpy:`ndarray`
            Rotated set of direction vectors.
        """

        directions = true_variables.copy()

        ax = x[::3]
        ay = x[1::3]
        az = x[2::3]

        thetas = np.sqrt(ax**2 + ay**2 + az**2)

        r = []
        for i in range(len(thetas)):
            theta = thetas[i]

            if theta < np.finfo(float).eps:
                continue

            r = np.array([ax[i], ay[i], az[i]]) / theta

            directions[i] = (
                np.cos(theta) * directions[i]
                + np.sin(theta) * np.cross(r, directions[i])
                + (1 - np.cos(theta)) * r * (r @ directions[i])
            )

        return directions

    def _update_difference(self, func_k, func_kp1, grad_kp1):
        r"""
        Computes the difference between two consecutive steps of the optimization.

        Parameters
        ----------
        func_k : float
            Energy at the current step.
        func_kp1 : float
            Energy at the next step.
        grad_kp1 : (I*3,) :numpy:`ndarray`
            Gradient of the energy at the next state.

        Returns
        -------
        difference : (2,) :numpy:`ndarray`
            Difference between the two consecutive steps of the optimization.
        """

        return np.array(
            [
                abs(func_kp1 - func_k),
                np.linalg.norm(grad_kp1.reshape(grad_kp1.size // 3, 3), axis=1).max(),
            ]
        )

    def _hessian(self, true_variables):
        h = 1e-6

        x_0 = self._to_x(true_variables)

        hessian = np.zeros((x_0.size, x_0.size), dtype=float)

        for i in range(x_0.size):
            for j in range(x_0.size):
                x_pp = x_0.copy()
                x_pm = x_0.copy()
                x_mp = x_0.copy()
                x_mm = x_0.copy()

                x_pp[i] += h
                x_pp[j] += h

                x_pm[i] += h
                x_pm[j] -= h

                x_mp[i] -= h
                x_mp[j] += h

                x_mm[i] -= h
                x_mm[j] -= h

                tv_pp = self._update(true_variables, x_pp)
                tv_pm = self._update(true_variables, x_pm)
                tv_mp = self._update(true_variables, x_mp)
                tv_mm = self._update(true_variables, x_mm)

                hessian[i, j] = (
                    (self._F(tv_pp) - self._F(tv_pm) - self._F(tv_mp) + self._F(tv_mm))
                    / 4
                    / h
                    / h
                )

        return hessian

    def optimize(
        self, directions_ig=None, energy_tolerance=1e-5, torque_tolerance=1e-5
    ):
        r"""
        Optimize the energy with respect to the directions of spins in the unit cell.

        Parameters
        ----------
        directions_ig : (I, 3) or (3,) |array-like|_, optional
            Initial guess for the direction of the spin vectors.
        energy_tolerance : float, default 1e-5
            Energy tolerance for the two consecutive steps of the optimization.
        torque_tolerance : float, default 1e-5
            Torque tolerance for the two consecutive steps of the optimization.

        Returns
        -------
        optimized_directions : (I, 3) :numpy:`ndarray`
            Optimized direction of the spin vectors.
        """

        if directions_ig is None:
            directions_ig = np.random.uniform(low=-1, high=1, size=(self._I, 3))
            _logger.debug("Initial guess for the optimization is random (C1).")

        # Check the input correctness and normalize vectors.
        directions = _check_directions(self._I, directions_ig)

        hessian = self._hessian(directions)

        print(hessian)

        optimized_directions = _optimize(
            self,
            true_variables_0=directions,
            hessian_0=hessian,
            tolerance=np.array([energy_tolerance, torque_tolerance]),
            func=self._F,
            grad=self._grad_F,
            update=self._update,
            to_x=self._to_x,
            update_difference=self._update_difference,
        )

        return optimized_directions
