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


class BTFeatureScriptEvalCall(object):
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
        'queries': 'dict(str, list[str])',
        'script': 'str',
        'serialization_version': 'str',
        'library_version': 'int',
        'source_microversion': 'str',
        'reject_microversion_skew': 'bool',
        'microversion_skew': 'bool'
    }

    attribute_map = {
        'queries': 'queries',
        'script': 'script',
        'serialization_version': 'serializationVersion',
        'library_version': 'libraryVersion',
        'source_microversion': 'sourceMicroversion',
        'reject_microversion_skew': 'rejectMicroversionSkew',
        'microversion_skew': 'microversionSkew'
    }

    def __init__(self, queries=None, script=None, serialization_version=None, library_version=None, source_microversion=None, reject_microversion_skew=None, microversion_skew=None):  # noqa: E501
        """BTFeatureScriptEvalCall - a model defined in OpenAPI"""  # noqa: E501

        self._queries = None
        self._script = None
        self._serialization_version = None
        self._library_version = None
        self._source_microversion = None
        self._reject_microversion_skew = None
        self._microversion_skew = None
        self.discriminator = None

        if queries is not None:
            self.queries = queries
        if script is not None:
            self.script = script
        if serialization_version is not None:
            self.serialization_version = serialization_version
        if library_version is not None:
            self.library_version = library_version
        if source_microversion is not None:
            self.source_microversion = source_microversion
        if reject_microversion_skew is not None:
            self.reject_microversion_skew = reject_microversion_skew
        if microversion_skew is not None:
            self.microversion_skew = microversion_skew

    @property
    def queries(self):
        """Gets the queries of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The queries of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this BTFeatureScriptEvalCall.


        :param queries: The queries of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._queries = queries

    @property
    def script(self):
        """Gets the script of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The script of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this BTFeatureScriptEvalCall.


        :param script: The script of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def serialization_version(self):
        """Gets the serialization_version of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The serialization_version of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this BTFeatureScriptEvalCall.


        :param serialization_version: The serialization_version of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def library_version(self):
        """Gets the library_version of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The library_version of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: int
        """
        return self._library_version

    @library_version.setter
    def library_version(self, library_version):
        """Sets the library_version of this BTFeatureScriptEvalCall.


        :param library_version: The library_version of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: int
        """

        self._library_version = library_version

    @property
    def source_microversion(self):
        """Gets the source_microversion of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The source_microversion of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this BTFeatureScriptEvalCall.


        :param source_microversion: The source_microversion of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

    @property
    def reject_microversion_skew(self):
        """Gets the reject_microversion_skew of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The reject_microversion_skew of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: bool
        """
        return self._reject_microversion_skew

    @reject_microversion_skew.setter
    def reject_microversion_skew(self, reject_microversion_skew):
        """Sets the reject_microversion_skew of this BTFeatureScriptEvalCall.


        :param reject_microversion_skew: The reject_microversion_skew of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: bool
        """

        self._reject_microversion_skew = reject_microversion_skew

    @property
    def microversion_skew(self):
        """Gets the microversion_skew of this BTFeatureScriptEvalCall.  # noqa: E501


        :return: The microversion_skew of this BTFeatureScriptEvalCall.  # noqa: E501
        :rtype: bool
        """
        return self._microversion_skew

    @microversion_skew.setter
    def microversion_skew(self, microversion_skew):
        """Sets the microversion_skew of this BTFeatureScriptEvalCall.


        :param microversion_skew: The microversion_skew of this BTFeatureScriptEvalCall.  # noqa: E501
        :type: bool
        """

        self._microversion_skew = microversion_skew

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
        if not isinstance(other, BTFeatureScriptEvalCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
