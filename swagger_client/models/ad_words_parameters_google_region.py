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

class AdWordsParametersGoogleRegion(object):
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
        'country': 'str',
        'region': 'int',
        'language': 'str'
    }

    attribute_map = {
        'country': 'country',
        'region': 'region',
        'language': 'language'
    }

    def __init__(self, country=None, region=None, language=None):  # noqa: E501
        """AdWordsParametersGoogleRegion - a model defined in Swagger"""  # noqa: E501
        self._country = None
        self._region = None
        self._language = None
        self.discriminator = None
        if country is not None:
            self.country = country
        if region is not None:
            self.region = region
        if language is not None:
            self.language = language

    @property
    def country(self):
        """Gets the country of this AdWordsParametersGoogleRegion.  # noqa: E501


        :return: The country of this AdWordsParametersGoogleRegion.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AdWordsParametersGoogleRegion.


        :param country: The country of this AdWordsParametersGoogleRegion.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def region(self):
        """Gets the region of this AdWordsParametersGoogleRegion.  # noqa: E501


        :return: The region of this AdWordsParametersGoogleRegion.  # noqa: E501
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AdWordsParametersGoogleRegion.


        :param region: The region of this AdWordsParametersGoogleRegion.  # noqa: E501
        :type: int
        """

        self._region = region

    @property
    def language(self):
        """Gets the language of this AdWordsParametersGoogleRegion.  # noqa: E501


        :return: The language of this AdWordsParametersGoogleRegion.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AdWordsParametersGoogleRegion.


        :param language: The language of this AdWordsParametersGoogleRegion.  # noqa: E501
        :type: str
        """

        self._language = language

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
        if issubclass(AdWordsParametersGoogleRegion, dict):
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
        if not isinstance(other, AdWordsParametersGoogleRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
