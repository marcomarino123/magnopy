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
from factory import plot_arc, plot_example, plot_line, plot_vector, save_figure


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
    fig = plot_example(
        spins=[(0, 0, 0, 5 * np.pi / 6, 0), (0, 0.5, 0, np.pi / 6, np.pi)],
        Q=(1, 0, 0),
        N=(5, 1, 1),
    )
    zoom = 1.5
    save_figure(
        fig,
        os.path.join(images_dir, "single-q-6.html"),
        camera_keywords=dict(eye=dict(x=1.25 * zoom, y=-1.25 * zoom, z=1 * zoom)),
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
