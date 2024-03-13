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

from os import listdir, remove, system
from os.path import abspath, basename, isfile, join

import pytest

from magnopy.io.txt.internal import _filter_txt_file, dump_model_txt, load_model_txt

resources_path = join("utests", "test_io", "model-file-examples")

inputs_to_pass = [
    (abspath(join(resources_path, "correct", "txt", f)))
    for f in listdir(join(resources_path, "correct", "txt"))
    if isfile(join(resources_path, "correct", "txt", f))
]


@pytest.mark.parametrize("filename", inputs_to_pass)
def test_load_model(filename):
    model = load_model_txt(filename)


@pytest.mark.parametrize("filename", inputs_to_pass)
def test_dump_model(filename):
    model = load_model_txt(filename)
    tmp_filename = f"tmp-model-test-{basename(filename)}"
    dump_model_txt(model, tmp_filename)
    model = load_model_txt(tmp_filename)
    system(f"rm {tmp_filename}")


def test__filter_txt_file_raises():
    with pytest.raises(ValueError):
        _filter_txt_file("file.txt", lines=[])

    with pytest.raises(ValueError):
        _filter_txt_file()
