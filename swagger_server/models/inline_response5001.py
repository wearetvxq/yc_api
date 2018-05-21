# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse5001(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code: int=None, msg: str=None):
        """
        InlineResponse5001 - a model defined in Swagger

        :param code: The code of this InlineResponse5001.
        :type code: int
        :param msg: The msg of this InlineResponse5001.
        :type msg: str
        """
        self.swagger_types = {
            'code': int,
            'msg': str
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg'
        }

        self._code = code
        self._msg = msg

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse5001':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_500_1 of this InlineResponse5001.
        :rtype: InlineResponse5001
        """
        return deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """
        Gets the code of this InlineResponse5001.
        system return code

        :return: The code of this InlineResponse5001.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """
        Sets the code of this InlineResponse5001.
        system return code

        :param code: The code of this InlineResponse5001.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """
        Gets the msg of this InlineResponse5001.
        system return news

        :return: The msg of this InlineResponse5001.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """
        Sets the msg of this InlineResponse5001.
        system return news

        :param msg: The msg of this InlineResponse5001.
        :type msg: str
        """

        self._msg = msg
