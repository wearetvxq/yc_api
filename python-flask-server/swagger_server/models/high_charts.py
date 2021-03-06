# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.high_chart_column import HighChartColumn  # noqa: F401,E501
from swagger_server.models.high_chart_map import HighChartMap  # noqa: F401,E501
from swagger_server import util


class HighCharts(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, map: List[HighChartMap]=None, column: List[HighChartColumn]=None):  # noqa: E501
        """HighCharts - a model defined in Swagger

        :param map: The map of this HighCharts.  # noqa: E501
        :type map: List[HighChartMap]
        :param column: The column of this HighCharts.  # noqa: E501
        :type column: List[HighChartColumn]
        """
        self.swagger_types = {
            'map': List[HighChartMap],
            'column': List[HighChartColumn]
        }

        self.attribute_map = {
            'map': 'map',
            'column': 'column'
        }

        self._map = map
        self._column = column

    @classmethod
    def from_dict(cls, dikt) -> 'HighCharts':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HighCharts of this HighCharts.  # noqa: E501
        :rtype: HighCharts
        """
        return util.deserialize_model(dikt, cls)

    @property
    def map(self) -> List[HighChartMap]:
        """Gets the map of this HighCharts.


        :return: The map of this HighCharts.
        :rtype: List[HighChartMap]
        """
        return self._map

    @map.setter
    def map(self, map: List[HighChartMap]):
        """Sets the map of this HighCharts.


        :param map: The map of this HighCharts.
        :type map: List[HighChartMap]
        """

        self._map = map

    @property
    def column(self) -> List[HighChartColumn]:
        """Gets the column of this HighCharts.


        :return: The column of this HighCharts.
        :rtype: List[HighChartColumn]
        """
        return self._column

    @column.setter
    def column(self, column: List[HighChartColumn]):
        """Sets the column of this HighCharts.


        :param column: The column of this HighCharts.
        :type column: List[HighChartColumn]
        """

        self._column = column
