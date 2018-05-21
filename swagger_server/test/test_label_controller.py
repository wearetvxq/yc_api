# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dict_list import DictList  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLabelController(BaseTestCase):
    """LabelController integration test stubs"""

    def test_label_business_get(self):
        """Test case for label_business_get

        business type
        """
        response = self.client.open(
            '/v1/label/business',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_label_people_get(self):
        """Test case for label_people_get

        Installed Dimensions Staff Dictionary Table
        """
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/v1/label/people',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_label_terminal_model_get(self):
        """Test case for label_terminal_model_get

        terminal model
        """
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/v1/label/terminal/model',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_label_terminal_type_get(self):
        """Test case for label_terminal_type_get

        terminal type
        """
        response = self.client.open(
            '/v1/label/terminal/type',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_label_work_get(self):
        """Test case for label_work_get

        Workstation dictionary interface
        """
        response = self.client.open(
            '/v1/label/work',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
