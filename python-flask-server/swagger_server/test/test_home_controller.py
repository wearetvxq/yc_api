# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.notice_data import NoticeData  # noqa: E501
from swagger_server.models.notice_list import NoticeList  # noqa: E501
from swagger_server.models.notice_list2 import NoticeList2  # noqa: E501
from swagger_server.models.notice_lists2 import NoticeLists2  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHomeController(BaseTestCase):
    """HomeController integration test stubs"""

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

    def test_home_notice_all_list_get(self):
        """Test case for home_notice_all_list_get

        Index Notice list
        """
        response = self.client.open(
            '/v1/home/notice/all_list',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_notice_get(self):
        """Test case for home_notice_get

        Notice desc
        """
        response = self.client.open(
            '/v1/home/notice/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_notice_list_get(self):
        """Test case for home_notice_list_get

        Notice list
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example')]
        response = self.client.open(
            '/v1/home/notice/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_home_notice_post(self):
        """Test case for home_notice_post

        Notice desc
        """
        body = NoticeData()
        response = self.client.open(
            '/v1/home/notice',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_barone_get(self):
        """Test case for index_barone_get

        Index Barone Chart
        """
        response = self.client.open(
            '/v1/home/barone',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_lineone_get(self):
        """Test case for index_lineone_get

        Index Lineone Chart
        """
        response = self.client.open(
            '/v1/home/lineone',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_linetwo_get(self):
        """Test case for index_linetwo_get

        Index Linetwo Chart
        """
        response = self.client.open(
            '/v1/home/linetwo',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_pan_get(self):
        """Test case for index_pan_get

        Index Pan Chart
        """
        response = self.client.open(
            '/v1/home/pan',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_showall_export_get(self):
        """Test case for index_showall_export_get

        Index Showall
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/home/showall/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_showall_get(self):
        """Test case for index_showall_get

        Index Showall
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/home/showall',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
