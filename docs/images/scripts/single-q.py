import os
from argparse import ArgumentParser

import numpy as np
import plotly.graph_objects as go
from factory import plot_arc, plot_line, plot_vector, save_figure


def plot_2d_example(output_name):
    fig = go.Figure()
    X = np.linspace(0, 10, 11)
    Y = np.linspace(0, 10, 11)
    theta = np.pi / 5
    Q = np.array([1, 1, 0], dtype=float)
    for i in range(len(X)):
        for j in range(len(Y)):
            R = [X[i], Y[j], 0]
            vector = [
                np.sin(theta) * np.cos(Q @ R),
                np.sin(theta) * np.sin(Q @ R),
                np.cos(theta),
            ]
            plot_vector(
                fig,
                vector=vector,
                origin=(X[i], Y[j], 0),
            )

    save_figure(fig, output_name)


def main(root_directory):
    images_dir = os.path.join(root_directory, "docs", "images")
    plot_2d_example(os.path.join(images_dir, "single-q-2d-example.html"))


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
