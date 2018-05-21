# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NetworkListResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, area: str=None, name: str=None, total: str=None):  # noqa: E501
        """NetworkListResult - a model defined in Swagger

        :param id: The id of this NetworkListResult.  # noqa: E501
        :type id: int
        :param area: The area of this NetworkListResult.  # noqa: E501
        :type area: str
        :param name: The name of this NetworkListResult.  # noqa: E501
        :type name: str
        :param total: The total of this NetworkListResult.  # noqa: E501
        :type total: str
        """
        self.swagger_types = {
            'id': int,
            'area': str,
            'name': str,
            'total': str
        }

        self.attribute_map = {
            'id': 'id',
            'area': 'area',
            'name': 'name',
            'total': 'total'
        }

        self._id = id
        self._area = area
        self._name = name
        self._total = total

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NetworkListResult of this NetworkListResult.  # noqa: E501
        :rtype: NetworkListResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this NetworkListResult.

        ID  # noqa: E501

        :return: The id of this NetworkListResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this NetworkListResult.

        ID  # noqa: E501

        :param id: The id of this NetworkListResult.
        :type id: int
        """

        self._id = id

    @property
    def area(self) -> str:
        """Gets the area of this NetworkListResult.

        area  # noqa: E501

        :return: The area of this NetworkListResult.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area: str):
        """Sets the area of this NetworkListResult.

        area  # noqa: E501

        :param area: The area of this NetworkListResult.
        :type area: str
        """

        self._area = area

    @property
    def name(self) -> str:
        """Gets the name of this NetworkListResult.

        Network element name  # noqa: E501

        :return: The name of this NetworkListResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this NetworkListResult.

        Network element name  # noqa: E501

        :param name: The name of this NetworkListResult.
        :type name: str
        """

        self._name = name

    @property
    def total(self) -> str:
        """Gets the total of this NetworkListResult.

        total  # noqa: E501

        :return: The total of this NetworkListResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total: str):
        """Sets the total of this NetworkListResult.

        total  # noqa: E501

        :param total: The total of this NetworkListResult.
        :type total: str
        """

        self._total = total