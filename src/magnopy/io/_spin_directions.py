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

try:
    import plotly.graph_objects as go

    PLOTLY_AVAILABLE = True
    PLOTLY_ERROR_MESSAGE = (
        "If you see this message, please contact developers of the code."
    )
except ImportError:
    PLOTLY_AVAILABLE = False
    PLOTLY_ERROR_MESSAGE = (
        "In order to use spin projection plotter an installation of Plotly is \n"
        "required, please try to install it with the command\n\n  "
        "pip install plotly\n\nor\n\n  pip3 install plotly\n"
    )

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def read_spin_directions(filename: str):
    r"""
    Read directions of the spins from the file.

    Parameters
    ----------
    filename : str or (3*M, ) |array-like|_
        File with the spin directions. See notes for the specification of the file
        format.

    Returns
    -------
    spin_directions : (M, ) :numpy:`ndarray`
        If ``spin_directions`` is an |array-like|_, then first three elements are

    Notes
    -----
    The file is expected to contain three numbers per line, here is an example for two
    spins

    .. code-block:: text

        S1_x S1_y S1_z
        S2_x S2_y S2_z

    Only the direction of the spin vector is recognized, the modulus is ignored.
    Comments are allowed at any place of the file and preceded by the symbol "#".
    If the symbol "#" is found, the part of the line after it is ignored. Here
    are examples of valid use of the comments

    .. code-block:: text

        # Spin vectors for the material XX
        S1_x S1_y S1_z # Atom X1
        # This comments is here by some reason
        S2_x S2_y S2_z # Atom X2

    """

    spin_directions = []
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            # Remove comment lines
            if line.startswith("#"):
                continue
            # Remove inline comments and leading/trailing whitespaces
            line = line.split("#")[0].strip()
            # Check for empty lines empty lines
            if line:
                line = line.split()
                if len(line) != 3:
                    raise ValueError(
                        f"Expected three numbers per line (in line{i}),"
                        f"got: {len(line)}."
                    )
                for tmp in line:
                    spin_directions.append(float(tmp))

    if len(spin_directions) % 3 != 0:
        raise ValueError(
            f"Length of the spin list should be dividable by three, got: {len(spin_directions)}."
        )

    spin_directions = np.array(spin_directions, dtype=float)
    # Pay attention to the np.reshape keywords
    spin_directions = np.reshape(spin_directions, (len(spin_directions) // 3, 3))
    spin_directions = (
        spin_directions / np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
    )
    return spin_directions


def _plot_cones(fig, positions, spin_directions, color, name=None):
    scale = 0.5

    if not PLOTLY_AVAILABLE:
        print(PLOTLY_ERROR_MESSAGE)
        raise ImportError(PLOTLY_ERROR_MESSAGE)

    # Prepare data
    x, y, z = np.transpose(positions, axes=(1, 0))
    u, v, w = np.transpose(spin_directions, axes=(1, 0))

    fig.add_traces(
        data=go.Cone(
            x=x + u * scale,
            y=y + v * scale,
            z=z + w * scale,
            u=u * (1 - scale),
            v=v * (1 - scale),
            w=w * (1 - scale),
            sizemode="raw",
            anchor="tail",
            legendgroup=name,
            name=name,
            showlegend=name is not None,
            showscale=False,
            colorscale=[color, color],
            hoverinfo="none",
        )
    )

    fig.add_traces(
        data=go.Scatter3d(
            mode="markers",
            x=x,
            y=y,
            z=z,
            marker=dict(size=10, color=color),
            hoverinfo="none",
            showlegend=False,
            legendgroup=name,
        )
    )

    for i in range(0, len(x)):
        fig.add_traces(
            dict(
                x=[x[i], x[i] + u[i] * scale],
                y=[y[i], y[i] + v[i] * scale],
                z=[z[i], z[i] + w[i] * scale],
                mode="lines",
                type="scatter3d",
                hoverinfo="none",
                line={"color": color, "width": 10},
                legendgroup=name,
                showlegend=False,
            )
        )

    return fig


def plot_spin_directions(
    output_name: str,
    positions,
    spin_directions,
    cell=None,
    highlight=None,
    name_highlighted="Group 1",
    name_other="Group 2",
    _full_plotly=True,
):
    r"""
    Plot a simple plot of spin directions in three projections.

    output_name : str
        Name of the file where the result is saved. An extension ".html" is added
        automatically.
    positions : (M, 3) |array-like|_
        Positions of atoms. The order should match an order in ``spin_directions``.
        Positions are used as given, i.e. absolute coordinates are expected.
    spin_directions : (M, 3) |array-like|_
        Directions of spin vectors. Only directions of vectors are used, modulus is
        ignored. The order should match the order in ``positions``.
    cell : (3, 3) |array-like|_, optional
        Three vectors of the unit cell. Rows are vectors, columns are coordinates.
        The provided cell do not affect the plotting procedure for the spins.
    highlight : list of int, optional
        List of indices for the ``spin_directions``. The spins with those indices will be
        plotted in different color.
    name_highlighted : str, default "Group 1"
        How to mark the highlighted spin on the legend.
    name_other : str, default "Group 2"
        How to mark the non-highlighted spin on the legend.
    _full_plotly : bool, default True
        Whether to produce full .html file that includes plotly.js. This argument is
        rather technical.

        * If `` _full_plotly == True``, then it passes ``include_plotlyjs=False`` and
          ``full_html=False`` to ``fig.write_html()``.
        * If `` _full_plotly == False``, then it passes ``include_plotlyjs=True`` and
          ``full_html=True`` to ``fig.write_html()``.
    """
    if not PLOTLY_AVAILABLE:
        print(PLOTLY_ERROR_MESSAGE)
        raise ImportError(PLOTLY_ERROR_MESSAGE)

    pos = np.array(positions, dtype=float)
    sd = np.array(spin_directions, dtype=float)

    # Get normalization length
    tmp = pos[:, np.newaxis] - pos[np.newaxis, :]
    tmp = np.linalg.norm(tmp, axis=2)
    norm_length = (tmp + np.eye(tmp.shape[0]) * tmp.max()).min()

    if norm_length == 0:
        norm_length = 1

    sd = sd / np.linalg.norm(sd, axis=1)[:, np.newaxis] * norm_length

    # Separate highlighted spins (pos2 and sd2)
    if highlight is None:
        pos1 = pos
        sd1 = sd
        pos2 = np.array([], dtype=float)
        sd2 = np.array([], dtype=float)
    else:
        highlight.sort()
        pos1 = []
        pos2 = []
        sd1 = []
        sd2 = []

        j = 0
        for i in range(len(sd)):
            if j >= len(highlight) or i != highlight[j]:
                pos2.append(pos[i])
                sd2.append(sd[i])
            else:
                pos1.append(pos[i])
                sd1.append(sd[i])
                j += 1

        pos1 = np.array(pos1)
        pos2 = np.array(pos2)
        sd1 = np.array(sd1)
        sd2 = np.array(sd2)

    fig = go.Figure()

    if len(pos1) > 0:
        _plot_cones(
            fig=fig,
            positions=pos1,
            spin_directions=sd1,
            color="#A47864",
            name=name_highlighted,
        )

    if len(pos2) > 0:
        _plot_cones(
            fig=fig,
            positions=pos2,
            spin_directions=sd2,
            color="#535FCF",
            name=name_other,
        )

    # Plot the unit cell
    if cell is not None:
        origin = np.array([0, 0, 0])
        a1, a2, a3 = cell
        bottom = np.array([origin, a1, a1 + a2, a2, origin])
        top = np.array([a3, a3 + a1, a3 + a1 + a2, a3 + a2, a3])
        leg1 = np.array([origin, a3])
        leg2 = np.array([a1, a1 + a3])
        leg3 = np.array([a2, a2 + a3])
        leg4 = np.array([a1 + a2, a1 + a2 + a3])

        for i, pset in enumerate([bottom, top, leg1, leg2, leg3, leg4]):
            x, y, z = pset.T
            fig.add_traces(
                dict(
                    x=x,
                    y=y,
                    z=z,
                    mode="lines",
                    type="scatter3d",
                    hoverinfo="none",
                    line={"color": "#000000", "width": 1},
                    showlegend=(i == 0),
                    legendgroup="Unit cell",
                    name="Unit cell",
                )
            )

        for i, vector in enumerate(cell):
            fig.add_traces(
                data=go.Cone(
                    x=[vector[0]],
                    y=[vector[1]],
                    z=[vector[2]],
                    u=[0.2 * vector[0]],
                    v=[0.2 * vector[1]],
                    w=[0.2 * vector[2]],
                    sizemode="absolute",
                    anchor="tip",
                    showscale=False,
                    colorscale=["#000000", "#000000"],
                    legendgroup=f"a_{i+1}",
                    showlegend=False,
                )
            )
            fig.add_traces(
                data=go.Scatter3d(
                    mode="text",
                    x=[1.2 * vector[0]],
                    y=[1.2 * vector[1]],
                    z=[1.2 * vector[2]],
                    marker=dict(size=0, color="#000000"),
                    text=f"a_{i+1}",
                    hoverinfo="none",
                    textposition="top center",
                    textfont=dict(size=12),
                    showlegend=False,
                    legendgroup=f"a_{i+1}",
                )
            )
            fig.add_traces(
                dict(
                    x=[0, vector[0]],
                    y=[0, vector[1]],
                    z=[0, vector[2]],
                    mode="lines",
                    type="scatter3d",
                    hoverinfo="none",
                    line={"color": "#000000", "width": 4},
                    legendgroup=f"a_{i+1}",
                    showlegend=True,
                    name=f"a_{i+1}",
                )
            )

    fig.update_layout(legend_title_text="Click to hide")
    fig.update_scenes(
        aspectmode="data", xaxis_visible=False, yaxis_visible=False, zaxis_visible=False
    )

    if _full_plotly:
        fig.write_html(
            file=f"{output_name}.html",
            include_plotlyjs=True,
            full_html=True,
        )
    else:
        fig.write_html(
            file=f"{output_name}.html",
            include_plotlyjs=False,
            full_html=False,
        )


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
