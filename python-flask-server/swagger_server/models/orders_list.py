# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.orders_list_result import OrdersListResult  # noqa: F401,E501
from swagger_server import util


class OrdersList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[OrdersListResult]=None):  # noqa: E501
        """OrdersList - a model defined in Swagger

        :param code: The code of this OrdersList.  # noqa: E501
        :type code: int
        :param msg: The msg of this OrdersList.  # noqa: E501
        :type msg: str
        :param result: The result of this OrdersList.  # noqa: E501
        :type result: List[OrdersListResult]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[OrdersListResult]
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
    def from_dict(cls, dikt) -> 'OrdersList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrdersList of this OrdersList.  # noqa: E501
        :rtype: OrdersList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this OrdersList.

        system return code  # noqa: E501

        :return: The code of this OrdersList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this OrdersList.

        system return code  # noqa: E501

        :param code: The code of this OrdersList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this OrdersList.

        system return news  # noqa: E501

        :return: The msg of this OrdersList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this OrdersList.

        system return news  # noqa: E501

        :param msg: The msg of this OrdersList.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[OrdersListResult]:
        """Gets the result of this OrdersList.


        :return: The result of this OrdersList.
        :rtype: List[OrdersListResult]
        """
        return self._result

    @result.setter
    def result(self, result: List[OrdersListResult]):
        """Sets the result of this OrdersList.


        :param result: The result of this OrdersList.
        :type result: List[OrdersListResult]
        """

        self._result = result