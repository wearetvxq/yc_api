# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Export(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, url: str=None):  # noqa: E501
        """Export - a model defined in Swagger

        :param code: The code of this Export.  # noqa: E501
        :type code: int
        :param msg: The msg of this Export.  # noqa: E501
        :type msg: str
        :param url: The url of this Export.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'url': str
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'url': 'url'
        }

        self._code = code
        self._msg = msg
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Export':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The export of this Export.  # noqa: E501
        :rtype: Export
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this Export.

        system return code  # noqa: E501

        :return: The code of this Export.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this Export.

        system return code  # noqa: E501

        :param code: The code of this Export.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this Export.

        system return news  # noqa: E501

        :return: The msg of this Export.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this Export.

        system return news  # noqa: E501

        :param msg: The msg of this Export.
        :type msg: str
        """

        self._msg = msg

    @property
    def url(self) -> str:
        """Gets the url of this Export.

        return url  # noqa: E501

        :return: The url of this Export.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Export.

        return url  # noqa: E501

        :param url: The url of this Export.
        :type url: str
        """

        self._url = url
