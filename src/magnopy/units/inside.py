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

R"""
Here we define default units of Magnopy.
Input is supported in a variety of different unit, but it is converted to the internal ones as early as possible.

The constants are converted here for the future use as well.
If you are using the constants inside magnopy, then import them from here and not from
magnopy.units.si
"""

from magnopy.units import si

__all__ = [
    "LENGTH",
    "ENERGY",
    "TIME",
    "MAGNETIC_FIELD",
    "TEMPERATURE",
    "LENGTH_NAME",
    "ENERGY_NAME",
    "TIME_NAME",
    "MAGNETIC_FIELD_NAME",
    "TEMPERATURE_NAME",
    "TRUE_KEYWORDS",
    "FALSE_KEYWORDS",
]


################################################################################
#                                Unit's values                                 #
################################################################################
LENGTH = si.ANGSTROM
ENERGY = 1e-3 * si.ELECTRON_VOLT
TIME = si.SECOND
MAGNETIC_FIELD = si.TESLA
TEMPERATURE = si.KELVIN


################################################################################
#                                Unit's names                                  #
################################################################################
LENGTH_NAME = "Angstrom"
ENERGY_NAME = "milli-electron-Volt"
TIME_NAME = "Second"
MAGNETIC_FIELD_NAME = "Tesla"
TEMPERATURE_NAME = "Kelvin"

################################################################################
#                               Technical units                                #
################################################################################
TRUE_KEYWORDS = ["true", "t", "yes", "y", "1"]
FALSE_KEYWORDS = ["false", "f", "no", "n", "0"]
