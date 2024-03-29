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

class RppResultCompetitorsLeadersInner(object):
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
        'top10_info': 'list[object]'
    }

    attribute_map = {
        'competitor': 'competitor',
        'top10_info': 'top10_info'
    }

    def __init__(self, competitor=None, top10_info=None):  # noqa: E501
        """RppResultCompetitorsLeadersInner - a model defined in Swagger"""  # noqa: E501
        self._competitor = None
        self._top10_info = None
        self.discriminator = None
        if competitor is not None:
            self.competitor = competitor
        if top10_info is not None:
            self.top10_info = top10_info

    @property
    def competitor(self):
        """Gets the competitor of this RppResultCompetitorsLeadersInner.  # noqa: E501


        :return: The competitor of this RppResultCompetitorsLeadersInner.  # noqa: E501
        :rtype: str
        """
        return self._competitor

    @competitor.setter
    def competitor(self, competitor):
        """Sets the competitor of this RppResultCompetitorsLeadersInner.


        :param competitor: The competitor of this RppResultCompetitorsLeadersInner.  # noqa: E501
        :type: str
        """

        self._competitor = competitor

    @property
    def top10_info(self):
        """Gets the top10_info of this RppResultCompetitorsLeadersInner.  # noqa: E501


        :return: The top10_info of this RppResultCompetitorsLeadersInner.  # noqa: E501
        :rtype: list[object]
        """
        return self._top10_info

    @top10_info.setter
    def top10_info(self, top10_info):
        """Sets the top10_info of this RppResultCompetitorsLeadersInner.


        :param top10_info: The top10_info of this RppResultCompetitorsLeadersInner.  # noqa: E501
        :type: list[object]
        """

        self._top10_info = top10_info

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
        if issubclass(RppResultCompetitorsLeadersInner, dict):
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
        if not isinstance(other, RppResultCompetitorsLeadersInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
