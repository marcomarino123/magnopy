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


from magnopy.magnons._representations import PolynomialParameter, get_vector_parameter


def get_classical_energy(spinham, spin_directions, A=None, B=None) -> float:
    r"""
    Computes classical energy of the given spin configuration :math:`E_0`.

    Parameters
    ----------
    spinham : :py:class:`.spinham.SpinHamiltonian`
        Spin Hamiltonian.
    spin_directions : (M, 3) |array-like|_
        Directions of spin vectors. Only directions of vectors are used, modulus is
        ignored. Note that spin directions have to be given for all atoms even if they
        are not magnetic.
    A : (M) list of :py:class:`.PolynomialParameter`, optional
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`. If None given, then
        :math:`A^{00}_{\alpha} = 0` is assumed.
    B : (M) list of :py:class:`.PolynomialParameter`, optional
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`. If None given, then
        :math:`B^{00}_{\alpha} = 0` is assumed.

    Returns
    -------
    E : float
        Classical energy.
    """

    if A is None:
        A = [PolynomialParameter() for _ in range(len(spinham.atoms.spins))]
        for alpha in range(len(spinham.atoms.spins)):
            A[alpha][0, 0] = 0
    if B is None:
        B = [PolynomialParameter() for _ in range(len(spinham.atoms.spins))]
        for alpha in range(len(spinham.atoms.spins)):
            B[alpha][0, 0] = 0

    v = get_vector_parameter(
        A=A, B=B, spin_values=spinham.atoms.spins, spin_directions=spin_directions
    )

    v_00 = [v_alpha[0, 0] for v_alpha in v]

    if spinham.notation.spin_normalized:
        v_00 = [
            v_00[index] / spinham.atoms.spins[index]
            for index in range(len(spinham.atoms.spins))
        ]

    energy = 0

    # One spin & one site
    for atom, parameter in spinham.p1:
        energy += spinham.notation.c1 * parameter @ v_00[atom]

    # Two spins & one site
    for atom, parameter in spinham.p21:
        energy += spinham.notation.c21 * v_00[atom] @ parameter @ v_00[atom]

    # Two spins & two sites
    for atom1, atom2, _, parameter in spinham.p22:
        energy += spinham.notation.c22 * v_00[atom1] @ parameter @ v_00[atom2]

    # TODO four spin terms

    if abs(energy.imag) < 1e-8:
        return float(energy.real)
    return energy


def get_energy_correction_lswt(spinham, spin_directions, A, B) -> float:
    r"""
    Computes correction to the classical energy of the given spin configuration at the
    level of LSWT :math:`E_0^{(2)}`.

    Parameters
    ----------
    spinham : :py:class:`.spinham.SpinHamiltonian`
        Spin Hamiltonian.
    spin_directions : (M, 3) |array-like|_
        Directions of spin vectors. Only directions of vectors are used, modulus is
        ignored. Note that spin directions have to be given for all atoms even if they
        are not magnetic.
    A : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.

    Returns
    -------
    E : float
        Correction to the  classical energy.
    """

    v = get_vector_parameter(
        A=A, B=B, spin_values=spinham.atoms.spins, spin_directions=spin_directions
    )

    v_00 = [v_alpha[0, 0] for v_alpha in v]

    v_21 = [v_alpha[2, 1] for v_alpha in v]

    if spinham.notation.spin_normalized:
        v_00 = [
            v_00[index] / spinham.atoms.spins[index]
            for index in range(len(spinham.atoms.spins))
        ]
        v_21 = [
            v_21[index] / spinham.atoms.spins[index]
            for index in range(len(spinham.atoms.spins))
        ]

    energy = 0

    # One spin & one site
    for atom, parameter in spinham.p1:
        energy += -0.5 * spinham.notation.c1 * parameter @ v_00[atom]

    # Two spins & one site
    for atom, parameter in spinham.p21:
        energy += -1 * spinham.notation.c21 * v_00[atom] @ parameter @ v_00[atom]

    # Two spins & two sites
    for atom1, atom2, _, parameter in spinham.p22:
        energy += -1 * spinham.notation.c22 * v_00[atom1] @ parameter @ v_00[atom2]

    # TODO four spin terms

    if abs(energy.imag) < 1e-8:
        return float(energy.real)
    return energy
