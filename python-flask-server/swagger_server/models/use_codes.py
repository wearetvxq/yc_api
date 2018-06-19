# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.use_codess import UseCodess  # noqa: F401,E501
from swagger_server import util


class UseCodes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[UseCodess]=None):  # noqa: E501
        """UseCodes - a model defined in Swagger

        :param code: The code of this UseCodes.  # noqa: E501
        :type code: int
        :param msg: The msg of this UseCodes.  # noqa: E501
        :type msg: str
        :param result: The result of this UseCodes.  # noqa: E501
        :type result: List[UseCodess]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[UseCodess]
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
    def from_dict(cls, dikt) -> 'UseCodes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UseCodes of this UseCodes.  # noqa: E501
        :rtype: UseCodes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this UseCodes.

        system return code  # noqa: E501

        :return: The code of this UseCodes.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this UseCodes.

        system return code  # noqa: E501

        :param code: The code of this UseCodes.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this UseCodes.

        system return news  # noqa: E501

        :return: The msg of this UseCodes.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this UseCodes.

        system return news  # noqa: E501

        :param msg: The msg of this UseCodes.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[UseCodess]:
        """Gets the result of this UseCodes.


        :return: The result of this UseCodes.
        :rtype: List[UseCodess]
        """
        return self._result

    @result.setter
    def result(self, result: List[UseCodess]):
        """Sets the result of this UseCodes.


        :param result: The result of this UseCodes.
        :type result: List[UseCodess]
        """

        self._result = result