# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.export import Export  # noqa: E501
from swagger_server.models.maintain_list import MaintainList  # noqa: E501
from swagger_server.models.out_data import OutData  # noqa: E501
from swagger_server.models.out_list import OutList  # noqa: E501
from swagger_server.models.statistics_install_list import StatisticsInstallList  # noqa: E501
from swagger_server.models.statistics_work_list import StatisticsWorkList  # noqa: E501
from swagger_server.models.storage_data import StorageData  # noqa: E501
from swagger_server.models.storage_data_edit import StorageDataEdit  # noqa: E501
from swagger_server.models.storage_list import StorageList  # noqa: E501
from swagger_server.models.storage_query import StorageQuery  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.supplies_query import SuppliesQuery  # noqa: E501
from swagger_server.models.use_codes import UseCodes  # noqa: E501
from swagger_server.models.use_list import UseList  # noqa: E501
from swagger_server.models.waste_list import WasteList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSuppliesController(BaseTestCase):
    """SuppliesController integration test stubs"""

    def test_supplies_maintain_export_get(self):
        """Test case for supplies_maintain_export_get

        maintain list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/maintain/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_maintain_get(self):
        """Test case for supplies_maintain_get

        maintain list
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/maintain',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_maintain_upload_post(self):
        """Test case for supplies_maintain_upload_post

        Install usage details import
        """
        data = dict(files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/v1/supplies/maintain/upload',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_out_export_get(self):
        """Test case for supplies_out_export_get

        Inventory list
        """
        query_string = [('model', 'model_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/out/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_out_get(self):
        """Test case for supplies_out_get

        Inventory list
        """
        query_string = [('model', 'model_example'),
                        ('page', 'page_example'),
                        ('size', 'size_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/out',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_out_post(self):
        """Test case for supplies_out_post

        Product warehousing
        """
        body = OutData()
        response = self.client.open(
            '/v1/supplies/out',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_query_code_get(self):
        """Test case for supplies_query_code_get

        According to the challenge, check the terminal status
        """
        response = self.client.open(
            '/v1/supplies/query/{code}'.format(code='code_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_statistics_install_export_get(self):
        """Test case for supplies_statistics_install_export_get

        Personnel statistics
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('type', 'type_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('model', 'model_example'),
                        ('people', 'people_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/statistics/install/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_statistics_install_get(self):
        """Test case for supplies_statistics_install_get

        Personnel statistics
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('type', 'type_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('model', 'model_example'),
                        ('people', 'people_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/statistics/install',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_statistics_work_export_get(self):
        """Test case for supplies_statistics_work_export_get

        Workstation installation dimension statistics
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('type', 'type_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('model', 'model_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/statistics/work/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_statistics_work_get(self):
        """Test case for supplies_statistics_work_get

        Workstation installation dimension statistics
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('type', 'type_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('model', 'model_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/statistics/work',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_storage_delete(self):
        """Test case for supplies_storage_delete

        Delete inventory
        """
        query_string = [('id', 56)]
        response = self.client.open(
            '/v1/supplies/storage',
            method='DELETE',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_storage_export_get(self):
        """Test case for supplies_storage_export_get

        Inventory list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('model', 'model_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/storage/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_storage_get(self):
        """Test case for supplies_storage_get

        Inventory list
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('model', 'model_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/storage',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_storage_post(self):
        """Test case for supplies_storage_post

        Product warehousing
        """
        body = StorageData()
        response = self.client.open(
            '/v1/supplies/storage',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_storage_put(self):
        """Test case for supplies_storage_put

        Edit inventory
        """
        body = StorageDataEdit()
        response = self.client.open(
            '/v1/supplies/storage',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_storage_query_code_get(self):
        """Test case for supplies_storage_query_code_get

        Inventory list
        """
        response = self.client.open(
            '/v1/supplies/storage/query/{code}'.format(code='code_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_use_code_id_get(self):
        """Test case for supplies_use_code_id_get

        Query a few devices and barcodes in the current work order
        """
        response = self.client.open(
            '/v1/supplies/use/code/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_use_export_get(self):
        """Test case for supplies_use_export_get

        Inventory list
        """
        query_string = [('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/use/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_use_get(self):
        """Test case for supplies_use_get

        Inventory list
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('type', 'type_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/use',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_use_upload_post(self):
        """Test case for supplies_use_upload_post

        Install usage details import
        """
        data = dict(files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/v1/supplies/use/upload',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_waste_export_get(self):
        """Test case for supplies_waste_export_get

        maintain list
        """
        query_string = [('type', 'type_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/waste/export',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_waste_get(self):
        """Test case for supplies_waste_get

        maintain list
        """
        query_string = [('page', 'page_example'),
                        ('size', 'size_example'),
                        ('type', 'type_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example'),
                        ('work', 'work_example'),
                        ('keyword', 'keyword_example')]
        response = self.client.open(
            '/v1/supplies/waste',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supplies_waste_upload_post(self):
        """Test case for supplies_waste_upload_post

        Install usage details import
        """
        query_string = [('type', 'type_example')]
        data = dict(files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/v1/supplies/waste/upload',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
