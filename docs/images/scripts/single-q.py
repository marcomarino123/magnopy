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


def plot_example_3(output_name):
    fig = go.Figure()
    plot_vector(fig, (7, 0, 0), label="v", cone_scale=0.1)
    plot_vector(fig, (0, 0, 2), label="n", cone_scale=0.3)
    X = np.linspace(0, 7, 8)
    theta = np.pi / 7
    for i in range(len(X)):
        vector = [
            np.sin(theta) * np.cos(X[i]),
            np.sin(theta) * np.sin(X[i]),
            np.cos(theta),
        ]
        plot_vector(
            fig,
            vector=vector,
            origin=(X[i], 0, 0),
            cone_scale=0.4,
            line_width=4,
            color="#E7676B",
        )
        arc = np.linspace(0, 2 * np.pi, 100)
        arc = [
            np.ones_like(arc) * X[i] + np.cos(arc) * np.sin(theta),
            np.sin(arc) * np.sin(theta),
            np.ones_like(arc) * np.cos(theta),
        ]
        plot_arc(fig, arc=arc, color="#63C06F")
    zoom = 1
    save_figure(
        fig,
        output_name,
        camera_keywords=dict(eye=dict(x=2 * zoom, y=-1.4 * zoom, z=1 * zoom)),
    )


def plot_example_4(output_name):
    fig = go.Figure()
    plot_vector(fig, (16, 0, 0), label="v", cone_scale=0.1)
    plot_vector(fig, (0, 0, 4), label="n", cone_scale=0.3)
    X = np.linspace(0, 7, 8)
    theta = (np.pi / 7, np.pi / 4)
    for i in range(len(X)):
        for a in range(2):
            vector = [
                1.5 * np.sin(theta[a]) * np.cos(X[i] * 2 + a),
                1.5 * np.sin(theta[a]) * np.sin(X[i] * 2 + a),
                1.5 * np.cos(theta[a]),
            ]
            plot_vector(
                fig,
                vector=vector,
                origin=(X[i] * 2 + a, a / 3, 0),
                cone_scale=0.4,
                line_width=4,
                color="#E7676B",
            )
            arc = np.linspace(0, 2 * np.pi, 100)
            arc = [
                np.ones_like(arc) * (X[i] * 2 + a)
                + 1.5 * np.cos(arc) * np.sin(theta[a]),
                1.5 * np.sin(arc) * np.sin(theta[a]) + a / 3,
                1.5 * np.ones_like(arc) * np.cos(theta[a]),
            ]
            plot_arc(fig, arc=arc, color="#63C06F")
    zoom = 1
    save_figure(
        fig,
        output_name,
        camera_keywords=dict(eye=dict(x=2 * zoom, y=-1.4 * zoom, z=1 * zoom)),
    )


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
