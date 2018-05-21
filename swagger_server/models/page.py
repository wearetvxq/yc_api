# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Page(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pageindex: int=None):
        """
        Page - a model defined in Swagger

        :param pageindex: The pageindex of this Page.
        :type pageindex: int
        """
        self.swagger_types = {
            'pageindex': int
        }

        self.attribute_map = {
            'pageindex': 'pageindex'
        }

        self._pageindex = pageindex

    @classmethod
    def from_dict(cls, dikt) -> 'Page':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The page of this Page.
        :rtype: Page
        """
        return deserialize_model(dikt, cls)

    @property
    def pageindex(self) -> int:
        """
        Gets the pageindex of this Page.
        page of data

        :return: The pageindex of this Page.
        :rtype: int
        """
        return self._pageindex

    @pageindex.setter
    def pageindex(self, pageindex: int):
        """
        Sets the pageindex of this Page.
        page of data

        :param pageindex: The pageindex of this Page.
        :type pageindex: int
        """

        self._pageindex = pageindex
