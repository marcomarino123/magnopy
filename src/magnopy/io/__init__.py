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
from os.path import abspath

from .hdf5 import *
from .txt import *

__all__ = ["load_spinham"]
__all__.extend(txt.__all__)
__all__.extend(hdf5.__all__)

_logger = logging.getLogger(__name__)


def load_spinham(filename, spinham_format=None, **kwargs):
    r"""
    Generalized interface function for the loading of the spin Hamiltonian.

    Parameters
    ----------
    filename : str
        Path to the filename that contains the information about the spin Hamiltonian.
        The source file can be any of the supported ones.
        If ends with ".hdf5" -> read as binary. If ends with "exchange.out" -> read as
        |TB2J|_. Otherwise read as human-readable.
    spinham_format : str, optional
        Hint for the source of the file. If not provided, then the function tries to
        guess the type of the file and type of the source.
        Supported values:

        * "txt"

            For the human-readable format that is default for magnopy.

        * "hdf5"

            For the binary format that is default for magnopy.

        * "tb2j"

            If the Hamiltonian is obtained from the |TB2J|_ package.

        All keywords are case-insensitive.
    ** kwargs
        Optional keyword arguments, that are specific to the load function for each
        ``spinham_format``.

    See Also
    --------
    io.load_tb2j
    io.load_spinham_txt
    io.load_spinham_hdf5
    """

    if spinham_format is None:
        _logger.info("Format of spinham is not given, guessing ...")
        if filename.endswith(".hdf5"):
            spinham_format = "hdf5"
            _logger.info("Guessed binary (.hdf5) format of magnopy")
        elif filename.endswith("exchange.out"):
            spinham_format = "tb2j"
            _logger.info("Guessed file coming from TB2J package")
        else:
            spinham_format = "txt"
            _logger.info("Guessed text format of magnopy")
    else:
        spinham_format = spinham_format.lower()

    _logger.info(
        f"Trying to read the Hamiltonian from the file {abspath(filename)}. "
        f"Type of the file is {spinham_format}."
    )

    if spinham_format == "txt":
        return load_spinham_txt(filename, **kwargs)
    elif spinham_format == "hdf5":
        return load_spinham_hdf5(filename=filename, **kwargs)
    elif spinham_format == "tb2j":
        return load_tb2j(filename, **kwargs)
    else:
        message = (
            f"Unsupported spinham_format ({spinham_format}). "
            "Supported formats are: 'txt', 'hdf5', 'tb2j'."
        )
        _logger.error(message)
        raise ValueError(message)
