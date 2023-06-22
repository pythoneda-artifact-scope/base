"""
tests/tag_tests.py

This script contains tests for pythonedaartifactgittagging/tag.py

Copyright (C) 2023-today rydnr's PythonEDA Artifact Git Tagging

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
from pathlib import Path

base_folder = str(Path(__file__).resolve().parent.parent)
if base_folder not in sys.path:
    sys.path.append(base_folder)

from pythonedaartifactgittagging.tag import Tag
from pythonedaartifactgittagging.tag_created import TagCreated
from pythonedaartifactgittagging.tag_requested import TagRequested

import asyncio
import pytest
import re
import unittest

class TagTests(unittest.IsolatedAsyncioTestCase):
    """
    Defines tests for pythonedaartifactgittagging/tag.py.

    Class name: TagTests

    Responsibilities:
        - Validates the functionality of the Tag class.

    Collaborators:
        - Tag: Some sample instances of a derived class are used in the tests.
    """

    async def test_listenTagRequested(self):
        """
        Tests the behavior of listTagRequested(event).
        """
        # given
        input = TagRequested("https://github.com/pythoneda-artifact/git-tagging", "main")

        # when
        result = await Tag.listenTagRequested(input)

        # then
        assert result is not None
        assert type(result) == TagCreated

    def check_tag_exists(self, repository: str, tag: str) -> bool:
        """
        Checks if given tag exists.
        :param repositoryUrl: The url of the git repository.
        :type repositoryUrl: str
        :param tag: The tag.
        :type tag: str
        :return: True in such case.
        :rtype: bool
        """

if __name__ == '__main__':
    unittest.main()
