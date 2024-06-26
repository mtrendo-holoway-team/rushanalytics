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

class CreateRppDataCollectionFrequency(object):
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
        'frequency': 'int',
        'days': 'str',
        'hour': 'int'
    }

    attribute_map = {
        'frequency': 'frequency',
        'days': 'days',
        'hour': 'hour'
    }

    def __init__(self, frequency=None, days=None, hour=None):  # noqa: E501
        """CreateRppDataCollectionFrequency - a model defined in Swagger"""  # noqa: E501
        self._frequency = None
        self._days = None
        self._hour = None
        self.discriminator = None
        if frequency is not None:
            self.frequency = frequency
        if days is not None:
            self.days = days
        if hour is not None:
            self.hour = hour

    @property
    def frequency(self):
        """Gets the frequency of this CreateRppDataCollectionFrequency.  # noqa: E501


        :return: The frequency of this CreateRppDataCollectionFrequency.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this CreateRppDataCollectionFrequency.


        :param frequency: The frequency of this CreateRppDataCollectionFrequency.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def days(self):
        """Gets the days of this CreateRppDataCollectionFrequency.  # noqa: E501


        :return: The days of this CreateRppDataCollectionFrequency.  # noqa: E501
        :rtype: str
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this CreateRppDataCollectionFrequency.


        :param days: The days of this CreateRppDataCollectionFrequency.  # noqa: E501
        :type: str
        """

        self._days = days

    @property
    def hour(self):
        """Gets the hour of this CreateRppDataCollectionFrequency.  # noqa: E501


        :return: The hour of this CreateRppDataCollectionFrequency.  # noqa: E501
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this CreateRppDataCollectionFrequency.


        :param hour: The hour of this CreateRppDataCollectionFrequency.  # noqa: E501
        :type: int
        """

        self._hour = hour

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
        if issubclass(CreateRppDataCollectionFrequency, dict):
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
        if not isinstance(other, CreateRppDataCollectionFrequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
