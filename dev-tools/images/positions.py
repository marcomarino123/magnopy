# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2025 Magnopy Team
#
# e-mail: anry@uv.es, web: magnopy.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
from argparse import ArgumentParser
from math import atan, pi

import matplotlib.pyplot as plt
import numpy as np


def arrow_with_text(ax, origin, target, text, shift=(0, 0), color="black"):
    shift = np.array(shift)
    origin = np.array(origin)
    target = np.array(target)
    arrow_style = dict(
        angles="xy",
        scale_units="xy",
        scale=1,
        width=0.003,
        headlength=8,
        headwidth=3,
        headaxislength=7,
    )
    ax.quiver(*origin, *(target - origin), **arrow_style, color=color, zorder=3)
    ax.text(
        *((origin + target) / 2 + shift),
        text,
        ha="center",
        va="center",
        fontsize=13,
        color=color,
    )


def plot_origin_point(ax, x, y):
    ax.scatter(x, y, color="black", s=40)
    ax.text(
        x,
        y,
        "\nReference\npoint",
        color="black",
        zorder=1,
        ha="center",
        va="top",
        fontsize=13,
    )


def prepare_fig_ax():
    fig, ax = plt.subplots(figsize=(18, 5))

    # ax.vlines([i for i in range(18)], 0, 5, lw=1, color="Grey", alpha=0.7, zorder=0)
    # ax.hlines([i for i in range(5)], 0, 18, lw=1, color="Grey", alpha=0.7, zorder=0)

    # Unit cell borders
    ax.vlines([0, 6, 12, 18], 0, 5, lw=2, color="Grey", alpha=0.7, zorder=0)
    ax.hlines([0, 5], 0, 18, lw=2, color="Grey", alpha=0.7, zorder=0)
    ax.text(0.1, 4.9, R"Unit cell index $\mu-\nu$", ha="left", va="top")
    ax.text(6.1, 4.9, R"Unit cell index $\mu$", ha="left", va="top")
    ax.text(12.1, 4.9, R"Unit cell index $\mu+\nu$", ha="left", va="top")

    # Reference frame
    origin = np.array((8, -2))
    plot_origin_point(ax, *origin)

    arrow_style = dict(
        angles="xy",
        scale_units="xy",
        scale=1,
        width=0.004,
        headlength=4,
        headaxislength=3.7,
    )

    # Magnetic sites legend
    x = 15
    y = -3
    ax.quiver(
        x,
        y + 1,
        0,
        0.5,
        **arrow_style,
        color="tab:blue",
        zorder=4,
    )
    ax.text(
        x + 0.2,
        y + 1.25,
        R"- site index $\alpha$",
        color="black",
        zorder=4,
        ha="left",
        va="center",
    )
    ax.quiver(
        x,
        y,
        0,
        0.5,
        **arrow_style,
        color="tab:orange",
        zorder=4,
    )
    ax.text(
        x + 0.2,
        y + 0.25,
        R"- site index $\beta$",
        color="black",
        zorder=4,
        ha="left",
        va="center",
    )

    # Magnetic sites
    site_1 = [1, 4]
    site_2 = [5, 1]
    sites = []

    for i in range(3):
        for j in range(1):
            sites.append(np.array((site_1[0] + i * 6, site_1[1] + j * 5)))
            ax.quiver(
                sites[-1][0],
                sites[-1][1] - 0.15,
                0,
                0.5,
                **arrow_style,
                color="tab:blue",
                zorder=4,
            )

            sites.append(np.array((site_2[0] + i * 6, site_2[1] + j * 5)))
            ax.quiver(
                sites[-1][0],
                sites[-1][1] - 0.15,
                0,
                0.5,
                **arrow_style,
                color="tab:orange",
                zorder=4,
            )

    return origin, sites, fig, ax


def plot_unit_cells(root_directory):
    origin, sites, fig, ax = prepare_fig_ax()

    # Unit cells
    arrow_with_text(
        ax,
        origin,
        (0, 0),
        R"$\boldsymbol{r}_{\mu - \nu}$",
        shift=(-0.3, -0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        (6, 0),
        R"$\boldsymbol{r}_{\mu}$",
        shift=(0.4, 0),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        (12, 0),
        R"$\boldsymbol{r}_{\mu+\nu}$",
        shift=(-0.4, 0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        (18, 0),
        R"$\boldsymbol{r}_{\mu+2\nu}$",
        shift=(0.4, -0.3),
        color="black",
    )

    # Between unit cells
    arrow_with_text(
        ax,
        (6, 0.5),
        (12, 0.5),
        R"$\boldsymbol{r}_{\nu}$",
        shift=(0, 0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        (6, 1.5),
        (0, 1.5),
        R"$\boldsymbol{r}_{-\nu}$",
        shift=(0, 0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        (6, 2.5),
        (18, 2.5),
        R"$\boldsymbol{r}_{2\nu}$",
        shift=(-0.5, 0.3),
        color="black",
    )

    ax.axis("off")
    ax.set_aspect(1)
    filename = os.path.join(
        root_directory,
        "docs",
        "images",
        "positions_unit-cells.png",
    )
    fig.savefig(filename, dpi=600, bbox_inches="tight")
    print(f"File is saved in {os.path.abspath(filename)}")
    plt.close()


def plot_sites(root_directory):
    origin, sites, fig, ax = prepare_fig_ax()

    # Sites from origin
    arrow_with_text(
        ax,
        origin,
        sites[0],
        R"$\boldsymbol{r}_{\mu - \nu, \alpha}$",
        shift=(-0.9, 1.5),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        sites[1],
        R"$\boldsymbol{r}_{\mu - \nu, \beta}$",
        shift=(0.6, 0.2),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        sites[2],
        R"$\boldsymbol{r}_{\mu, \alpha}$",
        shift=(0.3, 1),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        sites[3],
        R"$\boldsymbol{r}_{\mu, \beta}$",
        shift=(0.5, -0.1),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        sites[4],
        R"$\boldsymbol{r}_{\mu+\nu, \alpha}$",
        shift=(0.3, 1.5),
        color="black",
    )
    arrow_with_text(
        ax,
        origin,
        sites[5],
        R"$\boldsymbol{r}_{\mu+\nu, \beta}$",
        shift=(0, -0.5),
        color="black",
    )

    # Sites from unit cells
    arrow_with_text(
        ax,
        (0, 0),
        sites[0],
        R"$\boldsymbol{r}_{\alpha}$",
        shift=(-0.2, 0.5),
        color="black",
    )
    arrow_with_text(
        ax,
        (6, 0),
        sites[2],
        R"$\boldsymbol{r}_{\alpha}$",
        shift=(-0.2, 0.5),
        color="black",
    )
    arrow_with_text(
        ax,
        (12, 0),
        sites[4],
        R"$\boldsymbol{r}_{\alpha}$",
        shift=(0.4, 0.5),
        color="black",
    )
    arrow_with_text(
        ax,
        (0, 0),
        sites[1],
        R"$\boldsymbol{r}_{\beta}$",
        shift=(0, 0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        (6, 0),
        sites[3],
        R"$\boldsymbol{r}_{\beta}$",
        shift=(0, 0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        (12, 0),
        sites[5],
        R"$\boldsymbol{r}_{\beta}$",
        shift=(0, 0.3),
        color="black",
    )

    # Between sites

    ax.axis("off")
    ax.set_aspect(1)
    filename = os.path.join(
        root_directory,
        "docs",
        "images",
        "positions_sites.png",
    )
    fig.savefig(filename, dpi=600, bbox_inches="tight")
    print(f"File is saved in {os.path.abspath(filename)}")
    plt.close()


def plot_between_sites(root_directory):
    origin, sites, fig, ax = prepare_fig_ax()

    # From alpha
    arrow_with_text(
        ax,
        sites[2],
        sites[3],
        R"$\boldsymbol{r}_{0, \alpha\beta}$",
        shift=(1, -0.2),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[2],
        sites[5],
        R"$\boldsymbol{r}_{\nu, \alpha\beta}$",
        shift=(3, -0.5),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[2],
        sites[1],
        R"$\boldsymbol{r}_{-\nu, \alpha\beta}$",
        shift=(-1.2, -0.7),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[2],
        sites[4],
        R"$\boldsymbol{r}_{\nu, \alpha\alpha}$",
        shift=(0, 0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[2],
        sites[0],
        R"$\boldsymbol{r}_{-\nu, \alpha\alpha}$",
        shift=(0, 0.3),
        color="black",
    )

    # From beta

    arrow_with_text(
        ax,
        sites[3],
        sites[2],
        R"$\boldsymbol{r}_{0, \beta\alpha}$",
        shift=(-1, 0.2),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[3],
        sites[4],
        R"$\boldsymbol{r}_{\nu, \beta\alpha}$",
        shift=(1.2, 0.7),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[3],
        sites[0],
        R"$\boldsymbol{r}_{-\nu, \beta\alpha}$",
        shift=(-3, 0.5),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[3],
        sites[5],
        R"$\boldsymbol{r}_{\nu, \beta\beta}$",
        shift=(0, -0.3),
        color="black",
    )
    arrow_with_text(
        ax,
        sites[3],
        sites[1],
        R"$\boldsymbol{r}_{-\nu, \beta\beta}$",
        shift=(0, -0.3),
        color="black",
    )

    ax.axis("off")
    ax.set_aspect(1)
    filename = os.path.join(
        root_directory,
        "docs",
        "images",
        "positions_between-sites.png",
    )
    fig.savefig(filename, dpi=600, bbox_inches="tight")
    print(f"File is saved in {os.path.abspath(filename)}")
    plt.close()


def main(root_directory):
    plot_unit_cells(root_directory)
    plot_sites(root_directory)
    plot_between_sites(root_directory)


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
