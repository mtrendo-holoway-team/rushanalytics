# coding: utf-8

"""
    Rush Analytics API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    Contact: support@rushanalytics.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IndexationUrl(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'yandex_indexed': 'int',
        'google_indexed': 'int'
    }

    attribute_map = {
        'url': 'url',
        'yandex_indexed': 'yandexIndexed',
        'google_indexed': 'googleIndexed'
    }

    def __init__(self, url=None, yandex_indexed=None, google_indexed=None):  # noqa: E501
        """IndexationUrl - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._yandex_indexed = None
        self._google_indexed = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if yandex_indexed is not None:
            self.yandex_indexed = yandex_indexed
        if google_indexed is not None:
            self.google_indexed = google_indexed

    @property
    def url(self):
        """Gets the url of this IndexationUrl.  # noqa: E501


        :return: The url of this IndexationUrl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IndexationUrl.


        :param url: The url of this IndexationUrl.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def yandex_indexed(self):
        """Gets the yandex_indexed of this IndexationUrl.  # noqa: E501


        :return: The yandex_indexed of this IndexationUrl.  # noqa: E501
        :rtype: int
        """
        return self._yandex_indexed

    @yandex_indexed.setter
    def yandex_indexed(self, yandex_indexed):
        """Sets the yandex_indexed of this IndexationUrl.


        :param yandex_indexed: The yandex_indexed of this IndexationUrl.  # noqa: E501
        :type: int
        """

        self._yandex_indexed = yandex_indexed

    @property
    def google_indexed(self):
        """Gets the google_indexed of this IndexationUrl.  # noqa: E501


        :return: The google_indexed of this IndexationUrl.  # noqa: E501
        :rtype: int
        """
        return self._google_indexed

    @google_indexed.setter
    def google_indexed(self, google_indexed):
        """Sets the google_indexed of this IndexationUrl.


        :param google_indexed: The google_indexed of this IndexationUrl.  # noqa: E501
        :type: int
        """

        self._google_indexed = google_indexed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IndexationUrl, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IndexationUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
