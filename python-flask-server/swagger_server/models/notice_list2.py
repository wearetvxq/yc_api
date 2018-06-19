# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.notice_lists2 import NoticeLists2  # noqa: F401,E501
from swagger_server import util


class NoticeList2(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[NoticeLists2]=None, result2: List[NoticeLists2]=None):  # noqa: E501
        """NoticeList2 - a model defined in Swagger

        :param code: The code of this NoticeList2.  # noqa: E501
        :type code: int
        :param msg: The msg of this NoticeList2.  # noqa: E501
        :type msg: str
        :param result: The result of this NoticeList2.  # noqa: E501
        :type result: List[NoticeLists2]
        :param result2: The result2 of this NoticeList2.  # noqa: E501
        :type result2: List[NoticeLists2]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[NoticeLists2],
            'result2': List[NoticeLists2]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'result': 'result',
            'result2': 'result2'
        }

        self._code = code
        self._msg = msg
        self._result = result
        self._result2 = result2

    @classmethod
    def from_dict(cls, dikt) -> 'NoticeList2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NoticeList2 of this NoticeList2.  # noqa: E501
        :rtype: NoticeList2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this NoticeList2.

        system return code  # noqa: E501

        :return: The code of this NoticeList2.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this NoticeList2.

        system return code  # noqa: E501

        :param code: The code of this NoticeList2.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this NoticeList2.

        system return news  # noqa: E501

        :return: The msg of this NoticeList2.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this NoticeList2.

        system return news  # noqa: E501

        :param msg: The msg of this NoticeList2.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[NoticeLists2]:
        """Gets the result of this NoticeList2.


        :return: The result of this NoticeList2.
        :rtype: List[NoticeLists2]
        """
        return self._result

    @result.setter
    def result(self, result: List[NoticeLists2]):
        """Sets the result of this NoticeList2.


        :param result: The result of this NoticeList2.
        :type result: List[NoticeLists2]
        """

        self._result = result

    @property
    def result2(self) -> List[NoticeLists2]:
        """Gets the result2 of this NoticeList2.


        :return: The result2 of this NoticeList2.
        :rtype: List[NoticeLists2]
        """
        return self._result2

    @result2.setter
    def result2(self, result2: List[NoticeLists2]):
        """Sets the result2 of this NoticeList2.


        :param result2: The result2 of this NoticeList2.
        :type result2: List[NoticeLists2]
        """

        self._result2 = result2
