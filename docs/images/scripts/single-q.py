import os
from argparse import ArgumentParser

import numpy as np
import plotly.graph_objects as go
from factory import plot_arc, plot_line, plot_vector, save_figure


def plot_example_1(output_name):
    fig = go.Figure()
    plot_vector(fig, (8, 0, 0), label="n", cone_scale=0.1)
    X = np.linspace(0, 7, 8)
    theta = np.pi / 2
    for i in range(len(X)):
        vector = [
            0,
            np.cos(X[i]),
            np.sin(X[i]),
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
        arc = [np.ones_like(arc) * X[i], np.cos(arc), np.sin(arc)]
        plot_arc(fig, arc=arc, color="#63C06F")
    zoom = 0.85
    save_figure(
        fig,
        output_name,
        camera_keywords=dict(eye=dict(x=1.35 * zoom, y=-1.4 * zoom, z=1 * zoom)),
    )


def plot_example_2(output_name):
    fig = go.Figure()
    plot_vector(fig, (8, 0, 0), label="n", cone_scale=0.1)
    X = np.linspace(0, 7, 8)
    theta = np.pi / 3
    for i in range(len(X)):
        vector = [
            np.cos(theta),
            np.cos(X[i]) * np.sin(theta),
            np.sin(X[i]) * np.sin(theta),
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
            np.ones_like(arc) * X[i] + np.cos(theta),
            np.cos(arc) * np.sin(theta),
            np.sin(arc) * np.sin(theta),
        ]
        plot_arc(fig, arc=arc, color="#63C06F")
    zoom = 0.9
    save_figure(
        fig,
        output_name,
        camera_keywords=dict(eye=dict(x=1.35 * zoom, y=-1.4 * zoom, z=1 * zoom)),
    )


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
    plot_example_1(os.path.join(images_dir, "single-q-1.html"))
    plot_example_2(os.path.join(images_dir, "single-q-2.html"))
    plot_example_3(os.path.join(images_dir, "single-q-3.html"))
    plot_example_4(os.path.join(images_dir, "single-q-4.html"))


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
