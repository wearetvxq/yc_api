# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TwentyFourInfoExportResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, area: str=None, acceptance: str=None, complete: str=None, unfinished: str=None, completed: str=None, timely: str=None, average: str=None, repeat: str=None, repeatrate: str=None, investment: str=None):  # noqa: E501
        """TwentyFourInfoExportResult - a model defined in Swagger

        :param area: The area of this TwentyFourInfoExportResult.  # noqa: E501
        :type area: str
        :param acceptance: The acceptance of this TwentyFourInfoExportResult.  # noqa: E501
        :type acceptance: str
        :param complete: The complete of this TwentyFourInfoExportResult.  # noqa: E501
        :type complete: str
        :param unfinished: The unfinished of this TwentyFourInfoExportResult.  # noqa: E501
        :type unfinished: str
        :param completed: The completed of this TwentyFourInfoExportResult.  # noqa: E501
        :type completed: str
        :param timely: The timely of this TwentyFourInfoExportResult.  # noqa: E501
        :type timely: str
        :param average: The average of this TwentyFourInfoExportResult.  # noqa: E501
        :type average: str
        :param repeat: The repeat of this TwentyFourInfoExportResult.  # noqa: E501
        :type repeat: str
        :param repeatrate: The repeatrate of this TwentyFourInfoExportResult.  # noqa: E501
        :type repeatrate: str
        :param investment: The investment of this TwentyFourInfoExportResult.  # noqa: E501
        :type investment: str
        """
        self.swagger_types = {
            'area': str,
            'acceptance': str,
            'complete': str,
            'unfinished': str,
            'completed': str,
            'timely': str,
            'average': str,
            'repeat': str,
            'repeatrate': str,
            'investment': str
        }

        self.attribute_map = {
            'area': 'area',
            'acceptance': 'acceptance',
            'complete': 'complete',
            'unfinished': 'unfinished',
            'completed': 'completed',
            'timely': 'timely',
            'average': 'average',
            'repeat': 'repeat',
            'repeatrate': 'repeatrate',
            'investment': 'investment'
        }

        self._area = area
        self._acceptance = acceptance
        self._complete = complete
        self._unfinished = unfinished
        self._completed = completed
        self._timely = timely
        self._average = average
        self._repeat = repeat
        self._repeatrate = repeatrate
        self._investment = investment

    @classmethod
    def from_dict(cls, dikt) -> 'TwentyFourInfoExportResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The twentyFourInfoExportResult of this TwentyFourInfoExportResult.  # noqa: E501
        :rtype: TwentyFourInfoExportResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area(self) -> str:
        """Gets the area of this TwentyFourInfoExportResult.

        by area  # noqa: E501

        :return: The area of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area: str):
        """Sets the area of this TwentyFourInfoExportResult.

        by area  # noqa: E501

        :param area: The area of this TwentyFourInfoExportResult.
        :type area: str
        """

        self._area = area

    @property
    def acceptance(self) -> str:
        """Gets the acceptance of this TwentyFourInfoExportResult.

        by acceptance  # noqa: E501

        :return: The acceptance of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._acceptance

    @acceptance.setter
    def acceptance(self, acceptance: str):
        """Sets the acceptance of this TwentyFourInfoExportResult.

        by acceptance  # noqa: E501

        :param acceptance: The acceptance of this TwentyFourInfoExportResult.
        :type acceptance: str
        """

        self._acceptance = acceptance

    @property
    def complete(self) -> str:
        """Gets the complete of this TwentyFourInfoExportResult.

        by complete  # noqa: E501

        :return: The complete of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._complete

    @complete.setter
    def complete(self, complete: str):
        """Sets the complete of this TwentyFourInfoExportResult.

        by complete  # noqa: E501

        :param complete: The complete of this TwentyFourInfoExportResult.
        :type complete: str
        """

        self._complete = complete

    @property
    def unfinished(self) -> str:
        """Gets the unfinished of this TwentyFourInfoExportResult.

        by unfinished  # noqa: E501

        :return: The unfinished of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._unfinished

    @unfinished.setter
    def unfinished(self, unfinished: str):
        """Sets the unfinished of this TwentyFourInfoExportResult.

        by unfinished  # noqa: E501

        :param unfinished: The unfinished of this TwentyFourInfoExportResult.
        :type unfinished: str
        """

        self._unfinished = unfinished

    @property
    def completed(self) -> str:
        """Gets the completed of this TwentyFourInfoExportResult.

        by completed  # noqa: E501

        :return: The completed of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed: str):
        """Sets the completed of this TwentyFourInfoExportResult.

        by completed  # noqa: E501

        :param completed: The completed of this TwentyFourInfoExportResult.
        :type completed: str
        """

        self._completed = completed

    @property
    def timely(self) -> str:
        """Gets the timely of this TwentyFourInfoExportResult.

        by timely  # noqa: E501

        :return: The timely of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._timely

    @timely.setter
    def timely(self, timely: str):
        """Sets the timely of this TwentyFourInfoExportResult.

        by timely  # noqa: E501

        :param timely: The timely of this TwentyFourInfoExportResult.
        :type timely: str
        """

        self._timely = timely

    @property
    def average(self) -> str:
        """Gets the average of this TwentyFourInfoExportResult.

        by average  # noqa: E501

        :return: The average of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._average

    @average.setter
    def average(self, average: str):
        """Sets the average of this TwentyFourInfoExportResult.

        by average  # noqa: E501

        :param average: The average of this TwentyFourInfoExportResult.
        :type average: str
        """

        self._average = average

    @property
    def repeat(self) -> str:
        """Gets the repeat of this TwentyFourInfoExportResult.

        by repeat  # noqa: E501

        :return: The repeat of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat: str):
        """Sets the repeat of this TwentyFourInfoExportResult.

        by repeat  # noqa: E501

        :param repeat: The repeat of this TwentyFourInfoExportResult.
        :type repeat: str
        """

        self._repeat = repeat

    @property
    def repeatrate(self) -> str:
        """Gets the repeatrate of this TwentyFourInfoExportResult.

        by repeatrate  # noqa: E501

        :return: The repeatrate of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._repeatrate

    @repeatrate.setter
    def repeatrate(self, repeatrate: str):
        """Sets the repeatrate of this TwentyFourInfoExportResult.

        by repeatrate  # noqa: E501

        :param repeatrate: The repeatrate of this TwentyFourInfoExportResult.
        :type repeatrate: str
        """

        self._repeatrate = repeatrate

    @property
    def investment(self) -> str:
        """Gets the investment of this TwentyFourInfoExportResult.

        by investment  # noqa: E501

        :return: The investment of this TwentyFourInfoExportResult.
        :rtype: str
        """
        return self._investment

    @investment.setter
    def investment(self, investment: str):
        """Sets the investment of this TwentyFourInfoExportResult.

        by investment  # noqa: E501

        :param investment: The investment of this TwentyFourInfoExportResult.
        :type investment: str
        """

        self._investment = investment
