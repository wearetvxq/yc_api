# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StorageLists(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, work: str=None, type: str=None, factory: str=None, model: str=None, code: str=None, principal: str=None, posttime: str=None):  # noqa: E501
        """StorageLists - a model defined in Swagger

        :param id: The id of this StorageLists.  # noqa: E501
        :type id: int
        :param work: The work of this StorageLists.  # noqa: E501
        :type work: str
        :param type: The type of this StorageLists.  # noqa: E501
        :type type: str
        :param factory: The factory of this StorageLists.  # noqa: E501
        :type factory: str
        :param model: The model of this StorageLists.  # noqa: E501
        :type model: str
        :param code: The code of this StorageLists.  # noqa: E501
        :type code: str
        :param principal: The principal of this StorageLists.  # noqa: E501
        :type principal: str
        :param posttime: The posttime of this StorageLists.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'id': int,
            'work': str,
            'type': str,
            'factory': str,
            'model': str,
            'code': str,
            'principal': str,
            'posttime': str
        }

        self.attribute_map = {
            'id': 'id',
            'work': 'work',
            'type': 'type',
            'factory': 'factory',
            'model': 'model',
            'code': 'code',
            'principal': 'principal',
            'posttime': 'posttime'
        }

        self._id = id
        self._work = work
        self._type = type
        self._factory = factory
        self._model = model
        self._code = code
        self._principal = principal
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'StorageLists':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The storageLists of this StorageLists.  # noqa: E501
        :rtype: StorageLists
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this StorageLists.

        ID  # noqa: E501

        :return: The id of this StorageLists.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this StorageLists.

        ID  # noqa: E501

        :param id: The id of this StorageLists.
        :type id: int
        """

        self._id = id

    @property
    def work(self) -> str:
        """Gets the work of this StorageLists.

        workstation  # noqa: E501

        :return: The work of this StorageLists.
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work: str):
        """Sets the work of this StorageLists.

        workstation  # noqa: E501

        :param work: The work of this StorageLists.
        :type work: str
        """

        self._work = work

    @property
    def type(self) -> str:
        """Gets the type of this StorageLists.

        terminal type  # noqa: E501

        :return: The type of this StorageLists.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this StorageLists.

        terminal type  # noqa: E501

        :param type: The type of this StorageLists.
        :type type: str
        """

        self._type = type

    @property
    def factory(self) -> str:
        """Gets the factory of this StorageLists.

        factory  # noqa: E501

        :return: The factory of this StorageLists.
        :rtype: str
        """
        return self._factory

    @factory.setter
    def factory(self, factory: str):
        """Sets the factory of this StorageLists.

        factory  # noqa: E501

        :param factory: The factory of this StorageLists.
        :type factory: str
        """

        self._factory = factory

    @property
    def model(self) -> str:
        """Gets the model of this StorageLists.

        model  # noqa: E501

        :return: The model of this StorageLists.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this StorageLists.

        model  # noqa: E501

        :param model: The model of this StorageLists.
        :type model: str
        """

        self._model = model

    @property
    def code(self) -> str:
        """Gets the code of this StorageLists.

        Bar code  # noqa: E501

        :return: The code of this StorageLists.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this StorageLists.

        Bar code  # noqa: E501

        :param code: The code of this StorageLists.
        :type code: str
        """

        self._code = code

    @property
    def principal(self) -> str:
        """Gets the principal of this StorageLists.

        Warehousing  # noqa: E501

        :return: The principal of this StorageLists.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal: str):
        """Sets the principal of this StorageLists.

        Warehousing  # noqa: E501

        :param principal: The principal of this StorageLists.
        :type principal: str
        """

        self._principal = principal

    @property
    def posttime(self) -> str:
        """Gets the posttime of this StorageLists.

        date time  # noqa: E501

        :return: The posttime of this StorageLists.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this StorageLists.

        date time  # noqa: E501

        :param posttime: The posttime of this StorageLists.
        :type posttime: str
        """

        self._posttime = posttime
