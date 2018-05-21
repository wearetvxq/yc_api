# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.inline_response5001 import InlineResponse5001
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHistoricalController(BaseTestCase):
    """ HistoricalController integration test stubs """

    def test_historical(self):
        """
        Test case for historical

        historical_data
        """
        query_string = [('pageindex', 56),
                        ('type', 'type_example'),
                        ('status', 'status_example'),
                        ('time', 56)]
        response = self.client.open('/v1/historical',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
