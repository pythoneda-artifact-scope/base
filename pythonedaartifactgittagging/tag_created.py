"""
pythonedaartifactgittagging/tag_created.py

This file declares the TagCreated event.

Copyright (C) 2023-today rydnr's pythoneda-artifact/git-tagging

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


class TagCreated(Event):
    """
    Represents the moment a new tag has been created.

    Class name: TagCreated

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self, name: str, repositoryUrl: str):
        """
        Creates a new TagCreated instance.
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        """
        super().__init__()
        self._name = name
        self._repository_url = repositoryUrl

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the tag name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository to tag.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url
