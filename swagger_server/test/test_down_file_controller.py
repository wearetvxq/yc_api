# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.keyword import Keyword
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDownFileController(BaseTestCase):
    """ DownFileController integration test stubs """

    def test_down_file(self):
        """
        Test case for down_file

        down the file
        """
        sort = Keyword()
        response = self.client.open('/v1/down_file',
                                    method='POST',
                                    data=json.dumps(sort),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
