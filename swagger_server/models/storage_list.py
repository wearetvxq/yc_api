# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.storage_lists import StorageLists  # noqa: F401,E501
from swagger_server import util


class StorageList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, total: str=None, code: int=None, msg: str=None, result: List[StorageLists]=None):  # noqa: E501
        """StorageList - a model defined in Swagger

        :param total: The total of this StorageList.  # noqa: E501
        :type total: str
        :param code: The code of this StorageList.  # noqa: E501
        :type code: int
        :param msg: The msg of this StorageList.  # noqa: E501
        :type msg: str
        :param result: The result of this StorageList.  # noqa: E501
        :type result: List[StorageLists]
        """
        self.swagger_types = {
            'total': str,
            'code': int,
            'msg': str,
            'result': List[StorageLists]
        }

        self.attribute_map = {
            'total': 'total',
            'code': 'code',
            'msg': 'msg',
            'result': 'result'
        }

        self._total = total
        self._code = code
        self._msg = msg
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'StorageList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The storageList of this StorageList.  # noqa: E501
        :rtype: StorageList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> str:
        """Gets the total of this StorageList.

        system return total  # noqa: E501

        :return: The total of this StorageList.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total: str):
        """Sets the total of this StorageList.

        system return total  # noqa: E501

        :param total: The total of this StorageList.
        :type total: str
        """

        self._total = total

    @property
    def code(self) -> int:
        """Gets the code of this StorageList.

        system return code  # noqa: E501

        :return: The code of this StorageList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this StorageList.

        system return code  # noqa: E501

        :param code: The code of this StorageList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this StorageList.

        system return news  # noqa: E501

        :return: The msg of this StorageList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this StorageList.

        system return news  # noqa: E501

        :param msg: The msg of this StorageList.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[StorageLists]:
        """Gets the result of this StorageList.


        :return: The result of this StorageList.
        :rtype: List[StorageLists]
        """
        return self._result

    @result.setter
    def result(self, result: List[StorageLists]):
        """Sets the result of this StorageList.


        :param result: The result of this StorageList.
        :type result: List[StorageLists]
        """

        self._result = result
