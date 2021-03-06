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


class BTAdminTaskParams(object):
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
        'force': 'bool',
        'task_name': 'str',
        'task_names': 'list[str]',
        'message': 'str'
    }

    attribute_map = {
        'force': 'force',
        'task_name': 'taskName',
        'task_names': 'taskNames',
        'message': 'message'
    }

    def __init__(self, force=None, task_name=None, task_names=None, message=None):  # noqa: E501
        """BTAdminTaskParams - a model defined in OpenAPI"""  # noqa: E501

        self._force = None
        self._task_name = None
        self._task_names = None
        self._message = None
        self.discriminator = None

        if force is not None:
            self.force = force
        if task_name is not None:
            self.task_name = task_name
        if task_names is not None:
            self.task_names = task_names
        if message is not None:
            self.message = message

    @property
    def force(self):
        """Gets the force of this BTAdminTaskParams.  # noqa: E501


        :return: The force of this BTAdminTaskParams.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this BTAdminTaskParams.


        :param force: The force of this BTAdminTaskParams.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def task_name(self):
        """Gets the task_name of this BTAdminTaskParams.  # noqa: E501


        :return: The task_name of this BTAdminTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this BTAdminTaskParams.


        :param task_name: The task_name of this BTAdminTaskParams.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def task_names(self):
        """Gets the task_names of this BTAdminTaskParams.  # noqa: E501


        :return: The task_names of this BTAdminTaskParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_names

    @task_names.setter
    def task_names(self, task_names):
        """Sets the task_names of this BTAdminTaskParams.


        :param task_names: The task_names of this BTAdminTaskParams.  # noqa: E501
        :type: list[str]
        """

        self._task_names = task_names

    @property
    def message(self):
        """Gets the message of this BTAdminTaskParams.  # noqa: E501


        :return: The message of this BTAdminTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BTAdminTaskParams.


        :param message: The message of this BTAdminTaskParams.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, BTAdminTaskParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
