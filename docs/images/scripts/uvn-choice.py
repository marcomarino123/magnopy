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
from plotly.subplots import make_subplots


def get_figure():
    fig = go.Figure()
    plot_vector(fig, (1, 0, 0), label="x")
    plot_vector(fig, (0, 1, 0), label="y")
    plot_vector(fig, (0, 0, 1), label="z", label_shift=(0, 0, 0.2))
    return fig


def plot_n_angles(fig, n, color):
    plot_vector(fig, n, color=color, label="n")
    traces = [
        ([n[0], n[0]], [n[1], n[1]], [0, n[2]]),
        ([0, n[0]], [0, n[1]], [0, 0]),
        ([n[0], n[0]], [0, n[1]], [0, 0]),
        ([0, n[0]], [n[1], n[1]], [0, 0]),
    ]
    for x, y, z in traces:
        plot_line(fig, x, y, z, color="#FF8800")

    alpha = np.arccos(n[2])
    beta = np.arccos(n[0] / np.linalg.norm(n[:2]))
    alpha_arc = np.linspace(0, alpha, 50)
    alpha_arc = [
        np.cos(beta) * np.sin(alpha_arc) / 2,
        np.sin(beta) * np.sin(alpha_arc) / 2,
        np.cos(alpha_arc) / 2,
    ]
    plot_arc(fig, arc=alpha_arc, label="α", color="#FF8800")

    beta_arc = np.linspace(0, beta, 50)
    beta_arc = [np.cos(beta_arc) / 2, np.sin(beta_arc) / 2, np.zeros_like(beta_arc)]
    plot_arc(fig, arc=beta_arc, label="β", color="#FF8800")


def main(root_directory):
    images_dir = os.path.join(root_directory, "docs", "images")
    fig = get_figure()
    n = np.array([1, 1, 1], dtype=float)
    n /= np.linalg.norm(n)
    plot_n_angles(fig, n, "#00B508")
    save_figure(
        fig,
        os.path.join(images_dir, "uvn-choice-n-angles.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=0.2, z=0.5)),
    )

    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "scene"}, {"type": "scene"}]])
    plot_vector(fig, (1, 0, 0), label="x, u", kwargs=dict(row=1, col=1))
    plot_vector(fig, (0, 1, 0), label="y, v", kwargs=dict(row=1, col=1))
    plot_vector(fig, (0, 0, 1), label="z, n", kwargs=dict(row=1, col=1))
    plot_vector(
        fig,
        (-np.sin(np.pi / 2), np.cos(np.pi / 2), 0),
        label="r",
        color="#FF8800",
        kwargs=dict(row=1, col=1),
    )

    plot_vector(fig, (1, 0, 0), label="x", kwargs=dict(row=1, col=2))
    plot_vector(fig, (0, 1, 0), label="y", kwargs=dict(row=1, col=2))
    plot_vector(fig, (0, 0, 1), label="z", kwargs=dict(row=1, col=2))
    plot_vector(
        fig,
        (1, 0, 0),
        label="u",
        color="#00B508",
        kwargs=dict(row=1, col=2),
        label_shift=(0.2, 0, 0),
    )
    plot_vector(fig, (0, -1, 0), label="v", color="#00B508", kwargs=dict(row=1, col=2))
    plot_vector(
        fig,
        (0, 0, -1),
        label="n",
        color="#00B508",
        label_shift=(0, 0.2, 0),
        kwargs=dict(row=1, col=2),
    )
    plot_vector(
        fig,
        (-np.sin(np.pi / 2), np.cos(np.pi / 2), 0),
        label="r",
        color="#FF8800",
        kwargs=dict(row=1, col=2),
    )
    arc = np.linspace(0, np.pi, 50)
    arc = [
        np.cos(np.pi / 2) * np.sin(arc),
        np.sin(np.pi / 2) * np.sin(arc),
        np.cos(arc),
    ]
    plot_arc(
        fig,
        arc,
        color="#FF8800",
        label="α",
        arrow=True,
        arrow_scale=0.1,
        label_shift=(0.2, 0.2, 0),
        kwargs=dict(row=1, col=2),
    )
    save_figure(
        fig,
        os.path.join(images_dir, "uvn-choice-special-cases.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=0.7, z=1.25)),
    )

    fig = get_figure()
    n = np.array([1, 3, 2], dtype=float)
    n /= np.linalg.norm(n)
    u = (1 - n[0] ** 2 / (1 + n[2]), -n[0] * n[1] / (1 + n[2]), -n[0])
    v = (-n[0] * n[1] / (1 + n[2]), 1 - n[1] ** 2 / (1 + n[2]), -n[1])
    plot_vector(fig, u, label="u", color="#00B508")
    plot_vector(fig, v, label="v", color="#00B508")
    plot_vector(fig, n, label="n", color="#00B508", label_shift=(0, 0, -0.2))
    r = np.cross((0, 0, 1), n)
    r /= np.linalg.norm(r)
    plot_vector(fig, r, label="r", color="#FF8800")
    alpha = np.arccos(n[2])
    beta = np.arccos(n[0] / np.linalg.norm(n[:2]))
    alpha_arc = np.linspace(0, alpha, 50)
    alpha_arc = [
        np.cos(beta) * np.sin(alpha_arc) / 2,
        np.sin(beta) * np.sin(alpha_arc) / 2,
        np.cos(alpha_arc) / 2,
    ]
    plot_arc(fig, arc=alpha_arc, label="α", color="#FF8800", arrow=True)
    save_figure(
        fig,
        os.path.join(images_dir, "uvn-choice-main-case.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=1, z=0.2)),
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
