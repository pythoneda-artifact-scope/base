"""
pythonedaartifactgittagging/git_repo_factory.py

This file declares the GitRepoFactory class.

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
from pythoneda.port import Port
from pythonedasharedgit.git_repo import GitRepo

import abc

class GitRepoFactory(Port, abc.ABC):
    """
    A class capable of creating GitRepo instances.

    Class name: GitRepoFactory

    Responsibilities:
        - Builds GitRepo instances.

    Collaborators:
        - None
    """

    @abc.abstractmethod
    def create(self, repositoryUrl: str, head: str) -> GitRepo:
        """
        Creates a GitRepo instance.
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param head: The head to point to.
        :type head: str
        :return: The GitRepo.
        :rtype: GitRepo from pythonedasharedgit.git_repo
        """
        raise NotImplementedError("create(url, head) should be implemented by subclasses")
