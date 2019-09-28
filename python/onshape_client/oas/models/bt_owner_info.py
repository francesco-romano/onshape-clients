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


class BTOwnerInfo(object):
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
        'image': 'str',
        'is_enterprise_owned_resource': 'bool',
        'accept_ownership_transfer': 'bool',
        'type': 'int',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str'
    }

    attribute_map = {
        'image': 'image',
        'is_enterprise_owned_resource': 'isEnterpriseOwnedResource',
        'accept_ownership_transfer': 'acceptOwnershipTransfer',
        'type': 'type',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name'
    }

    def __init__(self, image=None, is_enterprise_owned_resource=None, accept_ownership_transfer=None, type=None, id=None, href=None, view_ref=None, name=None):  # noqa: E501
        """BTOwnerInfo - a model defined in OpenAPI"""  # noqa: E501

        self._image = None
        self._is_enterprise_owned_resource = None
        self._accept_ownership_transfer = None
        self._type = None
        self._id = None
        self._href = None
        self._view_ref = None
        self._name = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if is_enterprise_owned_resource is not None:
            self.is_enterprise_owned_resource = is_enterprise_owned_resource
        if accept_ownership_transfer is not None:
            self.accept_ownership_transfer = accept_ownership_transfer
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name

    @property
    def image(self):
        """Gets the image of this BTOwnerInfo.  # noqa: E501


        :return: The image of this BTOwnerInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this BTOwnerInfo.


        :param image: The image of this BTOwnerInfo.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def is_enterprise_owned_resource(self):
        """Gets the is_enterprise_owned_resource of this BTOwnerInfo.  # noqa: E501


        :return: The is_enterprise_owned_resource of this BTOwnerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_enterprise_owned_resource

    @is_enterprise_owned_resource.setter
    def is_enterprise_owned_resource(self, is_enterprise_owned_resource):
        """Sets the is_enterprise_owned_resource of this BTOwnerInfo.


        :param is_enterprise_owned_resource: The is_enterprise_owned_resource of this BTOwnerInfo.  # noqa: E501
        :type: bool
        """

        self._is_enterprise_owned_resource = is_enterprise_owned_resource

    @property
    def accept_ownership_transfer(self):
        """Gets the accept_ownership_transfer of this BTOwnerInfo.  # noqa: E501


        :return: The accept_ownership_transfer of this BTOwnerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._accept_ownership_transfer

    @accept_ownership_transfer.setter
    def accept_ownership_transfer(self, accept_ownership_transfer):
        """Sets the accept_ownership_transfer of this BTOwnerInfo.


        :param accept_ownership_transfer: The accept_ownership_transfer of this BTOwnerInfo.  # noqa: E501
        :type: bool
        """

        self._accept_ownership_transfer = accept_ownership_transfer

    @property
    def type(self):
        """Gets the type of this BTOwnerInfo.  # noqa: E501


        :return: The type of this BTOwnerInfo.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTOwnerInfo.


        :param type: The type of this BTOwnerInfo.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this BTOwnerInfo.  # noqa: E501


        :return: The id of this BTOwnerInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTOwnerInfo.


        :param id: The id of this BTOwnerInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTOwnerInfo.  # noqa: E501


        :return: The href of this BTOwnerInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTOwnerInfo.


        :param href: The href of this BTOwnerInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTOwnerInfo.  # noqa: E501


        :return: The view_ref of this BTOwnerInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTOwnerInfo.


        :param view_ref: The view_ref of this BTOwnerInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTOwnerInfo.  # noqa: E501


        :return: The name of this BTOwnerInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTOwnerInfo.


        :param name: The name of this BTOwnerInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, BTOwnerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other