import numpy as np
import plotly.graph_objects as go


def plot_vector(
    fig,
    vector,
    origin=(0, 0, 0),
    color="black",
    label=None,
    label_shift=(0, 0, 0),
    kwargs=None,
):
    r"""
    Plot a vector on the given figure.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        Figure object.
    vector : (3,) array-like
        Vector, to be plotted.
    origin : (3,) array-like, default (0,0,0)
        Origin of the vector.
    color : str, default black
        Color for the vector and label.
    label : str, optional
        Label for the vector.
    label_shift : (3,) array-like, default (0,0,0)
        Shift of the label in data coordinates.
    """
    if kwargs is None:
        kwargs = {}
    x = np.array([origin[0], origin[0] + 0.85 * vector[0]])
    y = np.array([origin[1], origin[1] + 0.85 * vector[1]])
    z = np.array([origin[2], origin[2] + 0.85 * vector[2]])
    cone_x = np.array([origin[0], origin[0] + vector[0]])
    cone_y = np.array([origin[1], origin[1] + vector[1]])
    cone_z = np.array([origin[2], origin[2] + vector[2]])
    fig.add_trace(
        {
            "x": x,
            "y": y,
            "z": z,
            "mode": "lines",
            "type": "scatter3d",
            "hoverinfo": "none",
            "line": {"color": color, "width": 5},
            "showlegend": False,
        },
        **kwargs,
    )
    fig.add_trace(
        {
            "type": "cone",
            "x": [cone_x[1]],
            "y": [cone_y[1]],
            "z": [cone_z[1]],
            "u": [0.3 * (vector[0])],
            "v": [0.3 * (vector[1])],
            "w": [0.3 * (vector[2])],
            "anchor": "tip",
            "hoverinfo": "none",
            "colorscale": [[0, color], [1, color]],
            "showscale": False,
            "showlegend": False,
        },
        **kwargs,
    )
    if label is not None:
        fig.add_trace(
            go.Scatter3d(
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
            ),
            **kwargs,
        )


def plot_arc(
    fig,
    arc,
    label=None,
    arrow=False,
    color="black",
    label_shift=(0, 0, 0),
    arrow_scale=0.25,
    kwargs=None,
):
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
    arrow_scale : float, default 0.25
        Scale of the arrow head with respect to the arc length.
    """
    if kwargs is None:
        kwargs = {}
    fig.add_trace(
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
        **kwargs,
    )
    fig.add_trace(
        go.Scatter3d(
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
        ),
        **kwargs,
    )
    if arrow:
        index = int(-len(arc[0]) * arrow_scale)
        fig.add_trace(
            {
                "type": "cone",
                "x": [arc[0][-1]],
                "y": [arc[1][-1]],
                "z": [arc[2][-1]],
                "u": [(2 * arc[0][-1] - 2 * arc[0][index])],
                "v": [(2 * arc[1][-1] - 2 * arc[1][index])],
                "w": [(2 * arc[2][-1] - 2 * arc[2][index])],
                "anchor": "tip",
                "hoverinfo": "none",
                "colorscale": [[0, color], [1, color]],
                "showscale": False,
                "showlegend": False,
            },
            **kwargs,
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
    fig.add_trace(
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
    )


def save_figure(
    fig,
    name,
    scene_keywords=None,
    camera_keywords=None,
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
    if camera_keywords is None:
        camera_keywords = {}
    if scene_keywords is None:
        scene_keywords = {}
    camera = dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.25, y=1.25, z=1.25),
    )
    for key in camera_keywords:
        camera[key] = camera_keywords[key]
    scene = dict(
        camera=camera,
        aspectratio=dict(x=1, y=1, z=1),
    )
    for key in scene_keywords:
        scene[key] = scene_keywords[key]
    fig.update_layout(
        width=600, height=500, margin=dict(l=0, r=0, t=0, b=0), scene=scene
    )
    fig.write_html(name, full_html=False, include_plotlyjs=False)
