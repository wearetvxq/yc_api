# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.supplies_query_info import SuppliesQueryInfo  # noqa: F401,E501
from swagger_server import util


class SuppliesQuerys(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, model: str=None, code: str=None, info: List[SuppliesQueryInfo]=None):  # noqa: E501
        """SuppliesQuerys - a model defined in Swagger

        :param type: The type of this SuppliesQuerys.  # noqa: E501
        :type type: str
        :param model: The model of this SuppliesQuerys.  # noqa: E501
        :type model: str
        :param code: The code of this SuppliesQuerys.  # noqa: E501
        :type code: str
        :param info: The info of this SuppliesQuerys.  # noqa: E501
        :type info: List[SuppliesQueryInfo]
        """
        self.swagger_types = {
            'type': str,
            'model': str,
            'code': str,
            'info': List[SuppliesQueryInfo]
        }

        self.attribute_map = {
            'type': 'type',
            'model': 'model',
            'code': 'code',
            'info': 'info'
        }

        self._type = type
        self._model = model
        self._code = code
        self._info = info

    @classmethod
    def from_dict(cls, dikt) -> 'SuppliesQuerys':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuppliesQuerys of this SuppliesQuerys.  # noqa: E501
        :rtype: SuppliesQuerys
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this SuppliesQuerys.

        type  # noqa: E501

        :return: The type of this SuppliesQuerys.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this SuppliesQuerys.

        type  # noqa: E501

        :param type: The type of this SuppliesQuerys.
        :type type: str
        """

        self._type = type

    @property
    def model(self) -> str:
        """Gets the model of this SuppliesQuerys.

        model  # noqa: E501

        :return: The model of this SuppliesQuerys.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this SuppliesQuerys.

        model  # noqa: E501

        :param model: The model of this SuppliesQuerys.
        :type model: str
        """

        self._model = model

    @property
    def code(self) -> str:
        """Gets the code of this SuppliesQuerys.

        Bar code  # noqa: E501

        :return: The code of this SuppliesQuerys.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this SuppliesQuerys.

        Bar code  # noqa: E501

        :param code: The code of this SuppliesQuerys.
        :type code: str
        """

        self._code = code

    @property
    def info(self) -> List[SuppliesQueryInfo]:
        """Gets the info of this SuppliesQuerys.


        :return: The info of this SuppliesQuerys.
        :rtype: List[SuppliesQueryInfo]
        """
        return self._info

    @info.setter
    def info(self, info: List[SuppliesQueryInfo]):
        """Sets the info of this SuppliesQuerys.


        :param info: The info of this SuppliesQuerys.
        :type info: List[SuppliesQueryInfo]
        """

        self._info = info
