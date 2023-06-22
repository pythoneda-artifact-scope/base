"""
pythonedaartifact/tag_requested.py

This file declares the TagRequested event.

Copyright (C) 2023-today rydnr's pythoneda-artifact/base

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
from pythoneda.event import Event
from pythoneda.value_object import primary_key_attribute


class TagRequested(Event):
    """
    Represents the request for tagging a repository.

    Class name: TagRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """
    def __init__(self, repositoryUrl: str):
        """
        Creates a new TagRequested instance.
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        """
        super().__init__()
        self._repository_url = repositoryUrl

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository to tag.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url
