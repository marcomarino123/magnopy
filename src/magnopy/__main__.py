from argparse import ArgumentParser, RawDescriptionHelpFormatter

from magnopy import __version__
from magnopy._pinfo import logo, warranty


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
    args = parser.parse_args()
    if args.command == "logo":
        print(logo())
    elif args.command == "warranty":
        print("\n" + warranty() + "\n")
    elif args.command == "version" or args.version:
        print(f"Magnopy v{__version__}")
    elif args.command is None:
        parser.print_help()
    else:
        raise ValueError(f"Command {args.command} is not recognized.")


if __name__ == "__main__":
    main()
