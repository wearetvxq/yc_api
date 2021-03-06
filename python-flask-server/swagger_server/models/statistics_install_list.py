# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.statistics_install_lists import StatisticsInstallLists  # noqa: F401,E501
from swagger_server import util


class StatisticsInstallList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[StatisticsInstallLists]=None):  # noqa: E501
        """StatisticsInstallList - a model defined in Swagger

        :param code: The code of this StatisticsInstallList.  # noqa: E501
        :type code: int
        :param msg: The msg of this StatisticsInstallList.  # noqa: E501
        :type msg: str
        :param result: The result of this StatisticsInstallList.  # noqa: E501
        :type result: List[StatisticsInstallLists]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[StatisticsInstallLists]
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
    def from_dict(cls, dikt) -> 'StatisticsInstallList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatisticsInstallList of this StatisticsInstallList.  # noqa: E501
        :rtype: StatisticsInstallList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this StatisticsInstallList.

        system return code  # noqa: E501

        :return: The code of this StatisticsInstallList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this StatisticsInstallList.

        system return code  # noqa: E501

        :param code: The code of this StatisticsInstallList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this StatisticsInstallList.

        system return news  # noqa: E501

        :return: The msg of this StatisticsInstallList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this StatisticsInstallList.

        system return news  # noqa: E501

        :param msg: The msg of this StatisticsInstallList.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[StatisticsInstallLists]:
        """Gets the result of this StatisticsInstallList.


        :return: The result of this StatisticsInstallList.
        :rtype: List[StatisticsInstallLists]
        """
        return self._result

    @result.setter
    def result(self, result: List[StatisticsInstallLists]):
        """Sets the result of this StatisticsInstallList.


        :param result: The result of this StatisticsInstallList.
        :type result: List[StatisticsInstallLists]
        """

        self._result = result
