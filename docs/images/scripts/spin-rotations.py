import os
from argparse import ArgumentParser

import numpy as np
import plotly.graph_objects as go


def plot_vector(fig, vector, label, color="black", label_shift=(0, 0, 0)):
    x = np.array([0, vector[0]])
    y = np.array([0, vector[1]])
    z = np.array([0, vector[2]])
    fig.add_traces(
        data=[
            {
                "x": 0.85 * x,
                "y": 0.85 * y,
                "z": 0.85 * z,
                "mode": "lines",
                "type": "scatter3d",
                "hoverinfo": "none",
                "line": {"color": color, "width": 5},
                "showlegend": False,
            },
            {
                "type": "cone",
                "x": [x[1]],
                "y": [y[1]],
                "z": [z[1]],
                "u": [0.3 * (x[1] - x[0])],
                "v": [0.3 * (y[1] - y[0])],
                "w": [0.3 * (z[1] - z[0])],
                "anchor": "tip",
                "hoverinfo": "none",
                "colorscale": [[0, color], [1, color]],
                "showscale": False,
                "showlegend": False,
            },
        ]
    )
    fig.add_traces(
        data=go.Scatter3d(
            mode="text",
            x=[x[1] + label_shift[0]],
            y=[y[1] + label_shift[1]],
            z=[z[1] + label_shift[2]],
            marker=dict(size=0),
            text=label,
            hoverinfo="none",
            textposition="top center",
            textfont=dict(size=20, color=color),
            showlegend=False,
        )
    )


def save_figure(
    fig,
    name,
    scene=dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.25, y=1.25, z=1.25),
    ),
):
    fig.update_scenes(
        aspectmode="data", xaxis_visible=False, yaxis_visible=False, zaxis_visible=False
    )
    fig.update_layout(
        width=600, height=500, margin=dict(l=0, r=0, t=0, b=0), scene_camera=scene
    )
    fig.write_html(name, full_html=False, include_plotlyjs=False)


def plot_arc(fig, arc, label=None, arrow=False, color="black", label_shift=(0, 0, 0)):
    fig.add_traces(
        data=[
            {
                "x": arc[0],
                "y": arc[1],
                "z": arc[2],
                "mode": "lines",
                "type": "scatter3d",
                "hoverinfo": "none",
                "line": {"color": color, "width": 2},
                "showlegend": False,
            },
        ]
    )
    fig.add_traces(
        data=go.Scatter3d(
            mode="text",
            x=[arc[0][len(arc[0]) // 2] + label_shift[0]],
            y=[arc[1][len(arc[0]) // 2] + label_shift[1]],
            z=[arc[2][len(arc[0]) // 2] + label_shift[2]],
            marker=dict(size=0),
            text=label,
            hoverinfo="none",
            textposition="top center",
            textfont=dict(size=20, color=color),
            showlegend=False,
        )
    )
    if arrow:
        fig.add_traces(
            data=[
                {
                    "type": "cone",
                    "x": [arc[0][-1]],
                    "y": [arc[1][-1]],
                    "z": [arc[2][-1]],
                    "u": [(2 * arc[0][-1] - 2 * arc[0][-len(arc[0]) // 5])],
                    "v": [(2 * arc[1][-1] - 2 * arc[1][-len(arc[0]) // 5])],
                    "w": [(2 * arc[2][-1] - 2 * arc[2][-len(arc[0]) // 5])],
                    "anchor": "tip",
                    "hoverinfo": "none",
                    "colorscale": [[0, color], [1, color]],
                    "showscale": False,
                    "showlegend": False,
                },
            ]
        )


def main(root_directory, theta, phi, S):
    theta = theta / 180 * np.pi
    phi = phi / 180 * np.pi
    images_dir = os.path.join(root_directory, "docs", "images")
    fig = go.Figure()
    Svec = (
        np.array(
            [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)],
            dtype=float,
        )
        * S
    )
    plot_vector(fig, (1, 0, 0), label=R"u")
    plot_vector(fig, (0, 1, 0), label=R"v")
    plot_vector(fig, (0, 0, 1), label=R"n")
    plot_vector(fig, Svec, label=R"S", color="#9E77F0")
    plot_vector(fig, (0, 0, S), label="S0", color="#4EB436", label_shift=(0, 0.1, 0))
    plot_vector(
        fig, (S * np.sin(theta), 0, S * np.cos(theta)), label="S'", color="#AB4740"
    )
    traces = [
        ([Svec[0], Svec[0]], [Svec[1], Svec[1]], [0, Svec[2]]),
        ([0, Svec[0]], [0, Svec[1]], [0, 0]),
        ([Svec[0], Svec[0]], [0, Svec[1]], [0, 0]),
        ([0, Svec[0]], [Svec[1], Svec[1]], [0, 0]),
    ]
    for x, y, z in traces:
        fig.add_traces(
            data=[
                {
                    "x": x,
                    "y": y,
                    "z": z,
                    "mode": "lines",
                    "type": "scatter3d",
                    "hoverinfo": "none",
                    "line": {"color": "#FF8800", "width": 3},
                    "showlegend": False,
                },
            ]
        )

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
    plot_arc(fig, arc=phi_arc, color="#FF8800", label="φ", label_shift=(0.1, 0, -0.1))

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
        label_shift=(0.1, 0.09, -0.1),
    )

    save_figure(
        fig,
        os.path.join(images_dir, "spin-rotations-1.html"),
        scene=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.25, y=0.5, z=0.75),
        ),
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
