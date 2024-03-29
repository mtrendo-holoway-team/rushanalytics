# coding: utf-8

"""
    Rush Analytics API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    Contact: support@rushanalytics.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.gds_api import GdsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGdsApi(unittest.TestCase):
    """GdsApi unit test stubs"""

    def setUp(self):
        self.api = GdsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gds_competitors_visibility(self):
        """Test case for gds_competitors_visibility

        Get competitors visibility data of your rank tracker project for Google Data Studio  # noqa: E501
        """
        pass

    def test_gds_positions(self):
        """Test case for gds_positions

        Get positions history of your rank tracker project for Google Data Studio  # noqa: E501
        """
        pass

    def test_gds_schema(self):
        """Test case for gds_schema

        Get schema of your rank tracker project for Google Data Studio  # noqa: E501
        """
        pass

    def test_gds_tops(self):
        """Test case for gds_tops

        Get tops (100,30,10,5,3) data of your rank tracker project for Google Data Studio  # noqa: E501
        """
        pass

    def test_gds_visibility(self):
        """Test case for gds_visibility

        Get competitors visibility data of your rank tracker project for Google Data Studio  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()