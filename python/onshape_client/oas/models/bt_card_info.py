# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.104
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTCardInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'last4': 'str',
        'exp_month': 'int',
        'exp_year': 'int',
        'billing_address': 'BTAddressInfo',
        'type': 'str'
    }

    attribute_map = {
        'last4': 'last4',
        'exp_month': 'expMonth',
        'exp_year': 'expYear',
        'billing_address': 'billingAddress',
        'type': 'type'
    }

    def __init__(self, last4=None, exp_month=None, exp_year=None, billing_address=None, type=None):  # noqa: E501
        """BTCardInfo - a model defined in OpenAPI"""  # noqa: E501

        self._last4 = None
        self._exp_month = None
        self._exp_year = None
        self._billing_address = None
        self._type = None
        self.discriminator = None

        if last4 is not None:
            self.last4 = last4
        if exp_month is not None:
            self.exp_month = exp_month
        if exp_year is not None:
            self.exp_year = exp_year
        if billing_address is not None:
            self.billing_address = billing_address
        if type is not None:
            self.type = type

    @property
    def last4(self):
        """Gets the last4 of this BTCardInfo.  # noqa: E501


        :return: The last4 of this BTCardInfo.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this BTCardInfo.


        :param last4: The last4 of this BTCardInfo.  # noqa: E501
        :type: str
        """

        self._last4 = last4

    @property
    def exp_month(self):
        """Gets the exp_month of this BTCardInfo.  # noqa: E501


        :return: The exp_month of this BTCardInfo.  # noqa: E501
        :rtype: int
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """Sets the exp_month of this BTCardInfo.


        :param exp_month: The exp_month of this BTCardInfo.  # noqa: E501
        :type: int
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """Gets the exp_year of this BTCardInfo.  # noqa: E501


        :return: The exp_year of this BTCardInfo.  # noqa: E501
        :rtype: int
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """Sets the exp_year of this BTCardInfo.


        :param exp_year: The exp_year of this BTCardInfo.  # noqa: E501
        :type: int
        """

        self._exp_year = exp_year

    @property
    def billing_address(self):
        """Gets the billing_address of this BTCardInfo.  # noqa: E501


        :return: The billing_address of this BTCardInfo.  # noqa: E501
        :rtype: BTAddressInfo
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this BTCardInfo.


        :param billing_address: The billing_address of this BTCardInfo.  # noqa: E501
        :type: BTAddressInfo
        """

        self._billing_address = billing_address

    @property
    def type(self):
        """Gets the type of this BTCardInfo.  # noqa: E501


        :return: The type of this BTCardInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTCardInfo.


        :param type: The type of this BTCardInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTCardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
