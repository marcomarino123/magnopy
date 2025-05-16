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


import numpy as np
from wulfric.geometry import absolute_to_relative

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def output_omegas(
    omegas,
    output_filename=None,
    kpoints=None,
    relative=False,
    rcell=None,
    digits=4,
    scientific_notation=True,
):
    r"""
    Outputs a list of omegas.

    Parameters
    ----------
    omegas : (N, M) |array-like|_
        Array of omegas, first index of an array runs over N (:math:`\le 1`) kpoints,
        second index of an array runs over M modes.
    output_filename : str, optional
        Name of the file for saving the omegas. If ``None``, then the result is returned
        as a string.
    kpoints : (N, 3) |array-like|_
        List of the kpoints. ``kpoints[i]`` correspond to the ``omegas[i]`` modes.
    relative : bool, default False
        If ``relative == True``, then ``kpoints`` are interpreted as given relative to
        the reciprocal unit cell. Otherwise it is interpreted as given in absolute
        coordinates.
    rcell : (3, 3) |array-like|_
        Reiprocal unit cell. Rows are interpreted as vectors, columns as Cartesian
        coordinates.
    digits : int, default 4
        Number of digits after the comma for the omegas.
    scientific_notation : bool, default True
        Whether to use scientific notation for the omegas.

    Returns
    -------
    lines : str
        Only returned if ``output_filename is None``. Use ``print("\n".join(lines))``
        to output the results to the standard output stream.

    Notes
    -----
    By default kpoints are interpreted as given in absolute coordinates in the
    reciprocal space.

    .. doctest::

        >>> import magnopy.io as mio
        >>> omegas = [[1, 2], [1.2, 2.3]]
        >>> kpoints = [[0, 0, 0], [0.1, 0.2, 0.3]]
        >>> lines = mio.output_omegas(omegas=omegas, kpoints=kpoints)
        >>> print("\n".join(lines))
        #         mode 1         mode 2          k_x          k_y          k_z
              1.0000e+00     2.0000e+00   0.00000000   0.00000000   0.00000000
              1.2000e+00     2.3000e+00   0.10000000   0.20000000   0.30000000

    One can tell it to interpret the kpoints as given in relative coordinates to some
    reciprocal cell

    .. doctest::

        >>> lines = mio.output_omegas(omegas=omegas, kpoints=kpoints, relative=True)
        >>> print("\n".join(lines))
        #         mode 1         mode 2         k_b1         k_b2         k_b3
              1.0000e+00     2.0000e+00   0.00000000   0.00000000   0.00000000
              1.2000e+00     2.3000e+00   0.10000000   0.20000000   0.30000000

    If the reciprocal cell is provided, then the kpoints are converter either way and
    both are printed

    .. doctest::

        >>> lines = mio.output_omegas(omegas=omegas, kpoints=kpoints, relative=True, rcell=[[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        >>> print("\n".join(lines))
        #         mode 1         mode 2         k_b1         k_b2         k_b3          k_x          k_y          k_z
              1.0000e+00     2.0000e+00   0.00000000   0.00000000   0.00000000   0.00000000   0.00000000   0.00000000
              1.2000e+00     2.3000e+00   0.10000000   0.20000000   0.30000000   0.10000000   0.40000000   0.90000000
        >>> lines = mio.output_omegas(omegas=omegas, kpoints=kpoints, relative=False, rcell=[[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        >>> print("\n".join(lines))
        #         mode 1         mode 2         k_b1         k_b2         k_b3          k_x          k_y          k_z
              1.0000e+00     2.0000e+00   0.00000000   0.00000000   0.00000000   0.00000000   0.00000000   0.00000000
              1.2000e+00     2.3000e+00   0.10000000   0.10000000   0.10000000   0.10000000   0.20000000   0.30000000

    One can control the number of digits in omegas

    .. doctest::

        >>> lines = mio.output_omegas(omegas=omegas, kpoints=kpoints, digits=8)
        >>> print("\n".join(lines))
        #             mode 1             mode 2          k_x          k_y          k_z
              1.00000000e+00     2.00000000e+00   0.00000000   0.00000000   0.00000000
              1.20000000e+00     2.30000000e+00   0.10000000   0.20000000   0.30000000

    and whether the scientific notation should be used

    .. doctest::

        >>> lines = mio.output_omegas(omegas=omegas, kpoints=kpoints, scientific_notation=False)
        >>> print("\n".join(lines))
        #    mode 1    mode 2          k_x          k_y          k_z
            1.0000    2.0000   0.00000000   0.00000000   0.00000000
            1.2000    2.3000   0.10000000   0.20000000   0.30000000

    """

    # Prepare format for the omegas
    chars = digits + 1 + 1 + 3
    if scientific_notation:
        chars += 1 + 1 + 3

    chars = max(chars, 8)

    if scientific_notation:
        fmt = f">{chars}.{digits}e"
    else:
        fmt = f">{chars}.{digits}f"

    # Prepare the header
    header = ["#"]
    for alpha in range(len(omegas[0])):
        header.append(f"{f'mode {alpha+1}':>{chars}}")

    if kpoints is not None:
        if rcell is not None:
            header.append(
                " ".join([f"{f'k_{comp}':>12}" for comp in ["b1", "b2", "b3"]])
            )
            header.append(" ".join([f"{f'k_{comp}':>12}" for comp in "xyz"]))
        elif relative:
            header.append(
                " ".join([f"{f'k_{comp}':>12}" for comp in ["b1", "b2", "b3"]])
            )
        else:
            header.append(" ".join([f"{f'k_{comp}':>12}" for comp in "xyz"]))

    header = " ".join(header)

    # Output header
    if output_filename is not None:
        f = open(output_filename, "w")
        f.write(header + "\n")
    else:
        lines = [header]

    # Output omegas for each kpoint
    for i in range(len(omegas)):
        line = [" "]

        for mode in omegas[i]:
            line.append(f"{mode:{fmt}}")

        if kpoints is not None:
            if rcell is not None:
                if relative:
                    k_vec = kpoints[i] @ np.array(rcell)
                    line.append(
                        " ".join([f"{kpoints[i][comp]:12.8f}" for comp in range(3)])
                    )
                    line.append(" ".join([f"{k_vec[comp]:12.8f}" for comp in range(3)]))
                else:
                    k_vec_rel = absolute_to_relative(vector=kpoints[i], basis=rcell)
                    line.append(
                        " ".join([f"{k_vec_rel[comp]:12.8f}" for comp in range(3)])
                    )
                    line.append(
                        " ".join([f"{kpoints[i][comp]:12.8f}" for comp in range(3)])
                    )
            else:
                line.append(
                    " ".join([f"{kpoints[i][comp]:12.8f}" for comp in range(3)])
                )

        line = " ".join(line)
        if output_filename is not None:
            f.write(line + "\n")
        else:
            lines.append(line)

    if output_filename is not None:
        f.close()
    else:
        return lines


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
