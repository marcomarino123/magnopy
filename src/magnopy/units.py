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
    "LENGTH_UNITS",
    "LENGTH_UNITS_NAME",
    "ENERGY_UNITS",
    "ENERGY_UNITS_NAME",
    "MAGNETIC_FIELD_UNITS",
    "MAGNETIC_FIELD_UNITS_NAME",
    "BOHR",
    "ANGSTROM",
    "JOULE",
    "MILLI_ELECTRON_VOLT",
    "KELVIN",
    "ELECTRON_VOLT",
    "RYDBERG",
    "TESLA",
    "MU_BOHR",
    "MU_BOHR_UNITS_NAME",
    "K_BOLTZMANN",
    "K_BOLTZMANN_UNITS_NAME",
]
# TODO work accurately with units

# In this module we list all other supported unit in the units of International System of Units
################################################################################
#                                    Units                                     #
################################################################################
########################################
#                Length                #
########################################
BOHR = 1 / 0.529177210903e-10  # Bohr / Meter
ANGSTROM = 1e10  # Angstrom / Meter
# Internal units
LENGTH_UNITS = ANGSTROM
LENGTH_UNITS_NAME = "Angstrom"

########################################
#                Energy                #
########################################
JOULE = 1  # Joule
ELECTRON_VOLT = 1.602176634e-19  # Joule
MILLI_ELECTRON_VOLT = ELECTRON_VOLT / 1000  # Joule
RYDBERG = 13.605693122994 * ELECTRON_VOLT  # Joule
# Internal units
ENERGY_UNITS = MILLI_ELECTRON_VOLT
ENERGY_UNITS_NAME = "meV"

########################################
#              Temperature             #
########################################
KELVIN = 1  # Kelvin
# Internal units
TEMPERATURE_UNITS = KELVIN
TEMPERATURE_UNITS_NAME = KELVIN


########################################
#            Magnetic field            #
########################################
TESLA = 1.0  # Tesla
# Internal units
MAGNETIC_FIELD_UNITS = TESLA
MAGNETIC_FIELD_UNITS_NAME = "Tesla"

################################################################################
#                                  Constants                                   #
################################################################################

########################################
#           Boolean keywords           #
########################################
# Case insensitive
_TRUE_KEYWORDS = ["true", "t", "1", "yes", "y"]

# Case insensitive
_FALSE_KEYWORDS = ["false", "f", "0", "no", "n"]

########################################
#             Bohr magneton            #
########################################
MU_BOHR = 9.2740100783e-24  # Joule / Tesla
# Convert to internal units
MU_BOHR /= ENERGY_UNITS / MAGNETIC_FIELD_UNITS  # meV/Tesla
MU_BOHR_UNITS_NAME = f"{ENERGY_UNITS_NAME}/{MAGNETIC_FIELD_UNITS_NAME}"

########################################
#          Boltzmann constant          #
########################################
K_BOLTZMANN = 1.380649e-23  # Joule / Kelvin
# Convert to internal units
K_BOLTZMANN /= ENERGY_UNITS / KELVIN
K_BOLTZMANN_UNITS_NAME = f"{ENERGY_UNITS_NAME}/{TEMPERATURE_UNITS_NAME}"
