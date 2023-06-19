"""
pythonedaartifact/tag_repository_requested.py

This file declares the TagRepositoryRequested event.

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


class TagRepositoryRequested(Event):
    """
    Represents the request for tagging a repository.

    Class name: TagRepositoryRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """
    def __init__(self, repositoryUrl: str):
        """
        Creates a new TagRepositoryRequested instance.
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        """
        super().__init()__
        self._repository_url = repositoryUrl

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository to tag.
        :return: Such url.
        :rtype: str
        """
        return sef._repository_url
