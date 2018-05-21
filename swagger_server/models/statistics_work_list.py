# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.statistics_work_lists import StatisticsWorkLists  # noqa: F401,E501
from swagger_server import util


class StatisticsWorkList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[StatisticsWorkLists]=None):  # noqa: E501
        """StatisticsWorkList - a model defined in Swagger

        :param code: The code of this StatisticsWorkList.  # noqa: E501
        :type code: int
        :param msg: The msg of this StatisticsWorkList.  # noqa: E501
        :type msg: str
        :param result: The result of this StatisticsWorkList.  # noqa: E501
        :type result: List[StatisticsWorkLists]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[StatisticsWorkLists]
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
    def from_dict(cls, dikt) -> 'StatisticsWorkList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatisticsWorkList of this StatisticsWorkList.  # noqa: E501
        :rtype: StatisticsWorkList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this StatisticsWorkList.

        system return code  # noqa: E501

        :return: The code of this StatisticsWorkList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this StatisticsWorkList.

        system return code  # noqa: E501

        :param code: The code of this StatisticsWorkList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this StatisticsWorkList.

        system return news  # noqa: E501

        :return: The msg of this StatisticsWorkList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this StatisticsWorkList.

        system return news  # noqa: E501

        :param msg: The msg of this StatisticsWorkList.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[StatisticsWorkLists]:
        """Gets the result of this StatisticsWorkList.


        :return: The result of this StatisticsWorkList.
        :rtype: List[StatisticsWorkLists]
        """
        return self._result

    @result.setter
    def result(self, result: List[StatisticsWorkLists]):
        """Sets the result of this StatisticsWorkList.


        :param result: The result of this StatisticsWorkList.
        :type result: List[StatisticsWorkLists]
        """

        self._result = result