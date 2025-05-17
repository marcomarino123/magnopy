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


import sys
from datetime import datetime
from os.path import abspath, join

sys.path.insert(0, abspath(join("..", "..")))

from magnopy import __release_date__ as release_date
from magnopy import __version__ as version

##########################################################################################
##                                   Project metadata                                   ##
##########################################################################################
project = "magnopy"
copyright = f"2023-{datetime.now().year}, Magnopy Team"
author = "Magnopy"
if ".dev" in version:
    switcher_version = "dev"
    github_version = "dev"
else:
    major, minor, rest = version.split(".")[0:3]
    switcher_version = f"{major}.{minor}"
    github_version = "main"

##########################################################################################
##                                      Extensions                                      ##
##########################################################################################
extensions = [
    "sphinx.ext.duration",  # Measure the time of the build
    "sphinx.ext.autodoc",  # Pull documentation from the docstrings
    "sphinx.ext.autosummary",  # Generate autodoc summaries
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.extlinks",  # Markup to shorten external links
    "sphinx.ext.mathjax",  # For latex-style math
    "sphinx.ext.doctest",  # For the doctests
    "sphinx_copybutton",  # Copybutton for the blocks
    "numpydoc",  # For the numpy-style docstrings
    "sphinx_design",  # For the design elements on the from page
    "sphinx.ext.intersphinx",  # Link to other projects
]

##########################################################################################
##                                  Intersphinx mapping                                 ##
##########################################################################################
intersphinx_mapping = {
    "wulfric": ("https://docs.wulfric.org/en/latest/", None),
}

##########################################################################################
##                                  Build configuration                                 ##
##########################################################################################
autosummary_generate = True
autodoc_member_order = "alphabetical"
smartquotes = False

# Avoid double generating the entries for the members of the class
numpydoc_class_members_toctree = False

# Fix problem with autosummary and numpydoc:
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

##########################################################################################
##                                Options for HTML output                               ##
##########################################################################################

htmlhelp_basename = "magnopy"
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["magnopy.css"]

html_title = f"{project} {version}"
# html_favicon = "img/favicon.png"

# Theme-specific options
html_theme_options = {
    "collapse_navigation": True,
    "use_edit_page_button": True,
    "navbar_center": ["version-switcher", "navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "switcher": {
    #     "version_match": switcher_version,
    #     "json_url": "https://magnopy.org/en/stable/_static/versions.json",
    # },
    "navbar_align": "left",
    # Add logo later
    # "logo": {
    #     "image_light": "_static/logo_black.png",
    #     "image_dark": "_static/logo_white.png",
    # },
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/magnopy/magnopy",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/magnopy/",
            "icon": "fa-solid fa-box",
        },
    ],
}

html_context = {
    "default_mode": "light",
    "display_github": True,  # Integrate GitHub
    "github_user": "magnopy",  # Username
    "github_repo": "magnopy",  # Repo name
    "github_version": github_version,  # Version
    "doc_path": "docs/source",  # Path in the checkout to the docs root
}


##########################################################################################
##              Custom variables with access from .rst files and docstrings             ##
##########################################################################################

# Custom variables with access from .rst files and docstrings
variables_to_export = [
    "project",
    "copyright",
    "version",
    "release_date",
]

frozen_locals = dict(locals())
rst_epilog = "\n".join(
    map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export)
)
del frozen_locals

# Dynamic external links
# Usage :issue:`123`
extlinks = {
    "DOI": ("https://doi.org/%s", "DOI: %s"),
    "issue": ("https://github.com/magnopy/magnopy/issues/%s", "issue #%s"),
    "numpy": (
        "https://numpy.org/doc/stable/reference/generated/numpy.%s.html",
        "numpy.%s",
    ),
}

# Static external links
# Solution source:
# https://docutils.sourceforge.io/docs/ref/rst/directives.html#directives-for-substitution-definitions
# Usage: |Python|_
custom_links = {
    "Python": ("Python", "https://python.org"),
    "NumPy": ("NumPy", "https://numpy.org/"),
    "SciPy": ("SciPy", "https://scipy.org/"),
    "matplotlib": ("matplotlib", "https://matplotlib.org/"),
    "tqdm": ("tqdm", "https://tqdm.github.io/"),
    "termcolor": ("termcolor", "https://pypi.org/project/termcolor/"),
    "array-like": (
        "array-like",
        "https://numpy.org/doc/stable/glossary.html#term-array_like",
    ),
    "Python-installation": (
        "Python installation",
        "https://wiki.python.org/moin/BeginnersGuide/Download",
    ),
    "NO_COLOR": ("NO_COLOR", "https://no-color.org/"),
    "GitHub": ("GitHub", "https://github.com"),
    "Git": ("Git", "https://git-scm.com/"),
    "Git-remote": (
        "remote",
        "https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes",
    ),
    "Git-repository": (
        "repository",
        "https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository",
    ),
    "repository": ("Magnopy repository", "https://github.com/magnopy/magnopy"),
    "HP-ref": (
        "DOI: 10.1103/PhysRev.58.1098",
        "https://doi.org/10.1103/PhysRev.58.1098",
    ),
    "UTF-8": ("utf-8", "https://en.wikipedia.org/wiki/UTF-8"),
    "PearsonSymbol": ("Pearson symbol", "https://en.wikipedia.org/wiki/Pearson_symbol"),
    "TB2J": ("TB2J", "https://tb2j.readthedocs.io/en/latest/"),
    "Vampire": ("Vampire", "https://vampire.york.ac.uk/"),
    "Wulfric": ("wulfric", "https://docs.wulfric.org/en/latest/"),
    "Wulfric-Bravais-lattices": (
        "Bravais lattices",
        "https://docs.wulfric.org/en/latest/user-guide/conventions/bravais-lattices/index.html",
    ),
    "myHDF5": ("myHDF5", "https://myhdf5.hdfgroup.org/"),
    "POSCAR": ("POSCAR", "https://www.vasp.at/wiki/index.php/POSCAR"),
    "h5py": ("h5py", "https://www.h5py.org/"),
    "sphinx": ("Sphinx", "https://www.sphinx-doc.org/en/master/"),
    "sphinx-autodoc": (
        "sphinx.ext.autodoc",
        "https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html",
    ),
    "sphinx-autosummary": (
        "sphinx.ext.autosummary",
        "https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html",
    ),
    "numpydoc": ("numpydoc", "https://numpydoc.readthedocs.io/en/latest/format.html"),
    "pytest": ("pytest", "https://docs.pytest.org/en/7.3.x/"),
    "hypothesis": ("hypothesis", "https://hypothesis.readthedocs.io/en/latest/"),
    "doctest": (
        "sphinx.ext.doctest",
        "https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html",
    ),
    "good-commit-messages": ("good commit messages", "https://cbea.ms/git-commit/"),
    "reStructuredText": (
        "reStructuredText",
        "https://docutils.sourceforge.io/rst.html",
    ),
    "GNU-make": ("GNU make", "https://www.gnu.org/software/make/manual/make.html"),
    "Fork-and-pull": (
        "Fork and pull",
        "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models#fork-and-pull-model",
    ),
    "venv": ("venv", "https://docs.python.org/3/library/venv.html"),
    "PYPI": ("Python package index", "https://pypi.org/"),
}
rst_epilog += "\n".join(
    map(
        lambda x: f"\n.. |{x}| replace:: {custom_links[x][0]}\n.. _{x}: {custom_links[x][1]}",
        [i for i in custom_links],
    )
)

###########
## Jaime ##
###########
mathjax3_config = {
    "loader": {"load": ["[tex]/physics"]},
    "tex": {"packages": {"[+]": ["physics"]}},
}
