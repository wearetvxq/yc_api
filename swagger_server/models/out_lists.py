# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class OutLists(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, work: str=None, type: str=None, factory: str=None, model: str=None, code: str=None, personnel: str=None, posttime: str=None):  # noqa: E501
        """OutLists - a model defined in Swagger

        :param id: The id of this OutLists.  # noqa: E501
        :type id: int
        :param work: The work of this OutLists.  # noqa: E501
        :type work: str
        :param type: The type of this OutLists.  # noqa: E501
        :type type: str
        :param factory: The factory of this OutLists.  # noqa: E501
        :type factory: str
        :param model: The model of this OutLists.  # noqa: E501
        :type model: str
        :param code: The code of this OutLists.  # noqa: E501
        :type code: str
        :param personnel: The personnel of this OutLists.  # noqa: E501
        :type personnel: str
        :param posttime: The posttime of this OutLists.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'id': int,
            'work': str,
            'type': str,
            'factory': str,
            'model': str,
            'code': str,
            'personnel': str,
            'posttime': str
        }

        self.attribute_map = {
            'id': 'id',
            'work': 'work',
            'type': 'type',
            'factory': 'factory',
            'model': 'model',
            'code': 'code',
            'personnel': 'personnel',
            'posttime': 'posttime'
        }

        self._id = id
        self._work = work
        self._type = type
        self._factory = factory
        self._model = model
        self._code = code
        self._personnel = personnel
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'OutLists':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OutLists of this OutLists.  # noqa: E501
        :rtype: OutLists
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this OutLists.

        ID  # noqa: E501

        :return: The id of this OutLists.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this OutLists.

        ID  # noqa: E501

        :param id: The id of this OutLists.
        :type id: int
        """

        self._id = id

    @property
    def work(self) -> str:
        """Gets the work of this OutLists.

        workstation  # noqa: E501

        :return: The work of this OutLists.
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work: str):
        """Sets the work of this OutLists.

        workstation  # noqa: E501

        :param work: The work of this OutLists.
        :type work: str
        """

        self._work = work

    @property
    def type(self) -> str:
        """Gets the type of this OutLists.

        terminal type  # noqa: E501

        :return: The type of this OutLists.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this OutLists.

        terminal type  # noqa: E501

        :param type: The type of this OutLists.
        :type type: str
        """

        self._type = type

    @property
    def factory(self) -> str:
        """Gets the factory of this OutLists.

        factory  # noqa: E501

        :return: The factory of this OutLists.
        :rtype: str
        """
        return self._factory

    @factory.setter
    def factory(self, factory: str):
        """Sets the factory of this OutLists.

        factory  # noqa: E501

        :param factory: The factory of this OutLists.
        :type factory: str
        """

        self._factory = factory

    @property
    def model(self) -> str:
        """Gets the model of this OutLists.

        model  # noqa: E501

        :return: The model of this OutLists.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this OutLists.

        model  # noqa: E501

        :param model: The model of this OutLists.
        :type model: str
        """

        self._model = model

    @property
    def code(self) -> str:
        """Gets the code of this OutLists.

        Bar code  # noqa: E501

        :return: The code of this OutLists.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this OutLists.

        Bar code  # noqa: E501

        :param code: The code of this OutLists.
        :type code: str
        """

        self._code = code

    @property
    def personnel(self) -> str:
        """Gets the personnel of this OutLists.

        Installation staff  # noqa: E501

        :return: The personnel of this OutLists.
        :rtype: str
        """
        return self._personnel

    @personnel.setter
    def personnel(self, personnel: str):
        """Sets the personnel of this OutLists.

        Installation staff  # noqa: E501

        :param personnel: The personnel of this OutLists.
        :type personnel: str
        """

        self._personnel = personnel

    @property
    def posttime(self) -> str:
        """Gets the posttime of this OutLists.

        date time  # noqa: E501

        :return: The posttime of this OutLists.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this OutLists.

        date time  # noqa: E501

        :param posttime: The posttime of this OutLists.
        :type posttime: str
        """

        self._posttime = posttime
