# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.down_url import DownUrl  # noqa: E501
from swagger_server.models.emos_first_chart import EmosFirstChart  # noqa: E501
from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.installed_list import InstalledList  # noqa: E501
from swagger_server.models.installed_top_list import InstalledTopList  # noqa: E501
from swagger_server.models.orders_list import OrdersList  # noqa: E501
from swagger_server.models.retreat_list import RetreatList  # noqa: E501
from swagger_server.models.satisfaction_list import SatisfactionList  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInstalledController(BaseTestCase):
    """InstalledController integration test stubs"""

    def test_installed_agricultural_chart_get(self):
        """Test case for installed_agricultural_chart_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/agricultural/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_agricultural_info_export_get(self):
        """Test case for installed_agricultural_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/agricultural/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_agricultural_list_export_get(self):
        """Test case for installed_agricultural_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/agricultural/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_agricultural_list_get(self):
        """Test case for installed_agricultural_list_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/agricultural/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_eight_chart_get(self):
        """Test case for installed_eight_chart_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/eight/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_eight_info_export_get(self):
        """Test case for installed_eight_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/eight/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_eight_list_export_get(self):
        """Test case for installed_eight_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/eight/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_eight_list_get(self):
        """Test case for installed_eight_list_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/eight/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_orders_chart_get(self):
        """Test case for installed_orders_chart_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/orders/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_orders_info_export_get(self):
        """Test case for installed_orders_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/orders/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_orders_list_export_get(self):
        """Test case for installed_orders_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/orders/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_orders_list_get(self):
        """Test case for installed_orders_list_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/orders/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_out_chart_get(self):
        """Test case for installed_out_chart_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/out/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_out_info_export_get(self):
        """Test case for installed_out_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/out/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_out_list_export_get(self):
        """Test case for installed_out_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/out/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_out_list_get(self):
        """Test case for installed_out_list_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/out/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_retreat_chart_get(self):
        """Test case for installed_retreat_chart_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/retreat/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_retreat_info_export_get(self):
        """Test case for installed_retreat_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/retreat/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_retreat_list_export_get(self):
        """Test case for installed_retreat_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/retreat/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_retreat_list_get(self):
        """Test case for installed_retreat_list_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/retreat/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_satisfaction_chart_get(self):
        """Test case for installed_satisfaction_chart_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/satisfaction/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_satisfaction_info_export_get(self):
        """Test case for installed_satisfaction_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/satisfaction/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_satisfaction_list_export_get(self):
        """Test case for installed_satisfaction_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/satisfaction/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_satisfaction_list_get(self):
        """Test case for installed_satisfaction_list_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/satisfaction/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_top_chart_get(self):
        """Test case for installed_top_chart_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/top/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_top_info_export_get(self):
        """Test case for installed_top_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/top/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_top_list_export_get(self):
        """Test case for installed_top_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/top/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_top_list_get(self):
        """Test case for installed_top_list_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/top/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_twenty_four_chart_get(self):
        """Test case for installed_twenty_four_chart_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/twentyFour/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_twenty_four_info_export_get(self):
        """Test case for installed_twenty_four_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/twentyFour/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_twenty_four_list_export_get(self):
        """Test case for installed_twenty_four_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/twentyFour/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installed_twenty_four_list_get(self):
        """Test case for installed_twenty_four_list_get

        Installed Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/installed/twentyFour/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
