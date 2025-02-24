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


__all__ = ["ColpaFailed", "NotationError", "FailedToVerifyTxtModelFile"]


class ColpaFailed(Exception):
    r"""
    Raised when Diagonalization via Colpa fails.
    """

    def __init__(self):
        message = "Diagonalization via Colpa failed."
        super().__init__(message)


class FailedToVerifyTxtModelFile(Exception):
    R"""
    Raise if the format of the model input file is invalid.
    """

    def __init__(self, message):
        super().__init__(message)


class NotationError(Exception):
    r"""
    Raised if notation or part of the notation of spin Hamiltonian is not defined.
    """

    def __init__(self, notation, property):
        message = (
            f"Notation of spin Hamiltonian has an undefined property '{property}':\n"
            + notation.summary(return_as_string=True)
        )
        super().__init__(message)
