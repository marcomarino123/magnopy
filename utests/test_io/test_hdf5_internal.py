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

from os import listdir, remove
from os.path import abspath, basename, isfile, join

import pytest

from magnopy.io.hdf5.internal import dump_spinham_hdf5
from magnopy.io.txt.internal import load_spinham_txt

resources_path = join("utests", "test_io", "model-file-examples")

correct_txt_inputs = [
    (abspath(join(resources_path, "correct", "txt", f)))
    for f in listdir(join(resources_path, "correct", "txt"))
    if isfile(join(resources_path, "correct", "txt", f))
]


@pytest.mark.parametrize("filename", correct_txt_inputs)
def test_dump_spinham_hdf5(filename):
    model = load_spinham_txt(filename)
    tmp_filename = f"tmp-test-{basename(filename).split('.')[0]}.hdf5"

    # Ensure that there is no file with the same name and data
    if isfile(tmp_filename):
        remove(tmp_filename)
    # Check that it writes with no problem
    dump_spinham_hdf5(model, filename=tmp_filename)
    # Check that it raises an error if the file already exists with the same group in it
    with pytest.raises(FileExistsError):
        dump_spinham_hdf5(model, filename=tmp_filename)
    # Check that it can overwrite without errors
    dump_spinham_hdf5(model, filename=tmp_filename, overwrite=True)
    # Clean the mess
    remove(tmp_filename)
