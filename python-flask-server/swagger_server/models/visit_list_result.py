# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.visit_list_ivr_result import VisitListIvrResult  # noqa: F401,E501
from swagger_server.models.visit_listart_result import VisitListartResult  # noqa: F401,E501
from swagger_server import util


class VisitListResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, area: str=None, rate: str=None, rank: str=None, ivr: List[VisitListIvrResult]=None, artificial: List[VisitListartResult]=None):  # noqa: E501
        """VisitListResult - a model defined in Swagger

        :param id: The id of this VisitListResult.  # noqa: E501
        :type id: int
        :param area: The area of this VisitListResult.  # noqa: E501
        :type area: str
        :param rate: The rate of this VisitListResult.  # noqa: E501
        :type rate: str
        :param rank: The rank of this VisitListResult.  # noqa: E501
        :type rank: str
        :param ivr: The ivr of this VisitListResult.  # noqa: E501
        :type ivr: List[VisitListIvrResult]
        :param artificial: The artificial of this VisitListResult.  # noqa: E501
        :type artificial: List[VisitListartResult]
        """
        self.swagger_types = {
            'id': int,
            'area': str,
            'rate': str,
            'rank': str,
            'ivr': List[VisitListIvrResult],
            'artificial': List[VisitListartResult]
        }

        self.attribute_map = {
            'id': 'id',
            'area': 'area',
            'rate': 'rate',
            'rank': 'rank',
            'ivr': 'ivr',
            'artificial': 'artificial'
        }

        self._id = id
        self._area = area
        self._rate = rate
        self._rank = rank
        self._ivr = ivr
        self._artificial = artificial

    @classmethod
    def from_dict(cls, dikt) -> 'VisitListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VisitListResult of this VisitListResult.  # noqa: E501
        :rtype: VisitListResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this VisitListResult.

        ID  # noqa: E501

        :return: The id of this VisitListResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this VisitListResult.

        ID  # noqa: E501

        :param id: The id of this VisitListResult.
        :type id: int
        """

        self._id = id

    @property
    def area(self) -> str:
        """Gets the area of this VisitListResult.

        area  # noqa: E501

        :return: The area of this VisitListResult.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area: str):
        """Sets the area of this VisitListResult.

        area  # noqa: E501

        :param area: The area of this VisitListResult.
        :type area: str
        """

        self._area = area

    @property
    def rate(self) -> str:
        """Gets the rate of this VisitListResult.

        Complaints visit satisfaction  # noqa: E501

        :return: The rate of this VisitListResult.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate: str):
        """Sets the rate of this VisitListResult.

        Complaints visit satisfaction  # noqa: E501

        :param rate: The rate of this VisitListResult.
        :type rate: str
        """

        self._rate = rate

    @property
    def rank(self) -> str:
        """Gets the rank of this VisitListResult.

        Rank  # noqa: E501

        :return: The rank of this VisitListResult.
        :rtype: str
        """
        return self._rank

    @rank.setter
    def rank(self, rank: str):
        """Sets the rank of this VisitListResult.

        Rank  # noqa: E501

        :param rank: The rank of this VisitListResult.
        :type rank: str
        """

        self._rank = rank

    @property
    def ivr(self) -> List[VisitListIvrResult]:
        """Gets the ivr of this VisitListResult.


        :return: The ivr of this VisitListResult.
        :rtype: List[VisitListIvrResult]
        """
        return self._ivr

    @ivr.setter
    def ivr(self, ivr: List[VisitListIvrResult]):
        """Sets the ivr of this VisitListResult.


        :param ivr: The ivr of this VisitListResult.
        :type ivr: List[VisitListIvrResult]
        """

        self._ivr = ivr

    @property
    def artificial(self) -> List[VisitListartResult]:
        """Gets the artificial of this VisitListResult.


        :return: The artificial of this VisitListResult.
        :rtype: List[VisitListartResult]
        """
        return self._artificial

    @artificial.setter
    def artificial(self, artificial: List[VisitListartResult]):
        """Sets the artificial of this VisitListResult.


        :param artificial: The artificial of this VisitListResult.
        :type artificial: List[VisitListartResult]
        """

        self._artificial = artificial
