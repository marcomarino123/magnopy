import os
from argparse import ArgumentParser

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, ax, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs
        self.ax = ax

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.ax.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

    def do_3d_projection(self, *_, **__):
        return 0


def plot_vector(ax, vector, label, color="black", label_shift=(0, 0, 0)):
    ax.add_artist(
        Arrow3D(
            ax,
            [0, vector[0]],
            [0, vector[1]],
            [0, vector[2]],
            mutation_scale=10,
            arrowstyle="-|>",
            color=color,
            lw=1,
            alpha=0.7,
        )
    )
    ax.text(
        *(np.array(vector) + np.array(label_shift)), label, color=color, fontsize=15
    )


def main(root_directory):
    fig = plt.figure(figsize=(9, 3))
    width = 1 / 3
    right_fix = 1 / 20
    dis = (1 - 3 * width - right_fix) / 6
    limit = 0.6
    axs = []
    titles = ["$\hat{n} = \hat{z}$", "$\hat{n} = -\hat{z}$", "Other"]
    color = "#AE1968"
    for i in range(3):
        axs.append(
            fig.add_axes(
                (i * width + (1 + 2 * i) * dis, 0, width, 0.8), projection="3d"
            )
        )
        plot_vector(
            axs[-1], (1, 0, 0), R"$\hat{x}$" if i != 0 else R"$\hat{x}$, $\hat{u}$"
        )
        plot_vector(
            axs[-1], (0, 1, 0), R"$\hat{y}$" if i != 0 else R"$\hat{y}$, $\hat{v}$"
        )
        plot_vector(
            axs[-1], (0, 0, 1), R"$\hat{z}$" if i != 0 else R"$\hat{z}$, $\hat{n}$"
        )
        axs[-1].set_xlim(-limit, limit)
        axs[-1].set_ylim(-limit, limit)
        axs[-1].set_zlim(-limit, limit)
        axs[-1].set_aspect("equal")
        axs[-1].axis("off")
        axs[-1].set_title(titles[i], fontsize=20, pad=20)

    # Plot v = -y
    plot_vector(axs[1], (0, 0, -1), R"$\hat{n}$", color=color, label_shift=(0, 0, -0.2))
    plot_vector(axs[1], (0, -1, 0), R"$\hat{u}$", color=color, label_shift=(0, -0.4, 0))
    plot_vector(axs[1], (-1, 0, 0), R"$\hat{v}$", color=color, label_shift=(-0.2, 0, 0))

    # Plot example of other cases
    n = np.array([-1, -1, -1], dtype=float)
    n /= np.linalg.norm(n)
    u = np.array((1 - (n[0] ** 2) / (1 + n[2]), -n[0] * n[1] / (1 + n[2]), -n[0]))
    v = np.array(
        (
            -n[0] * n[1] / (1 + n[2]),
            1 - (n[1] ** 2) / (1 + n[2]),
            -n[1],
        )
    )
    print(np.linalg.norm(u), np.linalg.norm(v), np.linalg.norm(n))
    print(u, v, n, sep="\n")
    plot_vector(axs[2], u, R"$\hat{u}$", color=color, label_shift=0.2 * u)
    plot_vector(axs[2], v, R"$\hat{v}$", color=color)
    plot_vector(axs[2], n, R"$\hat{n}$", color=color, label_shift=0.2 * n)
    axs[2].view_init(azim=-45, elev=28)

    plt.savefig(
        os.path.join(root_directory, "docs", "images", "cs-choice.png"), dpi=400
    )
    plt.close()


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
