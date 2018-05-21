# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2002Result(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, area: str=None, pingtai: str=None, complaint: str=None, status: str=None, timeout: str=None, starttime: str=None, endtime: str=None):
        """
        InlineResponse2002Result - a model defined in Swagger

        :param area: The area of this InlineResponse2002Result.
        :type area: str
        :param pingtai: The pingtai of this InlineResponse2002Result.
        :type pingtai: str
        :param complaint: The complaint of this InlineResponse2002Result.
        :type complaint: str
        :param status: The status of this InlineResponse2002Result.
        :type status: str
        :param timeout: The timeout of this InlineResponse2002Result.
        :type timeout: str
        :param starttime: The starttime of this InlineResponse2002Result.
        :type starttime: str
        :param endtime: The endtime of this InlineResponse2002Result.
        :type endtime: str
        """
        self.swagger_types = {
            'area': str,
            'pingtai': str,
            'complaint': str,
            'status': str,
            'timeout': str,
            'starttime': str,
            'endtime': str
        }

        self.attribute_map = {
            'area': 'area',
            'pingtai': 'pingtai',
            'complaint': 'complaint',
            'status': 'status',
            'timeout': 'Timeout',
            'starttime': 'starttime',
            'endtime': 'endtime'
        }

        self._area = area
        self._pingtai = pingtai
        self._complaint = complaint
        self._status = status
        self._timeout = timeout
        self._starttime = starttime
        self._endtime = endtime

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002Result':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2_result of this InlineResponse2002Result.
        :rtype: InlineResponse2002Result
        """
        return deserialize_model(dikt, cls)

    @property
    def area(self) -> str:
        """
        Gets the area of this InlineResponse2002Result.
        Guest area

        :return: The area of this InlineResponse2002Result.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area: str):
        """
        Sets the area of this InlineResponse2002Result.
        Guest area

        :param area: The area of this InlineResponse2002Result.
        :type area: str
        """

        self._area = area

    @property
    def pingtai(self) -> str:
        """
        Gets the pingtai of this InlineResponse2002Result.
        Guest pingtai

        :return: The pingtai of this InlineResponse2002Result.
        :rtype: str
        """
        return self._pingtai

    @pingtai.setter
    def pingtai(self, pingtai: str):
        """
        Sets the pingtai of this InlineResponse2002Result.
        Guest pingtai

        :param pingtai: The pingtai of this InlineResponse2002Result.
        :type pingtai: str
        """

        self._pingtai = pingtai

    @property
    def complaint(self) -> str:
        """
        Gets the complaint of this InlineResponse2002Result.
        complaint

        :return: The complaint of this InlineResponse2002Result.
        :rtype: str
        """
        return self._complaint

    @complaint.setter
    def complaint(self, complaint: str):
        """
        Sets the complaint of this InlineResponse2002Result.
        complaint

        :param complaint: The complaint of this InlineResponse2002Result.
        :type complaint: str
        """

        self._complaint = complaint

    @property
    def status(self) -> str:
        """
        Gets the status of this InlineResponse2002Result.
        status

        :return: The status of this InlineResponse2002Result.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """
        Sets the status of this InlineResponse2002Result.
        status

        :param status: The status of this InlineResponse2002Result.
        :type status: str
        """

        self._status = status

    @property
    def timeout(self) -> str:
        """
        Gets the timeout of this InlineResponse2002Result.
        Timeout

        :return: The timeout of this InlineResponse2002Result.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout: str):
        """
        Sets the timeout of this InlineResponse2002Result.
        Timeout

        :param timeout: The timeout of this InlineResponse2002Result.
        :type timeout: str
        """

        self._timeout = timeout

    @property
    def starttime(self) -> str:
        """
        Gets the starttime of this InlineResponse2002Result.
        starttime

        :return: The starttime of this InlineResponse2002Result.
        :rtype: str
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime: str):
        """
        Sets the starttime of this InlineResponse2002Result.
        starttime

        :param starttime: The starttime of this InlineResponse2002Result.
        :type starttime: str
        """

        self._starttime = starttime

    @property
    def endtime(self) -> str:
        """
        Gets the endtime of this InlineResponse2002Result.
        endtime

        :return: The endtime of this InlineResponse2002Result.
        :rtype: str
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime: str):
        """
        Sets the endtime of this InlineResponse2002Result.
        endtime

        :param endtime: The endtime of this InlineResponse2002Result.
        :type endtime: str
        """

        self._endtime = endtime
