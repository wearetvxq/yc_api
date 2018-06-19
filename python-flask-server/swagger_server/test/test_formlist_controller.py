# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response2002 import InlineResponse2002
from swagger_server.models.inline_response5001 import InlineResponse5001
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestFormlistController(BaseTestCase):
    """ FormlistController integration test stubs """

    def test_formlist(self):
        """
        Test case for formlist

        get the data of form_list
        """
        query_string = [('pageindex', 56),
                        ('area', 'area_example'),
                        ('pingtai', 'pingtai_example'),
                        ('status', 'status_example'),
                        ('complaint', 'complaint_example'),
                        ('Timeout', 'Timeout_example'),
                        ('start_time', 56),
                        ('end_time', 56)]
        response = self.client.open('/v1/formlist',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
