import os
from argparse import ArgumentParser

import numpy as np
import plotly.graph_objects as go
from factory import plot_arc, plot_line, plot_vector, save_figure


def get_figure():
    fig = go.Figure()
    plot_vector(fig, (1, 0, 0), label="x")
    plot_vector(fig, (0, 1, 0), label="y")
    plot_vector(fig, (0, 0, 1), label="z")
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
        os.path.join(images_dir, "cs-choice-n-angles.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=0.2, z=0.5)),
    )

    fig = go.Figure()
    plot_vector(fig, (1, 0, 0), label="x, u")
    plot_vector(fig, (0, 1, 0), label="y, v")
    plot_vector(fig, (0, 0, 1), label="z, n")
    plot_vector(
        fig, (-np.sin(np.pi / 2), np.cos(np.pi / 2), 0), label="r", color="#FF8800"
    )
    save_figure(fig, os.path.join(images_dir, "cs-choice-case-1.html"))

    fig = get_figure()
    plot_vector(fig, (0, -1, 0), label="u", color="#00B508")
    plot_vector(fig, (-1, 0, 0), label="v", color="#00B508")
    plot_vector(fig, (0, 0, -1), label="n", color="#00B508", label_shift=(0, 0, -0.4))
    plot_vector(
        fig, (-np.sin(np.pi / 4), np.cos(np.pi / 4), 0), label="r", color="#FF8800"
    )
    arc = np.linspace(0, np.pi, 50)
    arc = [
        np.cos(np.pi / 4) * np.sin(arc),
        np.sin(np.pi / 4) * np.sin(arc),
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
    )
    save_figure(
        fig,
        os.path.join(images_dir, "cs-choice-case-2.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=0.7, z=1.25)),
    )

    fig = get_figure()
    n = np.array([1, 3, 2], dtype=float)
    n /= np.linalg.norm(n)
    u = (1 - n[0] ** 2 / (1 + n[2]), -n[0] * n[1] / (1 + n[2]), -n[0])
    v = (-n[0] * n[1] / (1 + n[2]), 1 - n[1] ** 2 / (1 + n[2]), -n[1])
    plot_vector(fig, u, label="u", color="#00B508")
    plot_vector(fig, v, label="v", color="#00B508")
    plot_vector(fig, n, label="n", color="#00B508", label_shift=(0, 0, -0.4))
    plot_vector(fig, np.cross((0, 0, 1), n), label="r", color="#FF8800")
    alpha = np.arccos(n[2])
    beta = np.arccos(n[0] / np.linalg.norm(n[:2]))
    alpha_arc = np.linspace(0, alpha, 50)
    alpha_arc = [
        np.cos(beta) * np.sin(alpha_arc) / 2,
        np.sin(beta) * np.sin(alpha_arc) / 2,
        np.cos(alpha_arc) / 2,
    ]
    plot_arc(fig, arc=alpha_arc, label="α", color="#FF8800")
    save_figure(
        fig,
        os.path.join(images_dir, "cs-choice-case-3.html"),
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
