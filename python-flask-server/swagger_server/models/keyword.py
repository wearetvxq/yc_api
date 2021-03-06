# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.keyword1 import Keyword1  # noqa: F401,E501
from swagger_server import util


class Keyword(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[Keyword1]=None):  # noqa: E501
        """Keyword - a model defined in Swagger

        :param code: The code of this Keyword.  # noqa: E501
        :type code: int
        :param msg: The msg of this Keyword.  # noqa: E501
        :type msg: str
        :param result: The result of this Keyword.  # noqa: E501
        :type result: List[Keyword1]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[Keyword1]
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
    def from_dict(cls, dikt) -> 'Keyword':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The keyword of this Keyword.  # noqa: E501
        :rtype: Keyword
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this Keyword.

        status  # noqa: E501

        :return: The code of this Keyword.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this Keyword.

        status  # noqa: E501

        :param code: The code of this Keyword.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this Keyword.

        msg  # noqa: E501

        :return: The msg of this Keyword.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this Keyword.

        msg  # noqa: E501

        :param msg: The msg of this Keyword.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[Keyword1]:
        """Gets the result of this Keyword.

        msg for msg  # noqa: E501

        :return: The result of this Keyword.
        :rtype: List[Keyword1]
        """
        return self._result

    @result.setter
    def result(self, result: List[Keyword1]):
        """Sets the result of this Keyword.

        msg for msg  # noqa: E501

        :param result: The result of this Keyword.
        :type result: List[Keyword1]
        """

        self._result = result
