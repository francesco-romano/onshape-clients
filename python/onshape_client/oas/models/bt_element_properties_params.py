# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.103
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTElementPropertiesParams(object):
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
        'element_id': 'str',
        'api_configuration': 'str',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'element_id': 'elementId',
        'api_configuration': 'apiConfiguration',
        'properties': 'properties'
    }

    def __init__(self, element_id=None, api_configuration=None, properties=None):  # noqa: E501
        """BTElementPropertiesParams - a model defined in OpenAPI"""  # noqa: E501

        self._element_id = None
        self._api_configuration = None
        self._properties = None
        self.discriminator = None

        if element_id is not None:
            self.element_id = element_id
        if api_configuration is not None:
            self.api_configuration = api_configuration
        if properties is not None:
            self.properties = properties

    @property
    def element_id(self):
        """Gets the element_id of this BTElementPropertiesParams.  # noqa: E501


        :return: The element_id of this BTElementPropertiesParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTElementPropertiesParams.


        :param element_id: The element_id of this BTElementPropertiesParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def api_configuration(self):
        """Gets the api_configuration of this BTElementPropertiesParams.  # noqa: E501


        :return: The api_configuration of this BTElementPropertiesParams.  # noqa: E501
        :rtype: str
        """
        return self._api_configuration

    @api_configuration.setter
    def api_configuration(self, api_configuration):
        """Sets the api_configuration of this BTElementPropertiesParams.


        :param api_configuration: The api_configuration of this BTElementPropertiesParams.  # noqa: E501
        :type: str
        """

        self._api_configuration = api_configuration

    @property
    def properties(self):
        """Gets the properties of this BTElementPropertiesParams.  # noqa: E501


        :return: The properties of this BTElementPropertiesParams.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BTElementPropertiesParams.


        :param properties: The properties of this BTElementPropertiesParams.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

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
        if not isinstance(other, BTElementPropertiesParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
