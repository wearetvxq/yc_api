# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StatisticsInstallLists(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, work: str=None, people: str=None, type: str=None, factory: str=None, model: str=None, balance: str=None, take: str=None, use: str=None, maintain: str=None, good: str=None, bad: str=None):  # noqa: E501
        """StatisticsInstallLists - a model defined in Swagger

        :param id: The id of this StatisticsInstallLists.  # noqa: E501
        :type id: int
        :param work: The work of this StatisticsInstallLists.  # noqa: E501
        :type work: str
        :param people: The people of this StatisticsInstallLists.  # noqa: E501
        :type people: str
        :param type: The type of this StatisticsInstallLists.  # noqa: E501
        :type type: str
        :param factory: The factory of this StatisticsInstallLists.  # noqa: E501
        :type factory: str
        :param model: The model of this StatisticsInstallLists.  # noqa: E501
        :type model: str
        :param balance: The balance of this StatisticsInstallLists.  # noqa: E501
        :type balance: str
        :param take: The take of this StatisticsInstallLists.  # noqa: E501
        :type take: str
        :param use: The use of this StatisticsInstallLists.  # noqa: E501
        :type use: str
        :param maintain: The maintain of this StatisticsInstallLists.  # noqa: E501
        :type maintain: str
        :param good: The good of this StatisticsInstallLists.  # noqa: E501
        :type good: str
        :param bad: The bad of this StatisticsInstallLists.  # noqa: E501
        :type bad: str
        """
        self.swagger_types = {
            'id': int,
            'work': str,
            'people': str,
            'type': str,
            'factory': str,
            'model': str,
            'balance': str,
            'take': str,
            'use': str,
            'maintain': str,
            'good': str,
            'bad': str
        }

        self.attribute_map = {
            'id': 'id',
            'work': 'work',
            'people': 'people',
            'type': 'type',
            'factory': 'factory',
            'model': 'model',
            'balance': 'balance',
            'take': 'take',
            'use': 'use',
            'maintain': 'maintain',
            'good': 'good',
            'bad': 'bad'
        }

        self._id = id
        self._work = work
        self._people = people
        self._type = type
        self._factory = factory
        self._model = model
        self._balance = balance
        self._take = take
        self._use = use
        self._maintain = maintain
        self._good = good
        self._bad = bad

    @classmethod
    def from_dict(cls, dikt) -> 'StatisticsInstallLists':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatisticsInstallLists of this StatisticsInstallLists.  # noqa: E501
        :rtype: StatisticsInstallLists
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this StatisticsInstallLists.

        ID  # noqa: E501

        :return: The id of this StatisticsInstallLists.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this StatisticsInstallLists.

        ID  # noqa: E501

        :param id: The id of this StatisticsInstallLists.
        :type id: int
        """

        self._id = id

    @property
    def work(self) -> str:
        """Gets the work of this StatisticsInstallLists.

        workstation  # noqa: E501

        :return: The work of this StatisticsInstallLists.
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work: str):
        """Sets the work of this StatisticsInstallLists.

        workstation  # noqa: E501

        :param work: The work of this StatisticsInstallLists.
        :type work: str
        """

        self._work = work

    @property
    def people(self) -> str:
        """Gets the people of this StatisticsInstallLists.

        workstation  # noqa: E501

        :return: The people of this StatisticsInstallLists.
        :rtype: str
        """
        return self._people

    @people.setter
    def people(self, people: str):
        """Sets the people of this StatisticsInstallLists.

        workstation  # noqa: E501

        :param people: The people of this StatisticsInstallLists.
        :type people: str
        """

        self._people = people

    @property
    def type(self) -> str:
        """Gets the type of this StatisticsInstallLists.

        terminal type  # noqa: E501

        :return: The type of this StatisticsInstallLists.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this StatisticsInstallLists.

        terminal type  # noqa: E501

        :param type: The type of this StatisticsInstallLists.
        :type type: str
        """

        self._type = type

    @property
    def factory(self) -> str:
        """Gets the factory of this StatisticsInstallLists.

        factory  # noqa: E501

        :return: The factory of this StatisticsInstallLists.
        :rtype: str
        """
        return self._factory

    @factory.setter
    def factory(self, factory: str):
        """Sets the factory of this StatisticsInstallLists.

        factory  # noqa: E501

        :param factory: The factory of this StatisticsInstallLists.
        :type factory: str
        """

        self._factory = factory

    @property
    def model(self) -> str:
        """Gets the model of this StatisticsInstallLists.

        model  # noqa: E501

        :return: The model of this StatisticsInstallLists.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this StatisticsInstallLists.

        model  # noqa: E501

        :param model: The model of this StatisticsInstallLists.
        :type model: str
        """

        self._model = model

    @property
    def balance(self) -> str:
        """Gets the balance of this StatisticsInstallLists.

        Previous balance  # noqa: E501

        :return: The balance of this StatisticsInstallLists.
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance: str):
        """Sets the balance of this StatisticsInstallLists.

        Previous balance  # noqa: E501

        :param balance: The balance of this StatisticsInstallLists.
        :type balance: str
        """

        self._balance = balance

    @property
    def take(self) -> str:
        """Gets the take of this StatisticsInstallLists.

        The number of applications for this period  # noqa: E501

        :return: The take of this StatisticsInstallLists.
        :rtype: str
        """
        return self._take

    @take.setter
    def take(self, take: str):
        """Sets the take of this StatisticsInstallLists.

        The number of applications for this period  # noqa: E501

        :param take: The take of this StatisticsInstallLists.
        :type take: str
        """

        self._take = take

    @property
    def use(self) -> str:
        """Gets the use of this StatisticsInstallLists.

        Installed capacity  # noqa: E501

        :return: The use of this StatisticsInstallLists.
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use: str):
        """Sets the use of this StatisticsInstallLists.

        Installed capacity  # noqa: E501

        :param use: The use of this StatisticsInstallLists.
        :type use: str
        """

        self._use = use

    @property
    def maintain(self) -> str:
        """Gets the maintain of this StatisticsInstallLists.

        Maintenance usage  # noqa: E501

        :return: The maintain of this StatisticsInstallLists.
        :rtype: str
        """
        return self._maintain

    @maintain.setter
    def maintain(self, maintain: str):
        """Sets the maintain of this StatisticsInstallLists.

        Maintenance usage  # noqa: E501

        :param maintain: The maintain of this StatisticsInstallLists.
        :type maintain: str
        """

        self._maintain = maintain

    @property
    def good(self) -> str:
        """Gets the good of this StatisticsInstallLists.

        The remaining number of pieces  # noqa: E501

        :return: The good of this StatisticsInstallLists.
        :rtype: str
        """
        return self._good

    @good.setter
    def good(self, good: str):
        """Sets the good of this StatisticsInstallLists.

        The remaining number of pieces  # noqa: E501

        :param good: The good of this StatisticsInstallLists.
        :type good: str
        """

        self._good = good

    @property
    def bad(self) -> str:
        """Gets the bad of this StatisticsInstallLists.

        The number of bad balances  # noqa: E501

        :return: The bad of this StatisticsInstallLists.
        :rtype: str
        """
        return self._bad

    @bad.setter
    def bad(self, bad: str):
        """Sets the bad of this StatisticsInstallLists.

        The number of bad balances  # noqa: E501

        :param bad: The bad of this StatisticsInstallLists.
        :type bad: str
        """

        self._bad = bad
