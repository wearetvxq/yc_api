# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UseLists(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, work: str=None, business: str=None, order: str=None, modem: str=None, gateway: str=None, box: str=None, hemu: str=None, phone: str=None, personnel: str=None, posttime: str=None):  # noqa: E501
        """UseLists - a model defined in Swagger

        :param id: The id of this UseLists.  # noqa: E501
        :type id: int
        :param work: The work of this UseLists.  # noqa: E501
        :type work: str
        :param business: The business of this UseLists.  # noqa: E501
        :type business: str
        :param order: The order of this UseLists.  # noqa: E501
        :type order: str
        :param modem: The modem of this UseLists.  # noqa: E501
        :type modem: str
        :param gateway: The gateway of this UseLists.  # noqa: E501
        :type gateway: str
        :param box: The box of this UseLists.  # noqa: E501
        :type box: str
        :param hemu: The hemu of this UseLists.  # noqa: E501
        :type hemu: str
        :param phone: The phone of this UseLists.  # noqa: E501
        :type phone: str
        :param personnel: The personnel of this UseLists.  # noqa: E501
        :type personnel: str
        :param posttime: The posttime of this UseLists.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'id': int,
            'work': str,
            'business': str,
            'order': str,
            'modem': str,
            'gateway': str,
            'box': str,
            'hemu': str,
            'phone': str,
            'personnel': str,
            'posttime': str
        }

        self.attribute_map = {
            'id': 'id',
            'work': 'work',
            'business': 'business',
            'order': 'order',
            'modem': 'modem',
            'gateway': 'gateway',
            'box': 'box',
            'hemu': 'hemu',
            'phone': 'phone',
            'personnel': 'personnel',
            'posttime': 'posttime'
        }

        self._id = id
        self._work = work
        self._business = business
        self._order = order
        self._modem = modem
        self._gateway = gateway
        self._box = box
        self._hemu = hemu
        self._phone = phone
        self._personnel = personnel
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'UseLists':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UseLists of this UseLists.  # noqa: E501
        :rtype: UseLists
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this UseLists.

        ID  # noqa: E501

        :return: The id of this UseLists.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this UseLists.

        ID  # noqa: E501

        :param id: The id of this UseLists.
        :type id: int
        """

        self._id = id

    @property
    def work(self) -> str:
        """Gets the work of this UseLists.

        workstation  # noqa: E501

        :return: The work of this UseLists.
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work: str):
        """Sets the work of this UseLists.

        workstation  # noqa: E501

        :param work: The work of this UseLists.
        :type work: str
        """

        self._work = work

    @property
    def business(self) -> str:
        """Gets the business of this UseLists.

        business type  # noqa: E501

        :return: The business of this UseLists.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business: str):
        """Sets the business of this UseLists.

        business type  # noqa: E501

        :param business: The business of this UseLists.
        :type business: str
        """

        self._business = business

    @property
    def order(self) -> str:
        """Gets the order of this UseLists.

        Work order  # noqa: E501

        :return: The order of this UseLists.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order: str):
        """Sets the order of this UseLists.

        Work order  # noqa: E501

        :param order: The order of this UseLists.
        :type order: str
        """

        self._order = order

    @property
    def modem(self) -> str:
        """Gets the modem of this UseLists.

        Modem bar code  # noqa: E501

        :return: The modem of this UseLists.
        :rtype: str
        """
        return self._modem

    @modem.setter
    def modem(self, modem: str):
        """Sets the modem of this UseLists.

        Modem bar code  # noqa: E501

        :param modem: The modem of this UseLists.
        :type modem: str
        """

        self._modem = modem

    @property
    def gateway(self) -> str:
        """Gets the gateway of this UseLists.

        Gateway barcode  # noqa: E501

        :return: The gateway of this UseLists.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway: str):
        """Sets the gateway of this UseLists.

        Gateway barcode  # noqa: E501

        :param gateway: The gateway of this UseLists.
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def box(self) -> str:
        """Gets the box of this UseLists.

        Set-top box barcode  # noqa: E501

        :return: The box of this UseLists.
        :rtype: str
        """
        return self._box

    @box.setter
    def box(self, box: str):
        """Sets the box of this UseLists.

        Set-top box barcode  # noqa: E501

        :param box: The box of this UseLists.
        :type box: str
        """

        self._box = box

    @property
    def hemu(self) -> str:
        """Gets the hemu of this UseLists.

        hemu bar code  # noqa: E501

        :return: The hemu of this UseLists.
        :rtype: str
        """
        return self._hemu

    @hemu.setter
    def hemu(self, hemu: str):
        """Sets the hemu of this UseLists.

        hemu bar code  # noqa: E501

        :param hemu: The hemu of this UseLists.
        :type hemu: str
        """

        self._hemu = hemu

    @property
    def phone(self) -> str:
        """Gets the phone of this UseLists.

        Fixed phone barcode  # noqa: E501

        :return: The phone of this UseLists.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this UseLists.

        Fixed phone barcode  # noqa: E501

        :param phone: The phone of this UseLists.
        :type phone: str
        """

        self._phone = phone

    @property
    def personnel(self) -> str:
        """Gets the personnel of this UseLists.

        Installation staff  # noqa: E501

        :return: The personnel of this UseLists.
        :rtype: str
        """
        return self._personnel

    @personnel.setter
    def personnel(self, personnel: str):
        """Sets the personnel of this UseLists.

        Installation staff  # noqa: E501

        :param personnel: The personnel of this UseLists.
        :type personnel: str
        """

        self._personnel = personnel

    @property
    def posttime(self) -> str:
        """Gets the posttime of this UseLists.

        use time  # noqa: E501

        :return: The posttime of this UseLists.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this UseLists.

        use time  # noqa: E501

        :param posttime: The posttime of this UseLists.
        :type posttime: str
        """

        self._posttime = posttime
