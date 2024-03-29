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

class RppResultUrlsHistoryInner(object):
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
        'keyword': 'str',
        'urls_history': 'list[object]'
    }

    attribute_map = {
        'keyword': 'keyword',
        'urls_history': 'urls_history'
    }

    def __init__(self, keyword=None, urls_history=None):  # noqa: E501
        """RppResultUrlsHistoryInner - a model defined in Swagger"""  # noqa: E501
        self._keyword = None
        self._urls_history = None
        self.discriminator = None
        if keyword is not None:
            self.keyword = keyword
        if urls_history is not None:
            self.urls_history = urls_history

    @property
    def keyword(self):
        """Gets the keyword of this RppResultUrlsHistoryInner.  # noqa: E501


        :return: The keyword of this RppResultUrlsHistoryInner.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this RppResultUrlsHistoryInner.


        :param keyword: The keyword of this RppResultUrlsHistoryInner.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def urls_history(self):
        """Gets the urls_history of this RppResultUrlsHistoryInner.  # noqa: E501


        :return: The urls_history of this RppResultUrlsHistoryInner.  # noqa: E501
        :rtype: list[object]
        """
        return self._urls_history

    @urls_history.setter
    def urls_history(self, urls_history):
        """Sets the urls_history of this RppResultUrlsHistoryInner.


        :param urls_history: The urls_history of this RppResultUrlsHistoryInner.  # noqa: E501
        :type: list[object]
        """

        self._urls_history = urls_history

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
        if issubclass(RppResultUrlsHistoryInner, dict):
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
        if not isinstance(other, RppResultUrlsHistoryInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
