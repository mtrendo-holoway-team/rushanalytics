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
from swagger_client.api.status_api import StatusApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self):
        self.api = StatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_project_status(self):
        """Test case for get_project_status

        Get status of your project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
