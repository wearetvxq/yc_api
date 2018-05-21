# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UploadFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, url: str=None):  # noqa: E501
        """UploadFile - a model defined in Swagger

        :param code: The code of this UploadFile.  # noqa: E501
        :type code: int
        :param msg: The msg of this UploadFile.  # noqa: E501
        :type msg: str
        :param url: The url of this UploadFile.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'UploadFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UploadFile of this UploadFile.  # noqa: E501
        :rtype: UploadFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this UploadFile.

        system return code  # noqa: E501

        :return: The code of this UploadFile.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this UploadFile.

        system return code  # noqa: E501

        :param code: The code of this UploadFile.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this UploadFile.

        system return news  # noqa: E501

        :return: The msg of this UploadFile.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this UploadFile.

        system return news  # noqa: E501

        :param msg: The msg of this UploadFile.
        :type msg: str
        """

        self._msg = msg

    @property
    def url(self) -> str:
        """Gets the url of this UploadFile.

        return url  # noqa: E501

        :return: The url of this UploadFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this UploadFile.

        return url  # noqa: E501

        :param url: The url of this UploadFile.
        :type url: str
        """

        self._url = url
