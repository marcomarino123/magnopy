# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2024 Magnopy Team
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

from os import listdir
from os.path import abspath, basename, isfile, join

import pytest

from magnopy.io.internal import _filter_model_file
from magnopy.io.verify import FailedToVerifyModelFile, _verify_model_file

resources_path = join("utests", "io", "test_magnopy_inputs")

inputs_to_fail = [
    (abspath(join(resources_path, "fail", f)))
    for f in listdir(join(resources_path, "fail"))
    if isfile(join(resources_path, "fail", f))
]
inputs_to_pass = [
    (abspath(join(resources_path, "pass", f)))
    for f in listdir(join(resources_path, "pass"))
    if isfile(join(resources_path, "pass", f))
]


@pytest.mark.parametrize("filename", inputs_to_pass)
def test_verify_model_pass(filename):
    lines, indices = _filter_model_file(filename)
    _verify_model_file(lines, indices)


@pytest.mark.parametrize("filename", inputs_to_fail)
def test_verify_model_fail(filename):
    try:
        lines, indices = _filter_model_file(filename)
        _verify_model_file(lines, indices)
        assert False
    except FailedToVerifyModelFile:
        assert True


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=0)
    print(
        " ".join(
            [
                "This routine allows you to check the logs for each test input file.",
                "You can check:\n ",
                "\n  ".join(
                    [
                        "- all files",
                        "- all files that should fail",
                        "- all files that should pass",
                        "- individual files",
                    ]
                ),
            ]
        )
    )
    failed_or_passed = input('Type "fail" or "pass" or "all" or "individual"\n').lower()
    if failed_or_passed.startswith("f"):
        inputs = inputs_to_fail
    elif failed_or_passed.startswith("p"):
        inputs = inputs_to_pass
    elif failed_or_passed.startswith("a"):
        inputs = inputs_to_pass + inputs_to_fail
    elif failed_or_passed.startswith("i"):
        control_word = ""
        inputs = ["pass/" + basename(f) for f in inputs_to_pass] + [
            "fail/" + basename(f) for f in inputs_to_fail
        ]
        while True:
            control_word = input(
                "\n".join(
                    [
                        "Commands:",
                        '  - "verify <fail or pass>/<name of the file>" to verify the file',
                        '  - "show <fail or pass>/<name of the file>" to show the content of the file',
                        '  - "list" to show available files',
                        '  - "quit" to quit',
                        "",
                    ]
                )
            )
            if control_word.lower().startswith("l"):
                print("Files that supposed to pass:")
                print(
                    "  "
                    + "\n  ".join(
                        sorted(["pass/" + basename(f) for f in inputs_to_pass])
                    )
                )
                print("Files that supposed to fail:")
                print(
                    "  "
                    + "\n  ".join(
                        sorted(["fail/" + basename(f) for f in inputs_to_fail])
                    )
                )
            elif control_word.lower().startswith("q"):
                break
            elif control_word.lower().startswith("v"):
                if control_word.split()[1] in inputs:
                    input_file = join(resources_path, control_word.split()[1])
                    name = f' {control_word.replace("-", " ").split(".")[0]} '
                    print(f"{'':=^80}")
                    print(f"verifying file {input_file}")
                    lines, indices = _filter_model_file(filename=input_file)
                    _verify_model_file(lines, indices, raise_on_fail=False)
                    print(f"{' Done ':=^80}")
                else:
                    print("No such file")
            elif control_word.lower().startswith("s"):
                if control_word.split()[1] in inputs:
                    input_file = join(resources_path, control_word.split()[1])
                    with open(input_file, "r") as file:
                        print(
                            "".join(
                                [
                                    f"{i+1}: {line}"
                                    for i, line in enumerate(file.readlines())
                                ]
                            )
                        )
                else:
                    print("No such file")
        inputs = []
    else:
        print("Unsupported input")
        inputs = []

    for input_file in inputs:
        input_file = input_file
        name = f' {basename(input_file).replace("-", " ").split(".")[0]} '
        print(f"{name:=^80}")
        print(f"verifying file {input_file}")
        lines, indices = _filter_model_file(filename=input_file)
        _verify_model_file(lines, indices, raise_on_fail=False)
        print(f"{' Done, press ENTER for next file ':=^80}")
        input()
