# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.down_url import DownUrl  # noqa: E501
from swagger_server.models.eight_list import EightList  # noqa: E501
from swagger_server.models.emos_first_chart import EmosFirstChart  # noqa: E501
from swagger_server.models.emos_list import EmosList  # noqa: E501
from swagger_server.models.high_chart import HighChart  # noqa: E501
from swagger_server.models.high_list import HighList  # noqa: E501
from swagger_server.models.high_list_community_column import HighListCommunityColumn  # noqa: E501
from swagger_server.models.high_list_community_total import HighListCommunityTotal  # noqa: E501
from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.malfunction_list import MalfunctionList  # noqa: E501
from swagger_server.models.network_list import NetworkList  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.top_list import TopList  # noqa: E501
from swagger_server.models.twenty_list import TwentyList  # noqa: E501
from swagger_server.models.visit_list import VisitList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestComplainController(BaseTestCase):
    """ComplainController integration test stubs"""

    def test_complain_eight_chart_get(self):
        """Test case for complain_eight_chart_get

        eight hour complaint daily chart
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/eight/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_eight_info_export_get(self):
        """Test case for complain_eight_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/eight/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_eight_list_export_get(self):
        """Test case for complain_eight_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/eight/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_eight_list_get(self):
        """Test case for complain_eight_list_get

        eight hour complaint daily list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/eight/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_emos_first_chart_get(self):
        """Test case for complain_emos_first_chart_get

        emos Timely acceptance rate
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/emosFirst/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_emos_first_info_export_get(self):
        """Test case for complain_emos_first_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/emosFirst/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_emos_first_list_export_get(self):
        """Test case for complain_emos_first_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/emosFirst/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_emos_first_list_get(self):
        """Test case for complain_emos_first_list_get

        eight hour complaint daily list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/emosFirst/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_high_chart_get(self):
        """Test case for complain_high_chart_get

        High-frequency cell
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/high/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_high_column_get(self):
        """Test case for complain_high_column_get

        eight hour complaint daily list export
        """
        query_string = [('lat', 'lat_example'),
                        ('lon', 'lon_example')]
        response = self.client.open(
            '/v1/complain/high/column',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_high_community_id_get(self):
        """Test case for complain_high_community_id_get

        eight hour complaint daily list export
        """
        response = self.client.open(
            '/v1/complain/high/community/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_high_info_export_get(self):
        """Test case for complain_high_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/high/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_high_list_export_get(self):
        """Test case for complain_high_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/high/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_high_list_get(self):
        """Test case for complain_high_list_get

        eight hour complaint daily list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/high/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_malfunction_chart_get(self):
        """Test case for complain_malfunction_chart_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/malfunction/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_malfunction_info_export_get(self):
        """Test case for complain_malfunction_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/malfunction/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_malfunction_list_export_get(self):
        """Test case for complain_malfunction_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/malfunction/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_malfunction_list_get(self):
        """Test case for complain_malfunction_list_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/malfunction/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_network_info_export_get(self):
        """Test case for complain_network_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/network/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_network_list_export_get(self):
        """Test case for complain_network_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/network/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_network_list_get(self):
        """Test case for complain_network_list_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/network/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_out_chart_get(self):
        """Test case for complain_out_chart_get

        Overtime did not reply
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/out/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_out_info_export_get(self):
        """Test case for complain_out_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/out/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_out_list_export_get(self):
        """Test case for complain_out_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/out/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_out_list_get(self):
        """Test case for complain_out_list_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/out/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_top_chart_get(self):
        """Test case for complain_top_chart_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/top/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_top_info_export_get(self):
        """Test case for complain_top_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/top/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_top_list_export_get(self):
        """Test case for complain_top_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/top/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_top_list_get(self):
        """Test case for complain_top_list_get

        Yichang Branch Broadens Fault Daily
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/top/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_twenty_four_chart_get(self):
        """Test case for complain_twenty_four_chart_get

        24-hour complaint daily chart
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/twentyFour/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_twenty_four_info_export_get(self):
        """Test case for complain_twenty_four_info_export_get

        24-hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/twentyFour/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_twenty_four_list_export_get(self):
        """Test case for complain_twenty_four_list_export_get

        24-hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/twentyFour/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_twenty_four_list_get(self):
        """Test case for complain_twenty_four_list_get

        24-hour complaint daily list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/twentyFour/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_visit_chart_get(self):
        """Test case for complain_visit_chart_get

        Return visit satisfaction
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/visit/chart',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_visit_info_export_get(self):
        """Test case for complain_visit_info_export_get

        eight hour complaint daily list export
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/v1/complain/visit/info/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_visit_list_export_get(self):
        """Test case for complain_visit_list_export_get

        eight hour complaint daily list export
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/visit/list/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complain_visit_list_get(self):
        """Test case for complain_visit_list_get

        eight hour complaint daily list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open(
            '/v1/complain/visit/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
