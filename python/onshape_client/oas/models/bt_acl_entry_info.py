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


class BTAclEntryInfo(object):
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
        'entry_type': 'int',
        'entry_id': 'str',
        'email': 'str',
        'permission_set': 'object',
        'image': 'str',
        'entry_state': 'str',
        'enterprise_member': 'bool',
        'pending_owner_transfer': 'bool',
        'accept_owner_transfer': 'bool',
        'object_id': 'str',
        'team_name': 'str',
        'company_name': 'str',
        'name': 'str',
        'permission': 'int'
    }

    attribute_map = {
        'entry_type': 'entryType',
        'entry_id': 'entryId',
        'email': 'email',
        'permission_set': 'permissionSet',
        'image': 'image',
        'entry_state': 'entryState',
        'enterprise_member': 'enterpriseMember',
        'pending_owner_transfer': 'pendingOwnerTransfer',
        'accept_owner_transfer': 'acceptOwnerTransfer',
        'object_id': 'objectId',
        'team_name': 'teamName',
        'company_name': 'companyName',
        'name': 'name',
        'permission': 'permission'
    }

    def __init__(self, entry_type=None, entry_id=None, email=None, permission_set=None, image=None, entry_state=None, enterprise_member=None, pending_owner_transfer=None, accept_owner_transfer=None, object_id=None, team_name=None, company_name=None, name=None, permission=None):  # noqa: E501
        """BTAclEntryInfo - a model defined in OpenAPI"""  # noqa: E501

        self._entry_type = None
        self._entry_id = None
        self._email = None
        self._permission_set = None
        self._image = None
        self._entry_state = None
        self._enterprise_member = None
        self._pending_owner_transfer = None
        self._accept_owner_transfer = None
        self._object_id = None
        self._team_name = None
        self._company_name = None
        self._name = None
        self._permission = None
        self.discriminator = None

        if entry_type is not None:
            self.entry_type = entry_type
        if entry_id is not None:
            self.entry_id = entry_id
        if email is not None:
            self.email = email
        if permission_set is not None:
            self.permission_set = permission_set
        if image is not None:
            self.image = image
        if entry_state is not None:
            self.entry_state = entry_state
        if enterprise_member is not None:
            self.enterprise_member = enterprise_member
        if pending_owner_transfer is not None:
            self.pending_owner_transfer = pending_owner_transfer
        if accept_owner_transfer is not None:
            self.accept_owner_transfer = accept_owner_transfer
        if object_id is not None:
            self.object_id = object_id
        if team_name is not None:
            self.team_name = team_name
        if company_name is not None:
            self.company_name = company_name
        if name is not None:
            self.name = name
        if permission is not None:
            self.permission = permission

    @property
    def entry_type(self):
        """Gets the entry_type of this BTAclEntryInfo.  # noqa: E501


        :return: The entry_type of this BTAclEntryInfo.  # noqa: E501
        :rtype: int
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this BTAclEntryInfo.


        :param entry_type: The entry_type of this BTAclEntryInfo.  # noqa: E501
        :type: int
        """

        self._entry_type = entry_type

    @property
    def entry_id(self):
        """Gets the entry_id of this BTAclEntryInfo.  # noqa: E501


        :return: The entry_id of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this BTAclEntryInfo.


        :param entry_id: The entry_id of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._entry_id = entry_id

    @property
    def email(self):
        """Gets the email of this BTAclEntryInfo.  # noqa: E501


        :return: The email of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTAclEntryInfo.


        :param email: The email of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def permission_set(self):
        """Gets the permission_set of this BTAclEntryInfo.  # noqa: E501


        :return: The permission_set of this BTAclEntryInfo.  # noqa: E501
        :rtype: object
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this BTAclEntryInfo.


        :param permission_set: The permission_set of this BTAclEntryInfo.  # noqa: E501
        :type: object
        """

        self._permission_set = permission_set

    @property
    def image(self):
        """Gets the image of this BTAclEntryInfo.  # noqa: E501


        :return: The image of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this BTAclEntryInfo.


        :param image: The image of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def entry_state(self):
        """Gets the entry_state of this BTAclEntryInfo.  # noqa: E501


        :return: The entry_state of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._entry_state

    @entry_state.setter
    def entry_state(self, entry_state):
        """Sets the entry_state of this BTAclEntryInfo.


        :param entry_state: The entry_state of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETED", "ACTIVE", "INACTIVE", "REQUESTED", "APPROVED", "REQUEST_EXPIRED", "ALL", "MARKED_FOR_DELETION"]  # noqa: E501
        if entry_state not in allowed_values:
            raise ValueError(
                "Invalid value for `entry_state` ({0}), must be one of {1}"  # noqa: E501
                .format(entry_state, allowed_values)
            )

        self._entry_state = entry_state

    @property
    def enterprise_member(self):
        """Gets the enterprise_member of this BTAclEntryInfo.  # noqa: E501


        :return: The enterprise_member of this BTAclEntryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enterprise_member

    @enterprise_member.setter
    def enterprise_member(self, enterprise_member):
        """Sets the enterprise_member of this BTAclEntryInfo.


        :param enterprise_member: The enterprise_member of this BTAclEntryInfo.  # noqa: E501
        :type: bool
        """

        self._enterprise_member = enterprise_member

    @property
    def pending_owner_transfer(self):
        """Gets the pending_owner_transfer of this BTAclEntryInfo.  # noqa: E501


        :return: The pending_owner_transfer of this BTAclEntryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._pending_owner_transfer

    @pending_owner_transfer.setter
    def pending_owner_transfer(self, pending_owner_transfer):
        """Sets the pending_owner_transfer of this BTAclEntryInfo.


        :param pending_owner_transfer: The pending_owner_transfer of this BTAclEntryInfo.  # noqa: E501
        :type: bool
        """

        self._pending_owner_transfer = pending_owner_transfer

    @property
    def accept_owner_transfer(self):
        """Gets the accept_owner_transfer of this BTAclEntryInfo.  # noqa: E501


        :return: The accept_owner_transfer of this BTAclEntryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._accept_owner_transfer

    @accept_owner_transfer.setter
    def accept_owner_transfer(self, accept_owner_transfer):
        """Sets the accept_owner_transfer of this BTAclEntryInfo.


        :param accept_owner_transfer: The accept_owner_transfer of this BTAclEntryInfo.  # noqa: E501
        :type: bool
        """

        self._accept_owner_transfer = accept_owner_transfer

    @property
    def object_id(self):
        """Gets the object_id of this BTAclEntryInfo.  # noqa: E501


        :return: The object_id of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this BTAclEntryInfo.


        :param object_id: The object_id of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def team_name(self):
        """Gets the team_name of this BTAclEntryInfo.  # noqa: E501


        :return: The team_name of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this BTAclEntryInfo.


        :param team_name: The team_name of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._team_name = team_name

    @property
    def company_name(self):
        """Gets the company_name of this BTAclEntryInfo.  # noqa: E501


        :return: The company_name of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this BTAclEntryInfo.


        :param company_name: The company_name of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def name(self):
        """Gets the name of this BTAclEntryInfo.  # noqa: E501


        :return: The name of this BTAclEntryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTAclEntryInfo.


        :param name: The name of this BTAclEntryInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permission(self):
        """Gets the permission of this BTAclEntryInfo.  # noqa: E501


        :return: The permission of this BTAclEntryInfo.  # noqa: E501
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this BTAclEntryInfo.


        :param permission: The permission of this BTAclEntryInfo.  # noqa: E501
        :type: int
        """

        self._permission = permission

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
        if not isinstance(other, BTAclEntryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
