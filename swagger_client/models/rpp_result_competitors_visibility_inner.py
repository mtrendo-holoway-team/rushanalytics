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

class RppResultCompetitorsVisibilityInner(object):
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
        'competitor': 'str',
        'visibilities': 'list[object]'
    }

    attribute_map = {
        'competitor': 'competitor',
        'visibilities': 'visibilities'
    }

    def __init__(self, competitor=None, visibilities=None):  # noqa: E501
        """RppResultCompetitorsVisibilityInner - a model defined in Swagger"""  # noqa: E501
        self._competitor = None
        self._visibilities = None
        self.discriminator = None
        if competitor is not None:
            self.competitor = competitor
        if visibilities is not None:
            self.visibilities = visibilities

    @property
    def competitor(self):
        """Gets the competitor of this RppResultCompetitorsVisibilityInner.  # noqa: E501


        :return: The competitor of this RppResultCompetitorsVisibilityInner.  # noqa: E501
        :rtype: str
        """
        return self._competitor

    @competitor.setter
    def competitor(self, competitor):
        """Sets the competitor of this RppResultCompetitorsVisibilityInner.


        :param competitor: The competitor of this RppResultCompetitorsVisibilityInner.  # noqa: E501
        :type: str
        """

        self._competitor = competitor

    @property
    def visibilities(self):
        """Gets the visibilities of this RppResultCompetitorsVisibilityInner.  # noqa: E501


        :return: The visibilities of this RppResultCompetitorsVisibilityInner.  # noqa: E501
        :rtype: list[object]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """Sets the visibilities of this RppResultCompetitorsVisibilityInner.


        :param visibilities: The visibilities of this RppResultCompetitorsVisibilityInner.  # noqa: E501
        :type: list[object]
        """

        self._visibilities = visibilities

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
        if issubclass(RppResultCompetitorsVisibilityInner, dict):
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
        if not isinstance(other, RppResultCompetitorsVisibilityInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
