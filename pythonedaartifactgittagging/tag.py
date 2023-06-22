"""
pythonedaartifactgittagging/tag.py

This file declares the Tag class.

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
from pythoneda.entity import Entity
from pythoneda.event import Event
from pythoneda.event_listener import EventListener
from pythoneda.value_object import primary_key_attribute

from pythonedaartifactgittagging.tag_requested import TagRequested

from typing import List, Type

class Tag(Entity, EventListener):
    """
    Represents a tag in the source code.

    Class name: TagRepositoryRequested

    Responsibilities:
        - Represents a tag.
        - Accepts requests to create a tag on the source code.

    Collaborators:
        - TagRequested: The event that triggers the tagging process.
    """

    def __init__(self, name: str):
        """
        Creates a new Tag instance.
        :param name: The tag name.
        :type name: str
        """
        super().__init__()
        self._name = name

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the tag.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @classmethod
    def supported_events(cls) -> List[Type[Event]]:
        """
        Retrieves the list of supported event classes.
        """
        return [ TagRequested ]


    @classmethod
    async def listenTagRequested(cls, event: TagRequested): # -> TagCreated:
        result = None

        print(f'Received {event} !!')
