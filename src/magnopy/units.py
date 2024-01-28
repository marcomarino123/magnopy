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
    "BOHR",
    "ANGSTROM",
    "JOULE",
    "MILLI_ELECTRON_VOLT",
    "KELVIN",
    "ELECTRON_VOLT",
    "RYDBERG",
]

# Internal units are:
# - Angstrom for length
# - meV for parameters
# Bohr magneton for spins/magnetization

# In this module we list all other supported unit in terms of the internal ones.

# Length conversion
BOHR = 0.529177210903  # Angstrom
ANGSTROM = 1  # Angstrom

# Energy conversion
JOULE = 6.241509074e21  # meV
MILLI_ELECTRON_VOLT = 1  # meV
ELECTRON_VOLT = 1e3  # mev
KELVIN = 1 / 11.60451812  # meV
RYDBERG = 13605.693122994  # meV

# Case insensitive
TRUE_KEYWORDS = ["true", "t", "1", "yes", "y"]

# Case insensitive
FALSE_KEYWORDS = ["false", "f", "0", "no", "n"]
