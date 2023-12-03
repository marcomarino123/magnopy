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


def get_figure():
    fig = go.Figure()
    plot_vector(fig, (1, 0, 0), label="x")
    plot_vector(fig, (0, 1, 0), label="y")
    plot_vector(fig, (0, 0, 1), label="z")
    return fig


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


def plot_n_angles(fig, n, color):
    plot_vector(fig, n, color=color, label="n")
    traces = [
        ([n[0], n[0]], [n[1], n[1]], [0, n[2]]),
        ([0, n[0]], [0, n[1]], [0, 0]),
        ([n[0], n[0]], [0, n[1]], [0, 0]),
        ([0, n[0]], [n[1], n[1]], [0, 0]),
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

    alpha = np.arccos(n[2])
    beta = np.arccos(n[0] / np.linalg.norm(n[:2]))
    alpha_arc = np.linspace(0, alpha, 50)
    alpha_arc = [
        np.cos(beta) * np.sin(alpha_arc) / 2,
        np.sin(beta) * np.sin(alpha_arc) / 2,
        np.cos(alpha_arc) / 2,
    ]
    fig.add_traces(
        data=[
            {
                "x": alpha_arc[0],
                "y": alpha_arc[1],
                "z": alpha_arc[2],
                "mode": "lines",
                "type": "scatter3d",
                "hoverinfo": "none",
                "line": {"color": "#FF8800", "width": 2},
                "showlegend": False,
            },
        ]
    )
    fig.add_traces(
        data=go.Scatter3d(
            mode="text",
            x=[alpha_arc[0][25]],
            y=[alpha_arc[1][25]],
            z=[alpha_arc[2][25]],
            marker=dict(size=0),
            text="α",
            hoverinfo="none",
            textposition="top center",
            textfont=dict(size=20, color="#FF8800"),
            showlegend=False,
        )
    )

    beta_arc = np.linspace(0, beta, 50)
    beta_arc = [np.cos(beta_arc) / 2, np.sin(beta_arc) / 2, np.zeros_like(beta_arc)]
    fig.add_traces(
        data=[
            {
                "x": beta_arc[0],
                "y": beta_arc[1],
                "z": beta_arc[2],
                "mode": "lines",
                "type": "scatter3d",
                "hoverinfo": "none",
                "line": {"color": "#FF8800", "width": 2},
                "showlegend": False,
            },
        ]
    )
    fig.add_traces(
        data=go.Scatter3d(
            mode="text",
            x=[beta_arc[0][25]],
            y=[beta_arc[1][25]],
            z=[beta_arc[2][25] - 0.05],
            marker=dict(size=0),
            text="β",
            hoverinfo="none",
            textposition="top center",
            textfont=dict(size=20, color="#FF8800"),
            showlegend=False,
        )
    )


def main(root_directory):
    images_dir = os.path.join(root_directory, "docs", "images")
    fig = get_figure()
    n = np.array([1, 1, 1], dtype=float)
    n /= np.linalg.norm(n)
    plot_n_angles(fig, n, "#00B508")
    save_figure(
        fig,
        os.path.join(images_dir, "cs-choice-n-angles.html"),
        scene=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.25, y=0.2, z=0.5),
        ),
    )

    fig = go.Figure()
    plot_vector(fig, (1, 0, 0), label="x, u")
    plot_vector(fig, (0, 1, 0), label="y, v")
    plot_vector(fig, (0, 0, 1), label="z, n")
    save_figure(fig, os.path.join(images_dir, "cs-choice-case-1.html"))

    fig = get_figure()
    plot_vector(fig, (0, -1, 0), label="u", color="#00B508")
    plot_vector(fig, (-1, 0, 0), label="v", color="#00B508")
    plot_vector(fig, (0, 0, -1), label="n", color="#00B508", label_shift=(0, 0, -0.4))
    save_figure(fig, os.path.join(images_dir, "cs-choice-case-2.html"))

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
    fig.add_traces(
        data=[
            {
                "x": alpha_arc[0],
                "y": alpha_arc[1],
                "z": alpha_arc[2],
                "mode": "lines",
                "type": "scatter3d",
                "hoverinfo": "none",
                "line": {"color": "#FF8800", "width": 2},
                "showlegend": False,
            },
            {
                "type": "cone",
                "x": [alpha_arc[0][-1]],
                "y": [alpha_arc[1][-1]],
                "z": [alpha_arc[2][-1]],
                "u": [(2 * alpha_arc[0][-1] - 2 * alpha_arc[0][-10])],
                "v": [(2 * alpha_arc[1][-1] - 2 * alpha_arc[1][-10])],
                "w": [(2 * alpha_arc[2][-1] - 2 * alpha_arc[2][-10])],
                "anchor": "tip",
                "hoverinfo": "none",
                "colorscale": [[0, "#FF8800"], [1, "#FF8800"]],
                "showscale": False,
                "showlegend": False,
            },
        ]
    )
    fig.add_traces(
        data=go.Scatter3d(
            mode="text",
            x=[alpha_arc[0][25]],
            y=[alpha_arc[1][25]],
            z=[alpha_arc[2][25]],
            marker=dict(size=0),
            text="α",
            hoverinfo="none",
            textposition="top center",
            textfont=dict(size=20, color="#FF8800"),
            showlegend=False,
        )
    )
    save_figure(
        fig,
        os.path.join(images_dir, "cs-choice-case-3.html"),
        scene=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.25, y=1, z=0.2),
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
    main(**vars(parser.parse_args()))
