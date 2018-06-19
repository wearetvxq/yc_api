# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.out_data import OutData  # noqa: E501
from swagger_server.models.outcommit import Outcommit  # noqa: E501
from swagger_server.models.outlist import Outlist  # noqa: E501
from swagger_server.models.phone_maintain_lists import PhoneMaintainLists  # noqa: E501
from swagger_server.models.phone_use_lists import PhoneUseLists  # noqa: E501
from swagger_server.models.phonetoken import Phonetoken  # noqa: E501
from swagger_server.models.phonetokens import Phonetokens  # noqa: E501
from swagger_server.models.storage_data import StorageData  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPhoneController(BaseTestCase):
    """PhoneController integration test stubs"""

    def test_phone_login_post(self):
        """Test case for phone_login_post

        phone Product warehousing
        """
        body = Login()
        response = self.client.open(
            '/v1/phone/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_maintain_post(self):
        """Test case for phone_maintain_post

        phone maintain post
        """
        body = PhoneMaintainLists()
        response = self.client.open(
            '/v1/phone/maintain',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_out_post(self):
        """Test case for phone_out_post

        phone Product warehousing
        """
        body = OutData()
        response = self.client.open(
            '/v1/phone/out',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_outcommit_post(self):
        """Test case for phone_outcommit_post

        phone Product warehousing
        """
        body = Outcommit()
        response = self.client.open(
            '/v1/phone/outcommit',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_outlist_post(self):
        """Test case for phone_outlist_post

        phone Product warehousing
        """
        body = Outlist()
        response = self.client.open(
            '/v1/phone/outlist',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_storage_post(self):
        """Test case for phone_storage_post

        phone Product warehousing
        """
        body = StorageData()
        response = self.client.open(
            '/v1/phone/storage',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_token_post(self):
        """Test case for phone_token_post

        phone maintain post
        """
        body = Phonetoken()
        response = self.client.open(
            '/v1/phone/token',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_use_post(self):
        """Test case for phone_use_post

        phone use post
        """
        body = PhoneUseLists()
        response = self.client.open(
            '/v1/phone/use',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
