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


class BTRevisionRuleInfo(object):
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
        'revision_list': 'list[str]',
        'rule_type': 'int',
        'description': 'str',
        'company_id': 'str',
        'script': 'str',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'revision_list': 'revisionList',
        'rule_type': 'ruleType',
        'description': 'description',
        'company_id': 'companyId',
        'script': 'script',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, revision_list=None, rule_type=None, description=None, company_id=None, script=None, href=None, view_ref=None, name=None, id=None):  # noqa: E501
        """BTRevisionRuleInfo - a model defined in OpenAPI"""  # noqa: E501

        self._revision_list = None
        self._rule_type = None
        self._description = None
        self._company_id = None
        self._script = None
        self._href = None
        self._view_ref = None
        self._name = None
        self._id = None
        self.discriminator = None

        if revision_list is not None:
            self.revision_list = revision_list
        if rule_type is not None:
            self.rule_type = rule_type
        if description is not None:
            self.description = description
        if company_id is not None:
            self.company_id = company_id
        if script is not None:
            self.script = script
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def revision_list(self):
        """Gets the revision_list of this BTRevisionRuleInfo.  # noqa: E501


        :return: The revision_list of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._revision_list

    @revision_list.setter
    def revision_list(self, revision_list):
        """Sets the revision_list of this BTRevisionRuleInfo.


        :param revision_list: The revision_list of this BTRevisionRuleInfo.  # noqa: E501
        :type: list[str]
        """

        self._revision_list = revision_list

    @property
    def rule_type(self):
        """Gets the rule_type of this BTRevisionRuleInfo.  # noqa: E501


        :return: The rule_type of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this BTRevisionRuleInfo.


        :param rule_type: The rule_type of this BTRevisionRuleInfo.  # noqa: E501
        :type: int
        """

        self._rule_type = rule_type

    @property
    def description(self):
        """Gets the description of this BTRevisionRuleInfo.  # noqa: E501


        :return: The description of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTRevisionRuleInfo.


        :param description: The description of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def company_id(self):
        """Gets the company_id of this BTRevisionRuleInfo.  # noqa: E501


        :return: The company_id of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTRevisionRuleInfo.


        :param company_id: The company_id of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def script(self):
        """Gets the script of this BTRevisionRuleInfo.  # noqa: E501


        :return: The script of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this BTRevisionRuleInfo.


        :param script: The script of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def href(self):
        """Gets the href of this BTRevisionRuleInfo.  # noqa: E501


        :return: The href of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTRevisionRuleInfo.


        :param href: The href of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTRevisionRuleInfo.  # noqa: E501


        :return: The view_ref of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTRevisionRuleInfo.


        :param view_ref: The view_ref of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTRevisionRuleInfo.  # noqa: E501


        :return: The name of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTRevisionRuleInfo.


        :param name: The name of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTRevisionRuleInfo.  # noqa: E501


        :return: The id of this BTRevisionRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTRevisionRuleInfo.


        :param id: The id of this BTRevisionRuleInfo.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, BTRevisionRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
