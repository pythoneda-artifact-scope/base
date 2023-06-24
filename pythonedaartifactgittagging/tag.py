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
from pythoneda.event_emitter import EventEmitter
from pythoneda.event_listener import EventListener
from pythoneda.value_object import primary_key_attribute

from pythonedaartifactgittagging.tag_created import TagCreated
from pythonedaartifactgittagging.tag_requested import TagRequested

from pythonedasharedgit.git_repo import GitRepo
from pythonedasharedgit.version import Version

from typing import List, Type

class Tag(Entity, EventListener, EventEmitter):
    """
    Represents a tag in the source code.

    Class name: Tag

    Responsibilities:
        - Represents a tag.
        - Accepts requests to create a tag on the source code.

    Collaborators:
        - TagRequested: The event that triggers the tagging process.
        - GitRepoFactory: To create GitRepo instances.
    """

    def __init__(self, name: str, gitRepo: GitRepo):
        """
        Creates a new Tag instance.
        :param name: The tag name.
        :type name: str
        :param gitRepo: The git repository.
        :type gitRepo: GitRepo from pythonedasharedgit.git_repo
        """
        super().__init__()
        self._name = name
        self._git_repo = gitRepo

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the tag.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @primary_key_attribute
    def git_repo(self) -> str:
        """
        Retrieves the git repository.
        :return: Such information.
        :rtype: str
        """
        return self._git_repo

    @classmethod
    def supported_events(cls) -> List[Type[Event]]:
        """
        Retrieves the list of supported event classes.
        """
        return [ TagRequested ]


    @classmethod
    async def listenTagRequested(cls, event: TagRequested) -> TagCreated:
        result = None

        print(f'Received {event} !!')

        gitRepo = GitRepoFactory.create(event.repository_url, event.branch)
        tag = Tag("removeme", gitRepo)

        gitRepo.clone()

        gitRepo.increase_build()

        result = TagCreated("dummy", event.repository_url)
        await cls.emit(result)
        return result
