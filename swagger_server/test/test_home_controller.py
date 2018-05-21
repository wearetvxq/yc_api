# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHomeController(BaseTestCase):
    """HomeController integration test stubs"""

    def test_home_barone_get(self):
        """Test case for home_barone_get

        Index Barone Chart
        """
        response = self.client.open(
            '/v1/home/barone',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_bartwo_get(self):
        """Test case for home_bartwo_get

        Index Bartwo Chart
        """
        response = self.client.open(
            '/v1/home/bartwo',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_lineone_get(self):
        """Test case for home_lineone_get

        Index Lineone Chart
        """
        response = self.client.open(
            '/v1/home/lineone',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_linetwo_get(self):
        """Test case for home_linetwo_get

        Index Linetwo Chart
        """
        response = self.client.open(
            '/v1/home/linetwo',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_pan_get(self):
        """Test case for home_pan_get

        Index Pan Chart
        """
        response = self.client.open(
            '/v1/home/pan',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
