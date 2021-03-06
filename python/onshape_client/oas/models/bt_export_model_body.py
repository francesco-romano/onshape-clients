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


class BTExportModelBody(object):
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
        'faces': 'list[BTExportModelFace]',
        'vertices': 'list[BTExportModelVertex]',
        'id': 'str',
        'type': 'str',
        'edges': 'list[BTExportModelEdge]'
    }

    attribute_map = {
        'faces': 'faces',
        'vertices': 'vertices',
        'id': 'id',
        'type': 'type',
        'edges': 'edges'
    }

    def __init__(self, faces=None, vertices=None, id=None, type=None, edges=None):  # noqa: E501
        """BTExportModelBody - a model defined in OpenAPI"""  # noqa: E501

        self._faces = None
        self._vertices = None
        self._id = None
        self._type = None
        self._edges = None
        self.discriminator = None

        if faces is not None:
            self.faces = faces
        if vertices is not None:
            self.vertices = vertices
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if edges is not None:
            self.edges = edges

    @property
    def faces(self):
        """Gets the faces of this BTExportModelBody.  # noqa: E501


        :return: The faces of this BTExportModelBody.  # noqa: E501
        :rtype: list[BTExportModelFace]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this BTExportModelBody.


        :param faces: The faces of this BTExportModelBody.  # noqa: E501
        :type: list[BTExportModelFace]
        """

        self._faces = faces

    @property
    def vertices(self):
        """Gets the vertices of this BTExportModelBody.  # noqa: E501


        :return: The vertices of this BTExportModelBody.  # noqa: E501
        :rtype: list[BTExportModelVertex]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this BTExportModelBody.


        :param vertices: The vertices of this BTExportModelBody.  # noqa: E501
        :type: list[BTExportModelVertex]
        """

        self._vertices = vertices

    @property
    def id(self):
        """Gets the id of this BTExportModelBody.  # noqa: E501


        :return: The id of this BTExportModelBody.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTExportModelBody.


        :param id: The id of this BTExportModelBody.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this BTExportModelBody.  # noqa: E501


        :return: The type of this BTExportModelBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTExportModelBody.


        :param type: The type of this BTExportModelBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOLID", "SURFACE", "UNKNOWN"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def edges(self):
        """Gets the edges of this BTExportModelBody.  # noqa: E501


        :return: The edges of this BTExportModelBody.  # noqa: E501
        :rtype: list[BTExportModelEdge]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this BTExportModelBody.


        :param edges: The edges of this BTExportModelBody.  # noqa: E501
        :type: list[BTExportModelEdge]
        """

        self._edges = edges

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
        if not isinstance(other, BTExportModelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
