import numpy as np
import plotly.graph_objects as go


def plot_vector(fig, vector, color="black", label=None, label_shift=(0, 0, 0)):
    r"""
    Plot a vector on the given figure.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        Figure object.
    vector : (3,) array-like
        Vector, to be plotted.
    color : str, default black
        Color for the vector and label.
    label : str, optional
        Label for the vector.
    label_shift : (3,) array-like, default (0,0,0)
        Shift of the label in data coordinates.
    """
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
    if label is not None:
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


def plot_arc(fig, arc, label=None, arrow=False, color="black", label_shift=(0, 0, 0)):
    r"""
    Plot an arc.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        Figure object.
    arc : (3, N) array-like
        N points, which describes the arc.
    color : str, default black
        Color for the arc and label.
    label : str, optional
        Label for the arc.
    label_shift : (3,) array-like, default (0,0,0)
        Shift of the label in data coordinates.
    """

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


def plot_line(fig, x, y, z, color="black", width=3):
    r"""
    Plot a line.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        Figure object.
    x : (2,) array-like
        x coordinates of the line: [start, finish]
    y : (2,) array-like
        y coordinates of the line: [start, finish]
    z : (2,) array-like
        z coordinates of the line: [start, finish]
    color : str, default black
        Color for the arc and label.
    width : float
        Width of the line.
    """
    fig.add_traces(
        data=[
            {
                "x": x,
                "y": y,
                "z": z,
                "mode": "lines",
                "type": "scatter3d",
                "hoverinfo": "none",
                "line": {"color": color, "width": width},
                "showlegend": False,
            },
        ]
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
    r"""
    Save figure as lightweight html file, ready to be included into the sphinx docs.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        Figure object.
    name : str
        Path to the file where the figure is saved. With extension.
    scene : dict
        Dictionary for the ``scene_camera`` of ``fig.update_layout``.
    """
    fig.update_scenes(
        aspectmode="data", xaxis_visible=False, yaxis_visible=False, zaxis_visible=False
    )
    fig.update_layout(
        width=600, height=500, margin=dict(l=0, r=0, t=0, b=0), scene_camera=scene
    )
    fig.write_html(name, full_html=False, include_plotlyjs=False)
