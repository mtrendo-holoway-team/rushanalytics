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

class RppResultPositionsHistoryInner(object):
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
        'positions_history': 'list[object]'
    }

    attribute_map = {
        'keyword': 'keyword',
        'positions_history': 'positions_history'
    }

    def __init__(self, keyword=None, positions_history=None):  # noqa: E501
        """RppResultPositionsHistoryInner - a model defined in Swagger"""  # noqa: E501
        self._keyword = None
        self._positions_history = None
        self.discriminator = None
        if keyword is not None:
            self.keyword = keyword
        if positions_history is not None:
            self.positions_history = positions_history

    @property
    def keyword(self):
        """Gets the keyword of this RppResultPositionsHistoryInner.  # noqa: E501


        :return: The keyword of this RppResultPositionsHistoryInner.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this RppResultPositionsHistoryInner.


        :param keyword: The keyword of this RppResultPositionsHistoryInner.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def positions_history(self):
        """Gets the positions_history of this RppResultPositionsHistoryInner.  # noqa: E501


        :return: The positions_history of this RppResultPositionsHistoryInner.  # noqa: E501
        :rtype: list[object]
        """
        return self._positions_history

    @positions_history.setter
    def positions_history(self, positions_history):
        """Sets the positions_history of this RppResultPositionsHistoryInner.


        :param positions_history: The positions_history of this RppResultPositionsHistoryInner.  # noqa: E501
        :type: list[object]
        """

        self._positions_history = positions_history

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
        if issubclass(RppResultPositionsHistoryInner, dict):
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
        if not isinstance(other, RppResultPositionsHistoryInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
