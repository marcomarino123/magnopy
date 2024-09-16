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
from os.path import abspath

from .hdf5 import *
from .txt import *

__all__ = ["load_spinham"]
__all__.extend(txt.__all__)
__all__.extend(hdf5.__all__)

_logger = logging.getLogger(__name__)


def load_spinham(filename, source_type=None, **kwargs):
    r"""
    Generalized interface function for the loading of the spin Hamiltonian.

    Parameters
    ----------
    filename : str
        Path to the filename that contains the information about the spin Hamiltonian.
        The source file can be any of the supported ones.
    source_type : str, optional
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
        ``source_type``.

    See Also
    --------
    io.load_tb2j
    io.load_spinham_txt
    io.load_spinham_hdf5
    """

    if source_type is not None:
        source_type = source_type.lower()
    else:
        _logger.info(
            f"Trying to read the Hamiltonian from the file {abspath(filename)}. "
            "No source_type is provided, guessing ..."
        )
        if filename.endswith(".txt"):
            _logger("Guessed text format of magnopy")
            source_type = "txt"
        elif filename.endswith("hdf5"):
            _logger("Guessed binary (.hdf5) format of magnopy")
            source_type = "hdf5"
        elif filename == "exchange.out":
            _logger("Guessed file coming from TB2J package")
            source_type = "tb2j"
        else:
            _logger.error("Can not guess the file source, please provide it manually.")
            raise RuntimeError()

    if source_type == "txt":
        return load_spinham_txt(filename, **kwargs)
    elif source_type == "hdf5":
        return load_spinham_hdf5(filename=filename, **kwargs)
    elif source_type == "tb2j":
        return load_tb2j(filename, **kwargs)
    else:
        _logger.error(
            f"The file source {source_type} is not supported. "
            'Supported types are "txt", "hdf5", "tb2j".'
        )
        raise RuntimeError()
