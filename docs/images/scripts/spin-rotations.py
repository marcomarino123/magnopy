import os
from argparse import ArgumentParser

import numpy as np
import plotly.graph_objects as go
from factory import plot_arc, plot_line, plot_vector, save_figure


def prepare_figure(fig, theta, phi, S):
    Svec = (
        np.array(
            [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)],
            dtype=float,
        )
        * S
    )
    plot_vector(fig, (1, 0, 0), label=R"u")
    plot_vector(fig, (0, 1, 0), label=R"v")
    plot_vector(fig, (0, 0, 1), label=R"n", label_shift=(0, 0, 0.2))
    plot_vector(fig, Svec, label=R"S", color="#9E77F0", label_shift=(-0.05, 0.1, 0))
    plot_vector(fig, (0, 0, S), label="S0", color="#4EB436", label_shift=(0.1, -0.1, 0))
    traces = [
        ([Svec[0], Svec[0]], [Svec[1], Svec[1]], [0, Svec[2]]),
        ([0, Svec[0]], [0, Svec[1]], [0, 0]),
        ([Svec[0], Svec[0]], [0, Svec[1]], [0, 0]),
        ([0, Svec[0]], [Svec[1], Svec[1]], [0, 0]),
    ]
    for x, y, z in traces:
        plot_line(fig, x, y, z, color="#FF8800")

    theta_arc = np.linspace(0, theta, 50)
    theta_arc = [
        S * np.cos(phi) * np.sin(theta_arc) / 2,
        S * np.sin(phi) * np.sin(theta_arc) / 2,
        S * np.cos(theta_arc) / 2,
    ]
    plot_arc(fig, arc=theta_arc, color="#FF8800", label="θ")
    phi_arc = np.linspace(0, phi, 50)
    phi_arc = [
        S * np.sin(theta) * np.cos(phi_arc) / 2,
        S * np.sin(theta) * np.sin(phi_arc) / 2,
        np.zeros_like(phi_arc),
    ]
    plot_arc(fig, arc=phi_arc, color="#FF8800", label="φ", label_shift=(0.2, 0, -0.1))

    return Svec


def main(root_directory, theta, phi, S):
    theta = theta / 180 * np.pi
    phi = phi / 180 * np.pi
    images_dir = os.path.join(root_directory, "docs", "images")
    fig = go.Figure()
    prepare_figure(fig, theta, phi, S)
    plot_vector(
        fig,
        (S * np.sin(theta), 0, S * np.cos(theta)),
        label="S'",
        color="#AB4740",
        label_shift=(0.2, 0, 0),
    )
    theta_arc = np.linspace(0, theta, 50)
    theta_arc = [
        S * np.sin(theta_arc) * 0.6,
        np.zeros_like(theta_arc),
        S * np.cos(theta_arc) * 0.6,
    ]
    plot_arc(
        fig,
        arc=theta_arc,
        color="#AB4740",
        label="R(θ)",
        arrow=True,
        label_shift=(0.1, 0, 0),
    )

    phi_arc = np.linspace(0, phi, 50)
    phi_arc = [
        S * np.sin(theta) * np.cos(phi_arc) * 0.7,
        S * np.sin(theta) * np.sin(phi_arc) * 0.7,
        S * np.cos(theta) * 0.7 * np.ones_like(phi_arc),
    ]
    plot_arc(
        fig,
        arc=phi_arc,
        color="#9E77F0",
        label="R(φ)",
        arrow=True,
        label_shift=(0, 0, -0.2),
    )

    save_figure(
        fig,
        os.path.join(images_dir, "spin-rotations-simple.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=0.5, z=0.75)),
    )

    fig = go.Figure()
    Svec = prepare_figure(fig, theta, phi, S)
    arc = np.linspace(0, theta, 50)
    arc = [
        S * np.cos(phi) * np.sin(arc),
        S * np.sin(phi) * np.sin(arc),
        S * np.cos(arc),
    ]
    plot_arc(fig, arc=arc, color="#9E77F0", label="R(θ, φ)", arrow=True)
    r = np.cross((0, 0, 1), Svec)
    r /= np.linalg.norm(r)
    plot_vector(fig, vector=r, color="#9E77F0", label="r")

    save_figure(
        fig,
        os.path.join(images_dir, "spin-rotations-symmetric.html"),
        camera_keywords=dict(eye=dict(x=1.25, y=0.2, z=0.1)),
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
    parser.add_argument(
        "--theta",
        type=float,
        help="Theta angle for the spin direction.",
        default=40,
    )
    parser.add_argument(
        "--phi",
        type=float,
        help="Phi angle for the spin direction.",
        default=60,
    )
    parser.add_argument(
        "--S",
        type=float,
        help="Modulus of the spin vector.",
        default=0.7,
    )

    main(**vars(parser.parse_args()))
