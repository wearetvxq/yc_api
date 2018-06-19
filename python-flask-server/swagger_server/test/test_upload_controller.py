# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.keyword import Keyword  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.upload import Upload  # noqa: E501
from swagger_server.models.upload_file import UploadFile  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUploadController(BaseTestCase):
    """UploadController integration test stubs"""

    def test_upload_delete(self):
        """Test case for upload_delete

        User Upload
        """
        query_string = [('id', 56)]
        response = self.client.open(
            '/v1/upload/delete',
            method='DELETE',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_file_post(self):
        """Test case for upload_file_post

        User Upload
        """
        data = dict(files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/v1/upload/file',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_filelist_get(self):
        """Test case for upload_filelist_get

        User Upload
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/upload/filelist',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_post(self):
        """Test case for upload_post

        User Upload
        """
        body = Upload()
        response = self.client.open(
            '/v1/upload',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
