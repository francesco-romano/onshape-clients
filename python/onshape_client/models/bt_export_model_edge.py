# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.96
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTExportModelEdge(object):
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
        'id': 'str',
        'curve': 'BTCurveDescription',
        'geometry': 'BTExportModelEdgeGeometry',
        'vertices': 'list[str]',
        'type_id': 'int',
        'connection_source': 'BTConnection',
        'export_type_name': 'str',
        'unknown_class': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'curve': 'curve',
        'geometry': 'geometry',
        'vertices': 'vertices',
        'type_id': 'typeId',
        'connection_source': 'connectionSource',
        'export_type_name': 'exportTypeName',
        'unknown_class': 'unknownClass'
    }

    def __init__(self, id=None, curve=None, geometry=None, vertices=None, type_id=None, connection_source=None, export_type_name=None, unknown_class=None):  # noqa: E501
        """BTExportModelEdge - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._curve = None
        self._geometry = None
        self._vertices = None
        self._type_id = None
        self._connection_source = None
        self._export_type_name = None
        self._unknown_class = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if curve is not None:
            self.curve = curve
        if geometry is not None:
            self.geometry = geometry
        if vertices is not None:
            self.vertices = vertices
        if type_id is not None:
            self.type_id = type_id
        if connection_source is not None:
            self.connection_source = connection_source
        if export_type_name is not None:
            self.export_type_name = export_type_name
        if unknown_class is not None:
            self.unknown_class = unknown_class

    @property
    def id(self):
        """Gets the id of this BTExportModelEdge.  # noqa: E501


        :return: The id of this BTExportModelEdge.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTExportModelEdge.


        :param id: The id of this BTExportModelEdge.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def curve(self):
        """Gets the curve of this BTExportModelEdge.  # noqa: E501


        :return: The curve of this BTExportModelEdge.  # noqa: E501
        :rtype: BTCurveDescription
        """
        return self._curve

    @curve.setter
    def curve(self, curve):
        """Sets the curve of this BTExportModelEdge.


        :param curve: The curve of this BTExportModelEdge.  # noqa: E501
        :type: BTCurveDescription
        """

        self._curve = curve

    @property
    def geometry(self):
        """Gets the geometry of this BTExportModelEdge.  # noqa: E501


        :return: The geometry of this BTExportModelEdge.  # noqa: E501
        :rtype: BTExportModelEdgeGeometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this BTExportModelEdge.


        :param geometry: The geometry of this BTExportModelEdge.  # noqa: E501
        :type: BTExportModelEdgeGeometry
        """

        self._geometry = geometry

    @property
    def vertices(self):
        """Gets the vertices of this BTExportModelEdge.  # noqa: E501


        :return: The vertices of this BTExportModelEdge.  # noqa: E501
        :rtype: list[str]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this BTExportModelEdge.


        :param vertices: The vertices of this BTExportModelEdge.  # noqa: E501
        :type: list[str]
        """

        self._vertices = vertices

    @property
    def type_id(self):
        """Gets the type_id of this BTExportModelEdge.  # noqa: E501


        :return: The type_id of this BTExportModelEdge.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this BTExportModelEdge.


        :param type_id: The type_id of this BTExportModelEdge.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def connection_source(self):
        """Gets the connection_source of this BTExportModelEdge.  # noqa: E501


        :return: The connection_source of this BTExportModelEdge.  # noqa: E501
        :rtype: BTConnection
        """
        return self._connection_source

    @connection_source.setter
    def connection_source(self, connection_source):
        """Sets the connection_source of this BTExportModelEdge.


        :param connection_source: The connection_source of this BTExportModelEdge.  # noqa: E501
        :type: BTConnection
        """

        self._connection_source = connection_source

    @property
    def export_type_name(self):
        """Gets the export_type_name of this BTExportModelEdge.  # noqa: E501


        :return: The export_type_name of this BTExportModelEdge.  # noqa: E501
        :rtype: str
        """
        return self._export_type_name

    @export_type_name.setter
    def export_type_name(self, export_type_name):
        """Sets the export_type_name of this BTExportModelEdge.


        :param export_type_name: The export_type_name of this BTExportModelEdge.  # noqa: E501
        :type: str
        """

        self._export_type_name = export_type_name

    @property
    def unknown_class(self):
        """Gets the unknown_class of this BTExportModelEdge.  # noqa: E501


        :return: The unknown_class of this BTExportModelEdge.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_class

    @unknown_class.setter
    def unknown_class(self, unknown_class):
        """Sets the unknown_class of this BTExportModelEdge.


        :param unknown_class: The unknown_class of this BTExportModelEdge.  # noqa: E501
        :type: bool
        """

        self._unknown_class = unknown_class

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
        if not isinstance(other, BTExportModelEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other