# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.waste_lists import WasteLists  # noqa: F401,E501
from swagger_server import util


class WasteList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, total: str=None, code: int=None, msg: str=None, result: List[WasteLists]=None):  # noqa: E501
        """WasteList - a model defined in Swagger

        :param total: The total of this WasteList.  # noqa: E501
        :type total: str
        :param code: The code of this WasteList.  # noqa: E501
        :type code: int
        :param msg: The msg of this WasteList.  # noqa: E501
        :type msg: str
        :param result: The result of this WasteList.  # noqa: E501
        :type result: List[WasteLists]
        """
        self.swagger_types = {
            'total': str,
            'code': int,
            'msg': str,
            'result': List[WasteLists]
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
    def from_dict(cls, dikt) -> 'WasteList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WasteList of this WasteList.  # noqa: E501
        :rtype: WasteList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> str:
        """Gets the total of this WasteList.

        system return total  # noqa: E501

        :return: The total of this WasteList.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total: str):
        """Sets the total of this WasteList.

        system return total  # noqa: E501

        :param total: The total of this WasteList.
        :type total: str
        """

        self._total = total

    @property
    def code(self) -> int:
        """Gets the code of this WasteList.

        system return code  # noqa: E501

        :return: The code of this WasteList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this WasteList.

        system return code  # noqa: E501

        :param code: The code of this WasteList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this WasteList.

        system return news  # noqa: E501

        :return: The msg of this WasteList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this WasteList.

        system return news  # noqa: E501

        :param msg: The msg of this WasteList.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[WasteLists]:
        """Gets the result of this WasteList.


        :return: The result of this WasteList.
        :rtype: List[WasteLists]
        """
        return self._result

    @result.setter
    def result(self, result: List[WasteLists]):
        """Sets the result of this WasteList.


        :param result: The result of this WasteList.
        :type result: List[WasteLists]
        """

        self._result = result
