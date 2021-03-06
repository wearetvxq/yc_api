# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StorageData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, work: str=None, type: str=None, factory: str=None, model: str=None, principal: str=None, code: str=None):  # noqa: E501
        """StorageData - a model defined in Swagger

        :param work: The work of this StorageData.  # noqa: E501
        :type work: str
        :param type: The type of this StorageData.  # noqa: E501
        :type type: str
        :param factory: The factory of this StorageData.  # noqa: E501
        :type factory: str
        :param model: The model of this StorageData.  # noqa: E501
        :type model: str
        :param principal: The principal of this StorageData.  # noqa: E501
        :type principal: str
        :param code: The code of this StorageData.  # noqa: E501
        :type code: str
        """
        self.swagger_types = {
            'work': str,
            'type': str,
            'factory': str,
            'model': str,
            'principal': str,
            'code': str
        }

        self.attribute_map = {
            'work': 'work',
            'type': 'type',
            'factory': 'factory',
            'model': 'model',
            'principal': 'principal',
            'code': 'code'
        }

        self._work = work
        self._type = type
        self._factory = factory
        self._model = model
        self._principal = principal
        self._code = code

    @classmethod
    def from_dict(cls, dikt) -> 'StorageData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The storageData of this StorageData.  # noqa: E501
        :rtype: StorageData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def work(self) -> str:
        """Gets the work of this StorageData.

        workstation  # noqa: E501

        :return: The work of this StorageData.
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work: str):
        """Sets the work of this StorageData.

        workstation  # noqa: E501

        :param work: The work of this StorageData.
        :type work: str
        """

        self._work = work

    @property
    def type(self) -> str:
        """Gets the type of this StorageData.

        terminal type  # noqa: E501

        :return: The type of this StorageData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this StorageData.

        terminal type  # noqa: E501

        :param type: The type of this StorageData.
        :type type: str
        """

        self._type = type

    @property
    def factory(self) -> str:
        """Gets the factory of this StorageData.

        factory  # noqa: E501

        :return: The factory of this StorageData.
        :rtype: str
        """
        return self._factory

    @factory.setter
    def factory(self, factory: str):
        """Sets the factory of this StorageData.

        factory  # noqa: E501

        :param factory: The factory of this StorageData.
        :type factory: str
        """

        self._factory = factory

    @property
    def model(self) -> str:
        """Gets the model of this StorageData.

        model  # noqa: E501

        :return: The model of this StorageData.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this StorageData.

        model  # noqa: E501

        :param model: The model of this StorageData.
        :type model: str
        """

        self._model = model

    @property
    def principal(self) -> str:
        """Gets the principal of this StorageData.

        Warehousing  # noqa: E501

        :return: The principal of this StorageData.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal: str):
        """Sets the principal of this StorageData.

        Warehousing  # noqa: E501

        :param principal: The principal of this StorageData.
        :type principal: str
        """

        self._principal = principal

    @property
    def code(self) -> str:
        """Gets the code of this StorageData.

        Bar code  # noqa: E501

        :return: The code of this StorageData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this StorageData.

        Bar code  # noqa: E501

        :param code: The code of this StorageData.
        :type code: str
        """

        self._code = code
