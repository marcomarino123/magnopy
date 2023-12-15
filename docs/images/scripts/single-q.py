# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2023 Magnopy Team
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

import os
from argparse import ArgumentParser

import numpy as np
import plotly.graph_objects as go
from factory import plot_arc, plot_line, plot_vector, save_figure


def plot_example(spins, Q, N):
    r"""
    Plot example spin spiral for the cubic crystal.

    Lattice parameters are: a = b = c = 1 in the uvn
    reference frame. abc is oriented along uvn.

    Parameters
    ----------
    spins : (M, 5) array-like
        M spins in the unit cell. Each spin is a list of
        five floats: (Sx, Sy, Sz, theta, phi).
    Q : (3,) array-like
        Spin spiral vector.
    N : (3,) array-like
        (Na, Nb, Nc) - number of unit cells to be drawn.
    output_name : str
        Output name. Including the extension.

    Return
    ------
    fig : plotly.graph_obfect.Figure
        Figure with the plotted spiral.
    """
    fig = go.Figure()
    plot_vector(fig, (N[0], 0, 0), label="u", cone_scale=0.3 / max(N[0], 1))
    plot_vector(fig, (0, N[1], 0), label="v", cone_scale=0.3 / max(N[1], 1))
    plot_vector(fig, (0, 0, N[2]), label="n", cone_scale=0.3 / max(N[2], 1))

    for i in range(N[0]):
        for j in range(N[1]):
            for k in range(N[2]):
                for a in range(len(spins)):
                    R = np.array(
                        [i + spins[a][0], j + spins[a][1], k + spins[a][2]], dtype=float
                    )
                    theta = spins[a][3]
                    phi = spins[a][4]
                    vector = [
                        np.sin(theta) * np.cos(phi + Q @ R),
                        np.sin(theta) * np.sin(phi + Q @ R),
                        np.cos(theta),
                    ]
                    plot_vector(
                        fig,
                        vector=vector,
                        origin=R,
                        cone_scale=0.4,
                        line_width=4,
                        color="#E7676B",
                        origin_pont=True,
                    )
                    arc = np.linspace(0, 2 * np.pi, 100)
                    arc = [
                        R[0] + np.sin(theta) * np.cos(arc),
                        R[1] + np.sin(theta) * np.sin(arc),
                        R[2] + np.cos(theta) * np.ones_like(arc),
                    ]
                    plot_arc(fig, arc, color="#63C06F")

    return fig


def main(root_directory):
    images_dir = os.path.join(root_directory, "docs", "images")
    fig = plot_example(spins=[(0, 0, 0, np.pi / 2, 0)], Q=(0, 0, 1), N=(1, 1, 5))
    zoom = 1.5
    save_figure(
        fig,
        os.path.join(images_dir, "single-q-1.html"),
        camera_keywords=dict(eye=dict(x=1.25 * zoom, y=1.25 * zoom, z=0.25 * zoom)),
    )

    fig = plot_example(spins=[(0, 0, 0, np.pi / 3, 0)], Q=(0, 0, 1), N=(1, 1, 5))
    zoom = 1.5
    save_figure(
        fig,
        os.path.join(images_dir, "single-q-2.html"),
        camera_keywords=dict(eye=dict(x=1.25 * zoom, y=1.25 * zoom, z=0.25 * zoom)),
    )

    fig = plot_example(
        spins=[(0, 0, 0, np.pi / 3, np.pi / 4)], Q=(0, 0, 1), N=(1, 1, 5)
    )
    zoom = 1.5
    save_figure(
        fig,
        os.path.join(images_dir, "single-q-3.html"),
        camera_keywords=dict(eye=dict(x=1.25 * zoom, y=1.25 * zoom, z=0.25 * zoom)),
    )

    fig = plot_example(spins=[(0, 0, 0, np.pi / 6, 0)], Q=(0, 1, 0), N=(1, 5, 1))
    zoom = 1.2
    save_figure(
        fig,
        os.path.join(images_dir, "single-q-4.html"),
        camera_keywords=dict(eye=dict(x=1.25 * zoom, y=1.25 * zoom, z=1.25 * zoom)),
    )

    fig = plot_example(
        spins=[(0, 0, 0, np.pi / 6, 0), (0.5, 0.5, 0.5, np.pi / 12, np.pi / 4)],
        Q=(0, 1, 0),
        N=(1, 5, 1),
    )
    zoom = 1.4
    save_figure(
        fig,
        os.path.join(images_dir, "single-q-5.html"),
        camera_keywords=dict(eye=dict(x=1.25 * zoom, y=0.5 * zoom, z=0.5 * zoom)),
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-rd",
        "--root_directory",
        type=str,
        help="Root directory of magnopy",
        required=True,
    )

    main(**vars(parser.parse_args()))
