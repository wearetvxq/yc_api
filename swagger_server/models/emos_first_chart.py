# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.emos_first_charts import EmosFirstCharts  # noqa: F401,E501
from swagger_server import util


class EmosFirstChart(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[EmosFirstCharts]=None):  # noqa: E501
        """EmosFirstChart - a model defined in Swagger

        :param code: The code of this EmosFirstChart.  # noqa: E501
        :type code: int
        :param msg: The msg of this EmosFirstChart.  # noqa: E501
        :type msg: str
        :param result: The result of this EmosFirstChart.  # noqa: E501
        :type result: List[EmosFirstCharts]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[EmosFirstCharts]
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
    def from_dict(cls, dikt) -> 'EmosFirstChart':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmosFirstChart of this EmosFirstChart.  # noqa: E501
        :rtype: EmosFirstChart
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this EmosFirstChart.

        system return code  # noqa: E501

        :return: The code of this EmosFirstChart.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this EmosFirstChart.

        system return code  # noqa: E501

        :param code: The code of this EmosFirstChart.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this EmosFirstChart.

        system return news  # noqa: E501

        :return: The msg of this EmosFirstChart.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this EmosFirstChart.

        system return news  # noqa: E501

        :param msg: The msg of this EmosFirstChart.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[EmosFirstCharts]:
        """Gets the result of this EmosFirstChart.


        :return: The result of this EmosFirstChart.
        :rtype: List[EmosFirstCharts]
        """
        return self._result

    @result.setter
    def result(self, result: List[EmosFirstCharts]):
        """Sets the result of this EmosFirstChart.


        :param result: The result of this EmosFirstChart.
        :type result: List[EmosFirstCharts]
        """

        self._result = result
