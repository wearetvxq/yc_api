# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestImportfileController(BaseTestCase):
    """ ImportfileController integration test stubs """

    def test_import_data(self):
        """
        Test case for import_data

        import_data
        """
        data = dict(filetype='filetype_example',
                    file='file_example')
        response = self.client.open('/v1/Importfile',
                                    method='POST',
                                    data=data,
                                    content_type='multipart/form-data')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
