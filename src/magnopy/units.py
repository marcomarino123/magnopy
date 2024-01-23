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

__all__ = [
    "BOHR_TO_ANGSTROM",
    "ANGSTROM_TO_BOHR",
    "JOULE_TO_meV",
    "meV_TO_JOULE",
    "K_TO_meV",
    "meV_TO_K",
    "Ry_TO_meV",
    "meV_TO_Ry",
]

BOHR_TO_ANGSTROM = 0.529177210903
ANGSTROM_TO_BOHR = 1 / BOHR_TO_ANGSTROM

JOULE_TO_meV = 6.241509074e21
meV_TO_JOULE = 1 / JOULE_TO_meV

meV_TO_K = 11.60451812
K_TO_meV = 1 / meV_TO_K

Ry_TO_meV = 13605.693122994
meV_TO_Ry = 1 / Ry_TO_meV
