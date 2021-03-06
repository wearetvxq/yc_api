# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NoticeLists(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, type: int=None, posttime: str=None, title: str=None):  # noqa: E501
        """NoticeLists - a model defined in Swagger

        :param id: The id of this NoticeLists.  # noqa: E501
        :type id: int
        :param type: The type of this NoticeLists.  # noqa: E501
        :type type: int
        :param posttime: The posttime of this NoticeLists.  # noqa: E501
        :type posttime: str
        :param title: The title of this NoticeLists.  # noqa: E501
        :type title: str
        """
        self.swagger_types = {
            'id': int,
            'type': int,
            'posttime': str,
            'title': str
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'posttime': 'posttime',
            'title': 'title'
        }

        self._id = id
        self._type = type
        self._posttime = posttime
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'NoticeLists':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NoticeLists of this NoticeLists.  # noqa: E501
        :rtype: NoticeLists
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this NoticeLists.

        notice code  # noqa: E501

        :return: The id of this NoticeLists.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this NoticeLists.

        notice code  # noqa: E501

        :param id: The id of this NoticeLists.
        :type id: int
        """

        self._id = id

    @property
    def type(self) -> int:
        """Gets the type of this NoticeLists.

        notice type  # noqa: E501

        :return: The type of this NoticeLists.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this NoticeLists.

        notice type  # noqa: E501

        :param type: The type of this NoticeLists.
        :type type: int
        """

        self._type = type

    @property
    def posttime(self) -> str:
        """Gets the posttime of this NoticeLists.

        notice posttime  # noqa: E501

        :return: The posttime of this NoticeLists.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this NoticeLists.

        notice posttime  # noqa: E501

        :param posttime: The posttime of this NoticeLists.
        :type posttime: str
        """

        self._posttime = posttime

    @property
    def title(self) -> str:
        """Gets the title of this NoticeLists.

        notice title  # noqa: E501

        :return: The title of this NoticeLists.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this NoticeLists.

        notice title  # noqa: E501

        :param title: The title of this NoticeLists.
        :type title: str
        """

        self._title = title
