# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.inline_response2001_result import InlineResponse2001Result
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2001(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, page_count: int=None, msg: str=None, result: List[InlineResponse2001Result]=None, row_count: int=None):
        """
        InlineResponse2001 - a model defined in Swagger

        :param page_count: The page_count of this InlineResponse2001.
        :type page_count: int
        :param msg: The msg of this InlineResponse2001.
        :type msg: str
        :param result: The result of this InlineResponse2001.
        :type result: List[InlineResponse2001Result]
        :param row_count: The row_count of this InlineResponse2001.
        :type row_count: int
        """
        self.swagger_types = {
            'page_count': int,
            'msg': str,
            'result': List[InlineResponse2001Result],
            'row_count': int
        }

        self.attribute_map = {
            'page_count': 'pageCount',
            'msg': 'msg',
            'result': 'result',
            'row_count': 'rowCount'
        }

        self._page_count = page_count
        self._msg = msg
        self._result = result
        self._row_count = row_count

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.
        :rtype: InlineResponse2001
        """
        return deserialize_model(dikt, cls)

    @property
    def page_count(self) -> int:
        """
        Gets the page_count of this InlineResponse2001.
        total of page

        :return: The page_count of this InlineResponse2001.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count: int):
        """
        Sets the page_count of this InlineResponse2001.
        total of page

        :param page_count: The page_count of this InlineResponse2001.
        :type page_count: int
        """

        self._page_count = page_count

    @property
    def msg(self) -> str:
        """
        Gets the msg of this InlineResponse2001.
        system return status_msg

        :return: The msg of this InlineResponse2001.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """
        Sets the msg of this InlineResponse2001.
        system return status_msg

        :param msg: The msg of this InlineResponse2001.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[InlineResponse2001Result]:
        """
        Gets the result of this InlineResponse2001.

        :return: The result of this InlineResponse2001.
        :rtype: List[InlineResponse2001Result]
        """
        return self._result

    @result.setter
    def result(self, result: List[InlineResponse2001Result]):
        """
        Sets the result of this InlineResponse2001.

        :param result: The result of this InlineResponse2001.
        :type result: List[InlineResponse2001Result]
        """

        self._result = result

    @property
    def row_count(self) -> int:
        """
        Gets the row_count of this InlineResponse2001.
        total num of data

        :return: The row_count of this InlineResponse2001.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count: int):
        """
        Sets the row_count of this InlineResponse2001.
        total num of data

        :param row_count: The row_count of this InlineResponse2001.
        :type row_count: int
        """

        self._row_count = row_count
