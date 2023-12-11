import sys


def _winwait():
    r"""
    Add "Press Enter to continue" behavior to Windows.

    Its a hotfix for Window`s terminal behavior.
    """
    if sys.platform == "win32":
        input("Press Enter to continue")
