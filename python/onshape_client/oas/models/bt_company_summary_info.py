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


class BTCompanySummaryInfo(object):
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
        'no_public_documents': 'bool',
        'enterprise_base_url': 'str',
        'description': 'str',
        'image': 'str',
        'admin': 'bool',
        'owner_id': 'str',
        'domain_prefix': 'str',
        'type': 'int',
        'state': 'int',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str'
    }

    attribute_map = {
        'no_public_documents': 'noPublicDocuments',
        'enterprise_base_url': 'enterpriseBaseUrl',
        'description': 'description',
        'image': 'image',
        'admin': 'admin',
        'owner_id': 'ownerId',
        'domain_prefix': 'domainPrefix',
        'type': 'type',
        'state': 'state',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name'
    }

    def __init__(self, no_public_documents=None, enterprise_base_url=None, description=None, image=None, admin=None, owner_id=None, domain_prefix=None, type=None, state=None, id=None, href=None, view_ref=None, name=None):  # noqa: E501
        """BTCompanySummaryInfo - a model defined in OpenAPI"""  # noqa: E501

        self._no_public_documents = None
        self._enterprise_base_url = None
        self._description = None
        self._image = None
        self._admin = None
        self._owner_id = None
        self._domain_prefix = None
        self._type = None
        self._state = None
        self._id = None
        self._href = None
        self._view_ref = None
        self._name = None
        self.discriminator = None

        if no_public_documents is not None:
            self.no_public_documents = no_public_documents
        if enterprise_base_url is not None:
            self.enterprise_base_url = enterprise_base_url
        if description is not None:
            self.description = description
        if image is not None:
            self.image = image
        if admin is not None:
            self.admin = admin
        if owner_id is not None:
            self.owner_id = owner_id
        if domain_prefix is not None:
            self.domain_prefix = domain_prefix
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name

    @property
    def no_public_documents(self):
        """Gets the no_public_documents of this BTCompanySummaryInfo.  # noqa: E501


        :return: The no_public_documents of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._no_public_documents

    @no_public_documents.setter
    def no_public_documents(self, no_public_documents):
        """Sets the no_public_documents of this BTCompanySummaryInfo.


        :param no_public_documents: The no_public_documents of this BTCompanySummaryInfo.  # noqa: E501
        :type: bool
        """

        self._no_public_documents = no_public_documents

    @property
    def enterprise_base_url(self):
        """Gets the enterprise_base_url of this BTCompanySummaryInfo.  # noqa: E501


        :return: The enterprise_base_url of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._enterprise_base_url

    @enterprise_base_url.setter
    def enterprise_base_url(self, enterprise_base_url):
        """Sets the enterprise_base_url of this BTCompanySummaryInfo.


        :param enterprise_base_url: The enterprise_base_url of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._enterprise_base_url = enterprise_base_url

    @property
    def description(self):
        """Gets the description of this BTCompanySummaryInfo.  # noqa: E501


        :return: The description of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTCompanySummaryInfo.


        :param description: The description of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image(self):
        """Gets the image of this BTCompanySummaryInfo.  # noqa: E501


        :return: The image of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this BTCompanySummaryInfo.


        :param image: The image of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def admin(self):
        """Gets the admin of this BTCompanySummaryInfo.  # noqa: E501


        :return: The admin of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this BTCompanySummaryInfo.


        :param admin: The admin of this BTCompanySummaryInfo.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def owner_id(self):
        """Gets the owner_id of this BTCompanySummaryInfo.  # noqa: E501


        :return: The owner_id of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTCompanySummaryInfo.


        :param owner_id: The owner_id of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def domain_prefix(self):
        """Gets the domain_prefix of this BTCompanySummaryInfo.  # noqa: E501


        :return: The domain_prefix of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._domain_prefix

    @domain_prefix.setter
    def domain_prefix(self, domain_prefix):
        """Sets the domain_prefix of this BTCompanySummaryInfo.


        :param domain_prefix: The domain_prefix of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._domain_prefix = domain_prefix

    @property
    def type(self):
        """Gets the type of this BTCompanySummaryInfo.  # noqa: E501


        :return: The type of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTCompanySummaryInfo.


        :param type: The type of this BTCompanySummaryInfo.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def state(self):
        """Gets the state of this BTCompanySummaryInfo.  # noqa: E501


        :return: The state of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTCompanySummaryInfo.


        :param state: The state of this BTCompanySummaryInfo.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def id(self):
        """Gets the id of this BTCompanySummaryInfo.  # noqa: E501


        :return: The id of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTCompanySummaryInfo.


        :param id: The id of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTCompanySummaryInfo.  # noqa: E501


        :return: The href of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTCompanySummaryInfo.


        :param href: The href of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTCompanySummaryInfo.  # noqa: E501


        :return: The view_ref of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTCompanySummaryInfo.


        :param view_ref: The view_ref of this BTCompanySummaryInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTCompanySummaryInfo.  # noqa: E501


        :return: The name of this BTCompanySummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTCompanySummaryInfo.


        :param name: The name of this BTCompanySummaryInfo.  # noqa: E501
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
        if not isinstance(other, BTCompanySummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other