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

import logging
from typing import Iterable, Tuple

import numpy as np
from wulfric import TORADIANS, absolute_to_relative

from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.units.inside import ENERGY
from magnopy.units.si import BOHR_MAGNETON

_logger = logging.getLogger(__name__)

__all__ = ["Energy"]

# Convert to the internal units of energy
BOHR_MAGNETON /= ENERGY


def _update_x_ferro(x, search_direction, step=1):
    r"""
    Update the variables for the next step in the ferro case.

    Parameters
    ----------
    x : (I, 3) :numpy:`ndarray`
        Orientation of the spin vectors.
    search_direction : (I*3,) :numpy:`ndarray`
        Search direction computed in L-BFGS step
    step : float
        Size of the step along the search direction.
    """
    x = x.copy()
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

        x[i] = (
            np.cos(theta) * x[i]
            + np.sin(theta) * np.cross(r, x[i])
            + (1 - np.cos(theta)) * r * (r @ x[i])
        )

    return x


def _update_x_spiral(x, search_direction, step=1):
    r"""
    Update the variables for the next step in the ferro case.

    Parameters
    ----------
    x : list of two elements: (I+1, 3) :numpy:`ndarray` and (3,) :numpy:`ndarray`
        First element:
            * 0 - I-1:  Orientation of the spin vectors
            * I: cone axis
        Second element: spiral vector
    search_direction : (I*3+6,) :numpy:`ndarray`
        Search direction computed in L-BFGS step
    step : float
        Size of the step along the search direction.
    """
    x_0 = x[0].copy()
    x_1 = x[1].copy()
    a12 = search_direction[:-3:3] * step
    a13 = search_direction[1:-3:3] * step
    a23 = search_direction[2:-3:3] * step

    thetas = np.sqrt(a12**2 + a13**2 + a23**2)

    r = []
    for i in range(len(thetas)):
        theta = thetas[i]

        if theta < np.finfo(float).eps:
            continue

        r = (np.array([-a23[i], a13[i], -a12[i]])) / theta

        x_0[i] = (
            np.cos(theta) * x_0[i]
            + np.sin(theta) * np.cross(r, x_0[i])
            + (1 - np.cos(theta)) * r * (r @ x_0[i])
        )

    x_1 += search_direction[-3:] * step

    return [x_0, x_1]


def _unpack_ferro(x):
    r"""
    Unpack the coordinate for the feromagnetic case

    Parameters
    ----------
    x : (I, 3) :numpy:`ndarray`
        Orientation of the spin vectors.

    Returns
    -------
    spin_orientation : (I, 3) :numpy:`ndarray`
        Orientation of the spin vectors.
    """
    return (x,)


def _unpack_spiral(x):
    r"""
    Unpack parameters for the spiral case.

    Parameters
    ----------
    x : list of two elements: (I+1, 3) :numpy:`ndarray` and (3,) :numpy:`ndarray`
        First element:
            * 0 - I-1:  Orientation of the spin vectors
            * I: cone axis
        Second element: spiral vector

    Returns
    -------
    spin_orientation : (I, 3) :numpy:`ndarray`
        Orientation of the spin vectors.
    cone_axis : (3,)
        Cone axis.
    spiral_vector : (3,)
        Spiral vector.
    """
    return (x[0][:-1], x[0][-1], x[1])


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
            d = spinham.get_vector(atom1, atom2, R)
            self._bonds.append([i, j, d, J])

        # Return original noatation of SpinHamiltonian
        spinham.double_counting = previous_dc

        # Minimisation settings, exposed to public as properties
        self._m = 10

        # Parameters for Wolfe conditions
        self._wolfe_iter_max = 10000
        self._wolfe_c1 = 1e-4
        self._wolfe_c2 = 0.9

        # Minimisation settings, private
        # Gradient size depends on the expected ground state: 3*I for Ferromagnetic, FIXME
        self._gradient_size = None  # Have to be initialized at the beginning of every optimization function

        # External physical conditions
        self._magnetic_field = None

        # To be sorted
        self._d_vec = None  # Have to be initialised at the begining of every optimization function
        self._y_vec = None  # Have to be initialised at the begining of every optimization function
        self._rho = np.zeros((self._m), dtype=float)
        self._gamma = np.zeros((self._m), dtype=float)

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
            new_m = int(new_value)
        except:
            raise ValueError(
                "New size of memory storage for L-BFGS is not "
                f"an integer:{new_value}."
            )
        self._m = new_m

    @property
    def wolfe_c1(self) -> float:
        r"""
        Parameter for the Wolfe conditions:

        .. math::
          f(\boldsymbol{x} + \lambda\boldsymbol{p})
          \le
          f(\boldsymbol{x})
          +
          c_1  \lambda \nabla_{\boldsymbol{x}}f(\boldsymbol{x}) \cdot \boldsymbol{p}

        Default value is :math:`10^{-4}`

        Returns
        -------
        c1 : float
        """

        return self._wolfe_c1

    @wolfe_c1.setter
    def wolfe_c1(self, new_value):
        try:
            new_c1 = float(new_value)
        except:
            raise ValueError(
                "New c1 coefficient for Wolfe conditions is not "
                f"a float:{new_value}."
            )
        self._wolfe_c1 = new_c1

    @property
    def wolfe_c2(self) -> float:
        r"""
        Parameter for the Wolfe conditions:


        .. math::
          -\nabla_{\boldsymbol{x}}f(\boldsymbol{x} + \lambda\boldsymbol{p}) \cdot \boldsymbol{p}
          \le
          -c_2
          \nabla_{\boldsymbol{x}}f(\boldsymbol{x}) \cdot \boldsymbol{p}

        Default value is :math:`0.9`

        Returns
        -------
        c2 : float
        """

        return self._wolfe_c1

    @wolfe_c2.setter
    def wolfe_c2(self, new_value):
        try:
            new_c2 = float(new_value)
        except:
            raise ValueError(
                "New c2 coefficient for Wolfe conditions is not "
                f"a float:{new_value}."
            )
        self._wolfe_c2 = new_c2

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
                new_field = np.array(new_value, dtype=float)
            except:
                raise ValueError(f"New magnetic field is not array-like: {new_value}")

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
            gradient_vector = np.zeros((self._gradient_size), dtype=float)
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

    def _spiral_grad(
        self,
        x,
        spiral_vector,
        gradient_vector=None,
        torques=None,
    ):
        if gradient_vector is None:
            gradient_vector = np.zeros((self._gradient_size), dtype=float)
        if torques is None:
            torques = np.zeros((len(self._spins) + 1, 3), dtype=float)

        # Compute torques for spin_orientations and cone_axis
        for i in range(len(x)):
            h = 1e-4
            gradient = []
            for j in range(3):
                x[i][j] -= h
                f_minus_h = self.spiral(
                    x[:-1], cone_axis=x[-1], spiral_vector=spiral_vector
                )
                x[i][j] += 2 * h
                f_plus_h = self.spiral(
                    x[:-1], cone_axis=x[-1], spiral_vector=spiral_vector
                )
                gradient.append((f_plus_h - f_minus_h) / 2 / h)
                x[i][j] -= h

            t = np.cross(x[i], gradient)
            for j in range(0, 3):
                torques[i][j] = t[j]
            gradient_vector[3 * i] = t[2]
            gradient_vector[3 * i + 1] = -t[1]
            gradient_vector[3 * i + 2] = t[0]

        # Compute gradient for spiral_vector
        cone_axis = x[-1]
        K = np.array(
            [
                [0, -cone_axis[2], cone_axis[1]],
                [cone_axis[2], 0, -cone_axis[0]],
                [-cone_axis[1], cone_axis[0], 0],
            ]
        )
        K_sq = K @ K

        gradient = np.zeros(3, dtype=float)

        # Compute gradient ove spiral vector
        for i, j, d, J in self._bonds:
            C = np.cos(spiral_vector @ d) / 2 * (
                K @ J.matrix @ K_sq - K_sq @ J.matrix @ K
            ) - np.sin(spiral_vector @ d) / 2 * (
                K @ J.matrix @ K + K_sq @ J.matrix @ K_sq
            )
            gradient += d * (
                self._factor
                * self._spins[i]
                * self._spins[j]
                * np.einsum("i,ij,j", x[:-1][i], C, x[:-1][j])
            )

        gradient_vector[-3:] = gradient

        return gradient_vector, torques

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
            The vectors are normalized to one, i.e. only direction of the vectors
            is important.

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

        for i in range(len(spin_orientation)):
            spin_orientation[i] /= np.linalg.norm(spin_orientation[i])

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

    def spiral(self, spin_orientation, cone_axis, spiral_vector):
        r"""
        Computes energy of the spiral cone state for given
        ``spin_orientation``, ``cone_axis`` and ``spiral_vector``.

        Parameters
        ----------
        spin_orientation : (I, 3) or (3,) |array-like|_
            Orientation of the spin vectors.
            If ``I = 1``, then both ``(1,3)`` and ``(3,)`` shaped inputs are accepted.
            The vectors are normalized to one, i.e. only direction of the vectors
            is important.
        cone_axis : (3,) |array-like|_
            Orientation of the cone axis, only the direction is important.
        spiral_vector : (3,) |array-like|_
            Spiral vector.

        Returns
        -------
        energy :  float.
            Energy of the Hamiltonian for the given ``spin_orientation``, ``cone_axis``
            and ``spiral_vector``.
        """

        # Check that the input is correct (spins)
        try:
            spin_orientation = np.array(spin_orientation, dtype=float)
        except:
            raise ValueError(f"spin_orientation is not array-like: {spin_orientation}")

        if spin_orientation.shape[-1] != 3:
            raise ValueError(
                f"spin_orientation has to have the last dimension of "
                f"size 3, got {spin_orientation.shape[-1]}"
            )

        # Check that the input is correct (cone_axis)
        try:
            cone_axis = np.array(cone_axis, dtype=float)
        except:
            raise ValueError(f"cone_axis is not array-like: {cone_axis}")

        if cone_axis.shape != (3,):
            raise ValueError(
                f"cone_axis must have the shape of (3,) " f"got {cone_axis.shape}"
            )

        # Check that the input is correct (spiral vector)
        try:
            spiral_vector = np.array(spiral_vector, dtype=float)
        except:
            raise ValueError(f"spiral_vector is not array-like: {spiral_vector}")

        if spiral_vector.shape != (3,):
            raise ValueError(
                f"spiral_vector must have the shape of (3,) "
                f"got {spiral_vector.shape}"
            )

        # Make the input array have (I,3) shape for I = 1
        if len(self._spins) == 1 and spin_orientation.shape == (3,):
            spin_orientation = np.array([spin_orientation])

        if len(self._spins) != spin_orientation.shape[0]:
            raise ValueError(
                f"Expected {len(self._spins)} spin orientations, "
                f"got {spin_orientation.shape[0]}"
            )

        # Normalize spin orientations
        for i in range(len(spin_orientation)):
            spin_orientation[i] /= np.linalg.norm(spin_orientation[i])

        # Normalize cone axis
        cone_axis /= np.linalg.norm(cone_axis)

        K = np.array(
            [
                [0, -cone_axis[2], cone_axis[1]],
                [cone_axis[2], 0, -cone_axis[0]],
                [-cone_axis[1], cone_axis[0], 0],
            ]
        )
        K_sq = K @ K
        IK_sq = np.eye(3, dtype=float) + K_sq

        energy = 0

        # Compute exchange and single-ion-like anisotropy energy
        for i, j, d, J in self._bonds:
            C_dij = (
                IK_sq @ J.matrix @ IK_sq
                + (K @ J.matrix @ K + K_sq @ J.matrix @ K_sq)
                / 2
                * np.cos(spiral_vector @ d)
                + (K @ J.matrix @ K_sq - K_sq @ J.matrix @ K)
                / 2
                * np.sin(spiral_vector @ d)
            )
            energy += (
                self._factor
                * self._spins[i]
                * self._spins[j]
                * np.einsum("i,ij,j", spin_orientation[i], C_dij, spin_orientation[j])
            )

        # Compute zeeman energy
        if self.magnetic_field is not None:
            so_prime = np.einsum(
                "jk,ik ->ij", (np.eye(3, dtype=float) + K), spin_orientation
            )
            energy += BOHR_MAGNETON * np.einsum(
                "i,j,ij", self._g_factors, self.magnetic_field, so_prime
            )

        return energy

    ################################################################################
    #                             Optimization routines                            #
    ################################################################################

    def optimize_ferro(
        self,
        initial_guess=None,
        tol_torque=1e-5,
        tol_energy=1e-5,
        max_iterations=None,
        save_history=False,
        history_processor=None,
        history_step=1000,
    ):
        r"""
        Find minima of the energy assuming generalized ferromagnetic alignment.

        Parameters
        ----------
        initial_guess : (I, 3) or (3,) |array-like|_, optional
            Initial guess for the orientation of spin vectors.
            If none provided, then random initial guess is chosen.
            The vectors are normalized to one, i.e. only direction of the vectors
            is important.
            If ``I = 1``, then both ``(1,3)`` and ``(3,)`` shaped inputs are accepted.
        tol_torque : float, default 1e-5
            Tolerance for the root mean square value of torques of each spin.
            Given in the units of energy.
        tol_energy : float, default 1e-5
            Tolerance for the energy difference between the two consecutive minimization
            steps.
        max_iterations : int, optional
            Maximum amount of iterations for the minimization algorithm.
            By default the algorithm will run until the convergence is reached.
        save_history : bool, default False
            Whether to output the steps of the minimization algorithm.
        history_processor : function, optional
            Function for the history processing. If none provided, then history
            is directed to ``sys.stdout`` via ``print()`` with one line per iteration
            with each line in the following format:

            .. code-block:: text

                Energy torque_rms spin_1_x spin_1_y spin_2_z spin_2_x ...

            The call signature for ``history_processor`` is:

            .. code-block:: python

                history_processor(history)

            where ``history`` is a list with each element being a list:

            .. code-block:: python

                [energy, torque_rms, spin_orientation]

            where ``energy`` and ``torque_rms`` are ``float`` and
            ``spin_orientation.shape = (I,3)``.

        history_step : int, default 100
            amount of step to be outputted at once.

        Returns
        -------
        spin_orientation : (I, 3) :numpy:`ndarray`
            Spin orientation that corresponds to the found local minima of energy
            assuming generalized ferromagnetic state.
        """

        # Construct or check initial guess
        if initial_guess is None:
            spin_orientation = np.random.random((len(self._spins), 3))
        else:
            # Check that the input is correct
            try:
                spin_orientation = np.array(initial_guess, dtype=float)
            except:
                raise ValueError(f"initial guess is not array-like: {spin_orientation}")

            if spin_orientation.shape[-1] != 3:
                raise ValueError(
                    f"initial guess has to have the last dimension of "
                    f"size 3, got {spin_orientation.shape[-1]}"
                )

            # Make the input array have (I,3) shape for I = 1
            if len(self._spins) == 1 and spin_orientation.shape == (3,):
                spin_orientation = np.array([spin_orientation])

            if len(self._spins) != spin_orientation.shape[0]:
                raise ValueError(
                    f"Expected {len(self._spins)} spins in initial guess, "
                    f"got {spin_orientation.shape[0]}"
                )

        for i in range(len(spin_orientation)):
            spin_orientation[i] /= np.linalg.norm(spin_orientation[i])

        torque_max = 2 * tol_torque
        energy_diff = 2 * tol_energy
        # Note: iteration counter and k are distinct: k might be set to zero during
        # the algorithm's run.
        k = 0
        iteration_counter = 0

        #
        step_lambda = None
        previous_gradient_vector = None
        previous_search_direction = None
        energy_prev = self.ferro(spin_orientation)

        #
        self._gradient_size = 3 * len(self._spins)
        self._d_vec = np.zeros((self._m, self._gradient_size), dtype=float)
        self._y_vec = np.zeros((self._m, self._gradient_size), dtype=float)

        torques = np.zeros((len(self._spins), 3), dtype=float)
        gradient_vector = np.zeros((self._gradient_size), dtype=float)
        search_direction = np.zeros((self._gradient_size), dtype=float)

        if save_history:
            history = [[energy_prev, torque_max, spin_orientation]]

        while torque_max > tol_torque or abs(energy_diff) > tol_energy:
            if max_iterations is not None and iteration_counter >= max_iterations:
                _logger.warning(
                    f"Maximum iteration is reached. "
                    f"Torque: {torque_max:.5e}, Energy difference: {energy_diff:.5e}."
                )
                return spin_orientation

            self._ferro_grad(
                spin_orientation=spin_orientation,
                gradient_vector=gradient_vector,
                torques=torques,
            )

            torque_max = np.linalg.norm(torques, axis=1).max()
            if torque_max < tol_torque:
                break

            k, search_direction = self._compute_search_direction(
                k,
                gradient_vector=gradient_vector,
                previous_lambda=step_lambda,
                previous_gradient_vector=previous_gradient_vector,
                previous_search_direction=previous_search_direction,
            )

            step_lambda = self._lambda(
                spin_orientation,
                search_direction,
                self.ferro,
                _unpack_ferro,
                _update_x_ferro,
                self._ferro_grad,
            )

            spin_orientation = _update_x_ferro(
                spin_orientation, search_direction, step_lambda
            )
            energy_current = self.ferro(spin_orientation)
            energy_diff = abs(energy_prev - energy_current)

            if save_history:
                if iteration_counter % history_step == 0 and iteration_counter > 0:
                    if history_processor is not None:
                        history_processor(history)
                    else:
                        for i in range(len(history)):
                            history[
                                i
                            ] = f"{history[0]:.8e} {history[1]:.8e} " + " ".join(
                                [f"{a:.8f}" for a in spin_orientation.flatten()]
                            )
                        print("\n".join(history))

                    history = []

                history.append([energy_current, torque_max, spin_orientation])

            previous_gradient_vector = gradient_vector.copy()
            previous_search_direction = search_direction.copy()
            energy_prev = energy_current
            k += 1
            iteration_counter += 1

        # Output the remaining tail of history
        if save_history:
            if history_processor is not None:
                history_processor(history)
            else:
                for i in range(len(history)):
                    history[i] = f"{history[0]:.8e} {history[1]:.8e} " + " ".join(
                        [f"{a:.8f}" for a in spin_orientation.flatten()]
                    )
                print("\n".join(history))

        return spin_orientation

    def optimize_antiferro(self):
        raise NotImplementedError

    def optimize_spiral(
        self,
        initial_guess_spins=None,
        initial_guess_spiral_vector=None,
        initial_guess_cone_axis=None,
        tol_torque_spins=1e-5,
        tol_torque_cone_axis=1e-5,
        tol_energy=1e-5,
        max_iterations=None,
        save_history=False,
        history_processor=None,
        history_step=1000,
    ):
        r"""
        Find minima of the energy assuming generalized spiral cone alignment.

        Parameters
        ----------
        initial_guess_spins : (I, 3) or (3,) |array-like|_, optional
            Initial guess for the orientation of spin vectors.
            If none provided, then random initial guess is chosen.
            The vectors are normalized to one, i.e. only direction of the vectors
            is important.
            If ``I = 1``, then both ``(1,3)`` and ``(3,)`` shaped inputs are accepted.
        initial_guess_spiral_vector : (3,) |array-like|_, optional
            Initial guess for the spiral vector. If none provided then random value is
            chosen.
        initial_guess_cone_axis : (3,) |array-like|_, optional
            Initial guess for the cone axis. If none provided, then the random value is
            chosen. Normalised to the unit length, i.e. only the orientation of the
            vector is important.
        tol_torque_spins : float, default 1e-5
            Tolerance for the root mean square value of torques of each spin.
            Given in the units of energy.
        tol_torque_cone_axis : float, default 1e-5
            Tolerance for the artificial torque on the cone axis.
            Given in the units of energy.
        tol_energy : float, default 1e-5
            Tolerance for the energy difference between the two consecutive minimization
            steps.
        max_iterations : int, optional
            Maximum amount of iterations for the minimization algorithm.
            By default the algorithm will run until the convergence is reached.
        save_history : bool, default False
            Whether to output the steps of the minimization algorithm.
        history_processor : function, optional
            Function for the history processing. If none provided, then history
            is directed to ``sys.stdout`` via ``print()`` with one line per iteration
            with each line in the following format:

            .. code-block:: text

                Energy torque_rms torque_cone_axis n_x n_y n_z q_x q_y q_z spin_1_x spin_1_y spin_2_z spin_2_x ...

            The call signature for ``history_processor`` is:

            .. code-block:: python

                history_processor(history)

            where ``history`` is a list with each element being a list:

            .. code-block:: python

                [energy, torque_rms, torque_cone_axis, cone_axis, spiral_vector, spin_orientation]

            where ``energy``, ``torque_rms`` and ``torque_cone_axis`` are ``float`` and
            ``spin_orientation.shape = (I,3)``.

        history_step : int, default 100
            amount of step to be outputted at once.

        Returns
        -------
        spin_orientation : (I, 3) :numpy:`ndarray`
            Spin orientation that corresponds to the found local minima of energy
            assuming generalized ferromagnetic state.
        cone_axis : (3,) :numpy:`ndarray`
            Cone axis that corresponds to the found local minima of energy, assuming
            spiral cone state.
        spiral_vector : (3,) :numpy:`ndarray`
            Spiral vector that corresponds to the found local minima of energy, assuming
            spiral cone state.
        """
        # Construct or check initial guess for spins
        if initial_guess_spins is None:
            spin_orientation = np.random.random((len(self._spins), 3))
        else:
            # Check that the input is correct
            try:
                spin_orientation = np.array(initial_guess_spins, dtype=float)
            except:
                raise ValueError(f"initial guess is not array-like: {spin_orientation}")

            if spin_orientation.shape[-1] != 3:
                raise ValueError(
                    f"initial guess has to have the last dimension of "
                    f"size 3, got {spin_orientation.shape[-1]}"
                )

            # Make the input array have (I,3) shape for I = 1
            if len(self._spins) == 1 and spin_orientation.shape == (3,):
                spin_orientation = np.array([spin_orientation])

            if len(self._spins) != spin_orientation.shape[0]:
                raise ValueError(
                    f"Expected {len(self._spins)} spins in initial guess, "
                    f"got {spin_orientation.shape[0]}"
                )

        # Construct or check initial guess for spiral vector
        if initial_guess_spiral_vector is None:
            spiral_vector = np.random.random(3)
        else:
            # Check that the input is correct
            try:
                spiral_vector = np.array(initial_guess_spiral_vector, dtype=float)
            except:
                raise ValueError(
                    f"Initial guess for spiral vector is not array-like: "
                    f"{initial_guess_spiral_vector}"
                )
            if spiral_vector.shape != (3,):
                raise ValueError(
                    f"Initial guess for spiral vector should have shape "
                    f"of (3,), got: {spiral_vector.shape}"
                )

        # Construct or check initial guess for cone axis
        if initial_guess_cone_axis is None:
            cone_axis = np.random.random(3)
        else:
            # Check that the input is correct
            try:
                cone_axis = np.array(initial_guess_cone_axis, dtype=float)
            except:
                raise ValueError(
                    f"Initial guess for cone_axis is not array-like: "
                    f"{initial_guess_cone_axis}"
                )
            if cone_axis.shape != (3,):
                raise ValueError(
                    f"Initial guess for cone_axis should have shape "
                    f"of (3,), got: {cone_axis.shape}"
                )

        # Normalize spin orientations
        for i in range(len(spin_orientation)):
            spin_orientation[i] /= np.linalg.norm(spin_orientation[i])

        # Normalize cone axis:
        cone_axis /= np.linalg.norm(cone_axis)

        # Merge spin orientation and cone axis into one variable
        x = np.concatenate((spin_orientation, [cone_axis]), axis=0)

        # Set initial maximum torque and energy difference
        torque_spins_max = 2 * tol_torque_spins
        torque_cone_axis_max = 2 * tol_torque_cone_axis
        energy_diff = 2 * tol_energy

        # Note: iteration counter and k are distinct: k might be set to zero during
        # the algorithm's run.
        k = 0
        iteration_counter = 0

        #
        step_lambda = None
        previous_gradient_vector = None
        previous_search_direction = None
        energy_prev = self.spiral(x[:-1], x[-1], spiral_vector)

        #
        self._gradient_size = 3 * len(self._spins) + 6
        self._d_vec = np.zeros((self._m, self._gradient_size), dtype=float)
        self._y_vec = np.zeros((self._m, self._gradient_size), dtype=float)

        torques = np.zeros((len(self._spins) + 1, 3), dtype=float)
        gradient_vector = np.zeros((self._gradient_size), dtype=float)
        search_direction = np.zeros((self._gradient_size), dtype=float)

        if save_history:
            history = [
                [
                    energy_prev,
                    torque_spins_max,
                    torque_cone_axis_max,
                    x[-1],
                    spiral_vector,
                    x[:-1],
                ]
            ]

        while (
            torque_spins_max > tol_torque_spins
            or torque_cone_axis_max > tol_torque_cone_axis
            or abs(energy_diff) > tol_energy
        ):
            if max_iterations is not None and iteration_counter >= max_iterations:
                _logger.warning(
                    f"Maximum iteration is reached. "
                    f"Torque: {torque_spins_max:.5e}, "
                    f"Cone torque: {torque_cone_axis_max}, "
                    f"Energy difference: {energy_diff:.5e}."
                )
                return x[:-1], x[-1], spiral_vector

            self._spiral_grad(
                x=x,
                spiral_vector=spiral_vector,
                gradient_vector=gradient_vector,
                torques=torques,
            )

            torque_spins_max = np.linalg.norm(torques[:-1], axis=1).max()
            torque_cone_axis_max = np.linalg.norm(torques[-1])

            k, search_direction = self._compute_search_direction(
                k,
                gradient_vector=gradient_vector,
                previous_lambda=step_lambda,
                previous_gradient_vector=previous_gradient_vector,
                previous_search_direction=previous_search_direction,
            )

            step_lambda = self._lambda(
                [x, spiral_vector],
                search_direction,
                self.spiral,
                _unpack_spiral,
                _update_x_spiral,
                self._spiral_grad,
            )

            x, spiral_vector = _update_x_spiral(
                [x, spiral_vector], search_direction, step_lambda
            )
            energy_current = self.spiral(x[:-1], x[-1], spiral_vector)
            energy_diff = abs(energy_prev - energy_current)

            if save_history:
                if iteration_counter % history_step == 0 and iteration_counter > 0:
                    if history_processor is not None:
                        history_processor(history)
                    else:
                        for i in range(len(history)):
                            history[i] = (
                                f"{history[0]:.8e} {history[1]:.8e} "
                                + " ".join([f"{a:.8f}" for a in x[-1]])
                                + " ".join([f"{a:.8f}" for a in spiral_vector])
                                + " ".join([f"{a:.8f}" for a in x[:-1].flatten()])
                            )
                        print("\n".join(history))

                    history = []

                history.append(
                    [
                        energy_current,
                        torque_spins_max,
                        torque_cone_axis_max,
                        x[-1],
                        spiral_vector,
                        x[:-1],
                    ]
                )

            previous_gradient_vector = gradient_vector.copy()
            previous_search_direction = search_direction.copy()
            energy_prev = energy_current
            k += 1
            iteration_counter += 1

        # Output the remaining tail of history
        if save_history:
            if history_processor is not None:
                history_processor(history)
            else:
                for i in range(len(history)):
                    history[i] = (
                        f"{history[0]:.8e} {history[1]:.8e} "
                        + " ".join([f"{a:.8f}" for a in x[-1]])
                        + " ".join([f"{a:.8f}" for a in spiral_vector])
                        + " ".join([f"{a:.8f}" for a in x[:-1].flatten()])
                    )
                print("\n".join(history))

        return x[:-1], x[-1], spiral_vector

    ################################################################################
    #                                 L-BFGS update                                #
    ################################################################################
    def _compute_search_direction(
        self,
        k,
        gradient_vector,
        previous_lambda=None,
        previous_gradient_vector=None,
        previous_search_direction=None,
    ):
        r"""
        Compute search direction with L-BFGS algorithm.
        Universal and does not depend on the choice of the ground state type.

        Parameters
        ----------
        k : int
            Index of the minimization cycle.
        gradient_vector : (M,) :numpy:`ndarray`
            Gradient vector.
        previous_gradient_vector : (M,) :numpy:`ndarray`
            Gradient vector for k-1.
        previous_search_direction : (M,) :numpy:`ndarray`
            Search direction for k-1.

        Returns
        -------
        k : int
            Index of the minimization cycle (can be set to 0 at some of the steps).
        search_direction : (M,)
            Search direction computed for the step k.
        """

        if k != 0 and (
            previous_gradient_vector is None
            or previous_search_direction is None
            or previous_lambda is None
        ):
            raise ValueError("Need info about previous gradient and search direction")

        n = k % self._m

        if k == 0:
            self._d_vec = np.zeros((self._m, self._gradient_size), dtype=float)
            self._y_vec = np.zeros((self._m, self._gradient_size), dtype=float)
            self._rho = np.zeros((self._m), dtype=float)
            self._gamma = np.zeros((self._m), dtype=float)
            search_direction = gradient_vector
        else:
            self._d_vec[n] = previous_lambda * previous_search_direction
            self._y_vec[n] = gradient_vector - previous_gradient_vector
            self._rho[n] = 1 / (self._d_vec[n] @ self._y_vec[n])

            if self._rho[n] < 0:
                return (
                    0,
                    self._compute_search_direction(0, gradient_vector=gradient_vector)[
                        1
                    ],
                )

            q = gradient_vector.copy()

            for l in range(self._m - 1, -1):
                j = (l + n + 1) % self._m
                self._gamma[j] = self._rho[j] * (self._d_vec[j] @ q)
                q = q - self._gamma[j] * self._y_vec[j]
            search_direction = q / self._rho[n] / (np.linalg.norm(self._y_vec[n]))
            for l in range(0, self._m):
                if k < self._m:
                    j = l
                else:
                    j = (l + n + 1) % self._m
                search_direction = search_direction + self._d_vec[j] * (
                    self._gamma[j] - self._rho[j] * (self._y_vec[j] @ search_direction)
                )

        return k, search_direction

    ################################################################################
    #                   Inexact line search with Wolfe conditions                  #
    ################################################################################
    def _lambda(self, x, search_direction, energy, _unpack, _update, _grad):
        a = 1
        fx = energy(*_unpack(x))
        x_new = _update(x, search_direction, a)
        nabla_new = _grad(*_unpack(x_new))[0]
        nabla = _grad(*_unpack(x))[0]
        i = 0
        while (
            energy(*_unpack(x_new))
            >= fx + (self._wolfe_c1 * a * nabla.T @ search_direction)
            or nabla_new.T @ search_direction
            <= self._wolfe_c2 * nabla.T @ search_direction
        ):
            a *= 0.5
            x_new = x_new = _update(x, search_direction, a)
            nabla_new = _grad(*_unpack(x_new))[0]
            if i > self._wolfe_iter_max:
                return 1
                raise ValueError("Wolfe failed")
            i += 1
        return a


if __name__ == "__main__":
    from magnopy.io import load_spinham_txt

    spinham = load_spinham_txt(
        "/Users/rybakov.ad/Codes/magnopy/tmp/test/NiI2_varcell.txt"
    )
    nspins = 1
    # spinham = load_spinham_txt(
    #     "/Users/rybakov.ad/Codes/magnopy/tmp/crsbr-mono-grogu.txt"
    # )
    energy = Energy(spinham)
    # energy.magnetic_field = np.array([1, 0, 15])

    so_history = []
    targets = [[], []]

    # [[-2.92957708e-03  7.04724282e-07  9.99995709e-01]
    #  [ 2.93832550e-03  6.61310474e-07  9.99995683e-01]
    #  [ 4.42293934e-06  6.93626006e-07  1.00000000e+00]]

    #  [[-2.92949381e-03  6.65588520e-07  9.99995709e-01]
    #   [ 2.93840879e-03  6.22181286e-07  9.99995683e-01]
    #   [ 4.49872399e-06  6.57908504e-07  1.00000000e+00]]

    #  [[-2.92955988e-03  7.67294960e-07  9.99995709e-01]
    #   [ 2.93834271e-03  7.23901523e-07  9.99995683e-01]
    #   [ 4.43961966e-06  7.59410312e-07  1.00000000e+00]]

    def hprint(history):
        for line in history:
            print(f"{line[0]:.8f}", f"{line[1]:.8f}", end=" ")

            for so in line[2]:
                print(" ".join([f"{a:.5f}" for a in so]), end=" ")

            so_history.append(line[2])
            targets[0].append(line[0])
            targets[1].append(line[1])
            print()
        print("", end="", flush=True)

    result = energy.optimize_spiral(
        save_history=True,
        history_step=10,
        history_processor=hprint,
        max_iterations=10000,
    )
    print("\n\n", result, "\n")

    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)

    data = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            tmp_spins = []
            for k in range(nspins):
                tmp_spins.append(
                    [
                        np.cos(phi[j]) * np.sin(theta[i]),
                        np.sin(phi[j]) * np.sin(theta[i]),
                        np.cos(theta[i]),
                    ]
                )
            data[i][j] = energy.ferro(tmp_spins)

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(2, 1)
    x = np.linspace(0, len(targets[0]) - 1, len(targets[0]))
    axs[0].plot(x, targets[0], color="black", lw=2)
    axs[1].plot(x, targets[1], color="black", lw=2)
    axs[0].set_xlabel("Iteration step", fontsize=20)
    axs[0].set_ylabel("Energy", fontsize=20)
    axs[1].set_xlabel("Iteration step", fontsize=20)
    axs[1].set_ylabel("Max torque", fontsize=20)
    plt.savefig("test-targets.png", dpi=300, bbox_inches="tight")
    plt.close()

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
    colors = ["tab:purple", "tab:green", "tab:orange"]
    norm = mpl.colors.Normalize(vmin=0, vmax=len(so_history) - 1)

    scattered = []
    for i in range(nspins):
        scattered.append([])
    print(np.array(so_history).shape)
    for i, sos in enumerate(so_history):
        for j in range(nspins):
            so = sos[j]

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
                scattered[j].append([phi, theta, i])

    scattered = np.array(scattered)
    phi = scattered[:, :, 0]
    theta = scattered[:, :, 1]
    i = scattered[:, :, 2]
    for j in range(nspins):
        ax.plot(phi[j], theta[j], zorder=10, color=colors[j], lw=1)
        ax.scatter(phi[j][-1], theta[j][-1], zorder=11, lw=0, s=20, color="black")

    plt.savefig("test.png", dpi=300, bbox_inches="tight")
    plt.close()
