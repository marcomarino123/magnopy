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


from argparse import ArgumentParser, RawDescriptionHelpFormatter

from magnopy import __git_commit__, __version__
from magnopy._pinfo import conditions, logo, warranty


def main():
    parser = ArgumentParser(
        description=logo(),
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "command",
        default=None,
        help="Which command to run",
        choices=["logo", "warranty", "version"],
        nargs="?",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Print version",
    )
    parser.add_argument(
        "-gc",
        "--git-commit",
        action="store_true",
        help="Print the git commit hash of the current version",
    )
    args = parser.parse_args()
    if args.command == "logo":
        print(logo())
    elif args.command == "warranty":
        print("\n" + warranty() + "\n")
    elif args.command == "version" or args.version:
        print(f"Magnopy v{__version__}")
    elif args.git_commit:
        print(f"Git commit hash: {__git_commit__}")
    elif args.command is None:
        parser.print_help()
    else:
        raise ValueError(f"Command {args.command} is not recognized.")


if __name__ == "__main__":
    main()
