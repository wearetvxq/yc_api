# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.out_lists import OutLists  # noqa: F401,E501
from swagger_server import util


class OutList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, total: str=None, code: int=None, msg: str=None, result: List[OutLists]=None):  # noqa: E501
        """OutList - a model defined in Swagger

        :param total: The total of this OutList.  # noqa: E501
        :type total: str
        :param code: The code of this OutList.  # noqa: E501
        :type code: int
        :param msg: The msg of this OutList.  # noqa: E501
        :type msg: str
        :param result: The result of this OutList.  # noqa: E501
        :type result: List[OutLists]
        """
        self.swagger_types = {
            'total': str,
            'code': int,
            'msg': str,
            'result': List[OutLists]
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
    def from_dict(cls, dikt) -> 'OutList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OutList of this OutList.  # noqa: E501
        :rtype: OutList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> str:
        """Gets the total of this OutList.

        system return total  # noqa: E501

        :return: The total of this OutList.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total: str):
        """Sets the total of this OutList.

        system return total  # noqa: E501

        :param total: The total of this OutList.
        :type total: str
        """

        self._total = total

    @property
    def code(self) -> int:
        """Gets the code of this OutList.

        system return code  # noqa: E501

        :return: The code of this OutList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this OutList.

        system return code  # noqa: E501

        :param code: The code of this OutList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this OutList.

        system return news  # noqa: E501

        :return: The msg of this OutList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this OutList.

        system return news  # noqa: E501

        :param msg: The msg of this OutList.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[OutLists]:
        """Gets the result of this OutList.


        :return: The result of this OutList.
        :rtype: List[OutLists]
        """
        return self._result

    @result.setter
    def result(self, result: List[OutLists]):
        """Sets the result of this OutList.


        :param result: The result of this OutList.
        :type result: List[OutLists]
        """

        self._result = result