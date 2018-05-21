# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.storage_querys import StorageQuerys  # noqa: F401,E501
from swagger_server import util


class StorageQuery(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[StorageQuerys]=None):  # noqa: E501
        """StorageQuery - a model defined in Swagger

        :param code: The code of this StorageQuery.  # noqa: E501
        :type code: int
        :param msg: The msg of this StorageQuery.  # noqa: E501
        :type msg: str
        :param result: The result of this StorageQuery.  # noqa: E501
        :type result: List[StorageQuerys]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[StorageQuerys]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'result': 'result'
        }

        self._code = code
        self._msg = msg
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'StorageQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The storageQuery of this StorageQuery.  # noqa: E501
        :rtype: StorageQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this StorageQuery.

        system return code  # noqa: E501

        :return: The code of this StorageQuery.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this StorageQuery.

        system return code  # noqa: E501

        :param code: The code of this StorageQuery.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this StorageQuery.

        system return news  # noqa: E501

        :return: The msg of this StorageQuery.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this StorageQuery.

        system return news  # noqa: E501

        :param msg: The msg of this StorageQuery.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[StorageQuerys]:
        """Gets the result of this StorageQuery.


        :return: The result of this StorageQuery.
        :rtype: List[StorageQuerys]
        """
        return self._result

    @result.setter
    def result(self, result: List[StorageQuerys]):
        """Sets the result of this StorageQuery.


        :param result: The result of this StorageQuery.
        :type result: List[StorageQuerys]
        """

        self._result = result
