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


class BTCommentInfo(object):
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
        'element_query': 'str',
        'element_feature': 'str',
        'assignee': 'BTUserSummaryInfo',
        'assigned_at': 'datetime',
        'view_data': 'BTViewDataInfo',
        'top_level': 'bool',
        'reopened_by': 'BTUserSummaryInfo',
        'reopened_at': 'datetime',
        'attachment': 'BTCommentAttachmentInfo',
        'resolved_at': 'datetime',
        'version_id': 'str',
        'created_at': 'datetime',
        'workspace_id': 'str',
        'element_id': 'str',
        'user': 'BTUserSummaryInfo',
        'document_id': 'str',
        'can_delete': 'bool',
        'resolved_by': 'BTUserSummaryInfo',
        'parent_id': 'str',
        'thumbnail': 'BTCommentAttachmentInfo',
        'release_package_id': 'str',
        'element_occurrences': 'list[str]',
        'assembly_features': 'list[str]',
        'can_resolve_or_reopen': 'bool',
        'message': 'str',
        'state': 'int',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'element_query': 'elementQuery',
        'element_feature': 'elementFeature',
        'assignee': 'assignee',
        'assigned_at': 'assignedAt',
        'view_data': 'viewData',
        'top_level': 'topLevel',
        'reopened_by': 'reopenedBy',
        'reopened_at': 'reopenedAt',
        'attachment': 'attachment',
        'resolved_at': 'resolvedAt',
        'version_id': 'versionId',
        'created_at': 'createdAt',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'user': 'user',
        'document_id': 'documentId',
        'can_delete': 'canDelete',
        'resolved_by': 'resolvedBy',
        'parent_id': 'parentId',
        'thumbnail': 'thumbnail',
        'release_package_id': 'releasePackageId',
        'element_occurrences': 'elementOccurrences',
        'assembly_features': 'assemblyFeatures',
        'can_resolve_or_reopen': 'canResolveOrReopen',
        'message': 'message',
        'state': 'state',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, element_query=None, element_feature=None, assignee=None, assigned_at=None, view_data=None, top_level=None, reopened_by=None, reopened_at=None, attachment=None, resolved_at=None, version_id=None, created_at=None, workspace_id=None, element_id=None, user=None, document_id=None, can_delete=None, resolved_by=None, parent_id=None, thumbnail=None, release_package_id=None, element_occurrences=None, assembly_features=None, can_resolve_or_reopen=None, message=None, state=None, href=None, view_ref=None, name=None, id=None):  # noqa: E501
        """BTCommentInfo - a model defined in OpenAPI"""  # noqa: E501

        self._element_query = None
        self._element_feature = None
        self._assignee = None
        self._assigned_at = None
        self._view_data = None
        self._top_level = None
        self._reopened_by = None
        self._reopened_at = None
        self._attachment = None
        self._resolved_at = None
        self._version_id = None
        self._created_at = None
        self._workspace_id = None
        self._element_id = None
        self._user = None
        self._document_id = None
        self._can_delete = None
        self._resolved_by = None
        self._parent_id = None
        self._thumbnail = None
        self._release_package_id = None
        self._element_occurrences = None
        self._assembly_features = None
        self._can_resolve_or_reopen = None
        self._message = None
        self._state = None
        self._href = None
        self._view_ref = None
        self._name = None
        self._id = None
        self.discriminator = None

        if element_query is not None:
            self.element_query = element_query
        if element_feature is not None:
            self.element_feature = element_feature
        if assignee is not None:
            self.assignee = assignee
        if assigned_at is not None:
            self.assigned_at = assigned_at
        if view_data is not None:
            self.view_data = view_data
        if top_level is not None:
            self.top_level = top_level
        if reopened_by is not None:
            self.reopened_by = reopened_by
        if reopened_at is not None:
            self.reopened_at = reopened_at
        if attachment is not None:
            self.attachment = attachment
        if resolved_at is not None:
            self.resolved_at = resolved_at
        if version_id is not None:
            self.version_id = version_id
        if created_at is not None:
            self.created_at = created_at
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if user is not None:
            self.user = user
        if document_id is not None:
            self.document_id = document_id
        if can_delete is not None:
            self.can_delete = can_delete
        if resolved_by is not None:
            self.resolved_by = resolved_by
        if parent_id is not None:
            self.parent_id = parent_id
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if release_package_id is not None:
            self.release_package_id = release_package_id
        if element_occurrences is not None:
            self.element_occurrences = element_occurrences
        if assembly_features is not None:
            self.assembly_features = assembly_features
        if can_resolve_or_reopen is not None:
            self.can_resolve_or_reopen = can_resolve_or_reopen
        if message is not None:
            self.message = message
        if state is not None:
            self.state = state
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def element_query(self):
        """Gets the element_query of this BTCommentInfo.  # noqa: E501


        :return: The element_query of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_query

    @element_query.setter
    def element_query(self, element_query):
        """Sets the element_query of this BTCommentInfo.


        :param element_query: The element_query of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._element_query = element_query

    @property
    def element_feature(self):
        """Gets the element_feature of this BTCommentInfo.  # noqa: E501


        :return: The element_feature of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_feature

    @element_feature.setter
    def element_feature(self, element_feature):
        """Sets the element_feature of this BTCommentInfo.


        :param element_feature: The element_feature of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._element_feature = element_feature

    @property
    def assignee(self):
        """Gets the assignee of this BTCommentInfo.  # noqa: E501


        :return: The assignee of this BTCommentInfo.  # noqa: E501
        :rtype: BTUserSummaryInfo
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this BTCommentInfo.


        :param assignee: The assignee of this BTCommentInfo.  # noqa: E501
        :type: BTUserSummaryInfo
        """

        self._assignee = assignee

    @property
    def assigned_at(self):
        """Gets the assigned_at of this BTCommentInfo.  # noqa: E501


        :return: The assigned_at of this BTCommentInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._assigned_at

    @assigned_at.setter
    def assigned_at(self, assigned_at):
        """Sets the assigned_at of this BTCommentInfo.


        :param assigned_at: The assigned_at of this BTCommentInfo.  # noqa: E501
        :type: datetime
        """

        self._assigned_at = assigned_at

    @property
    def view_data(self):
        """Gets the view_data of this BTCommentInfo.  # noqa: E501


        :return: The view_data of this BTCommentInfo.  # noqa: E501
        :rtype: BTViewDataInfo
        """
        return self._view_data

    @view_data.setter
    def view_data(self, view_data):
        """Sets the view_data of this BTCommentInfo.


        :param view_data: The view_data of this BTCommentInfo.  # noqa: E501
        :type: BTViewDataInfo
        """

        self._view_data = view_data

    @property
    def top_level(self):
        """Gets the top_level of this BTCommentInfo.  # noqa: E501


        :return: The top_level of this BTCommentInfo.  # noqa: E501
        :rtype: bool
        """
        return self._top_level

    @top_level.setter
    def top_level(self, top_level):
        """Sets the top_level of this BTCommentInfo.


        :param top_level: The top_level of this BTCommentInfo.  # noqa: E501
        :type: bool
        """

        self._top_level = top_level

    @property
    def reopened_by(self):
        """Gets the reopened_by of this BTCommentInfo.  # noqa: E501


        :return: The reopened_by of this BTCommentInfo.  # noqa: E501
        :rtype: BTUserSummaryInfo
        """
        return self._reopened_by

    @reopened_by.setter
    def reopened_by(self, reopened_by):
        """Sets the reopened_by of this BTCommentInfo.


        :param reopened_by: The reopened_by of this BTCommentInfo.  # noqa: E501
        :type: BTUserSummaryInfo
        """

        self._reopened_by = reopened_by

    @property
    def reopened_at(self):
        """Gets the reopened_at of this BTCommentInfo.  # noqa: E501


        :return: The reopened_at of this BTCommentInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._reopened_at

    @reopened_at.setter
    def reopened_at(self, reopened_at):
        """Sets the reopened_at of this BTCommentInfo.


        :param reopened_at: The reopened_at of this BTCommentInfo.  # noqa: E501
        :type: datetime
        """

        self._reopened_at = reopened_at

    @property
    def attachment(self):
        """Gets the attachment of this BTCommentInfo.  # noqa: E501


        :return: The attachment of this BTCommentInfo.  # noqa: E501
        :rtype: BTCommentAttachmentInfo
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this BTCommentInfo.


        :param attachment: The attachment of this BTCommentInfo.  # noqa: E501
        :type: BTCommentAttachmentInfo
        """

        self._attachment = attachment

    @property
    def resolved_at(self):
        """Gets the resolved_at of this BTCommentInfo.  # noqa: E501


        :return: The resolved_at of this BTCommentInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._resolved_at

    @resolved_at.setter
    def resolved_at(self, resolved_at):
        """Sets the resolved_at of this BTCommentInfo.


        :param resolved_at: The resolved_at of this BTCommentInfo.  # noqa: E501
        :type: datetime
        """

        self._resolved_at = resolved_at

    @property
    def version_id(self):
        """Gets the version_id of this BTCommentInfo.  # noqa: E501


        :return: The version_id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTCommentInfo.


        :param version_id: The version_id of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def created_at(self):
        """Gets the created_at of this BTCommentInfo.  # noqa: E501


        :return: The created_at of this BTCommentInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BTCommentInfo.


        :param created_at: The created_at of this BTCommentInfo.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTCommentInfo.  # noqa: E501


        :return: The workspace_id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTCommentInfo.


        :param workspace_id: The workspace_id of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTCommentInfo.  # noqa: E501


        :return: The element_id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTCommentInfo.


        :param element_id: The element_id of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def user(self):
        """Gets the user of this BTCommentInfo.  # noqa: E501


        :return: The user of this BTCommentInfo.  # noqa: E501
        :rtype: BTUserSummaryInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BTCommentInfo.


        :param user: The user of this BTCommentInfo.  # noqa: E501
        :type: BTUserSummaryInfo
        """

        self._user = user

    @property
    def document_id(self):
        """Gets the document_id of this BTCommentInfo.  # noqa: E501


        :return: The document_id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTCommentInfo.


        :param document_id: The document_id of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def can_delete(self):
        """Gets the can_delete of this BTCommentInfo.  # noqa: E501


        :return: The can_delete of this BTCommentInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this BTCommentInfo.


        :param can_delete: The can_delete of this BTCommentInfo.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def resolved_by(self):
        """Gets the resolved_by of this BTCommentInfo.  # noqa: E501


        :return: The resolved_by of this BTCommentInfo.  # noqa: E501
        :rtype: BTUserSummaryInfo
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """Sets the resolved_by of this BTCommentInfo.


        :param resolved_by: The resolved_by of this BTCommentInfo.  # noqa: E501
        :type: BTUserSummaryInfo
        """

        self._resolved_by = resolved_by

    @property
    def parent_id(self):
        """Gets the parent_id of this BTCommentInfo.  # noqa: E501


        :return: The parent_id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTCommentInfo.


        :param parent_id: The parent_id of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def thumbnail(self):
        """Gets the thumbnail of this BTCommentInfo.  # noqa: E501


        :return: The thumbnail of this BTCommentInfo.  # noqa: E501
        :rtype: BTCommentAttachmentInfo
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this BTCommentInfo.


        :param thumbnail: The thumbnail of this BTCommentInfo.  # noqa: E501
        :type: BTCommentAttachmentInfo
        """

        self._thumbnail = thumbnail

    @property
    def release_package_id(self):
        """Gets the release_package_id of this BTCommentInfo.  # noqa: E501


        :return: The release_package_id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._release_package_id

    @release_package_id.setter
    def release_package_id(self, release_package_id):
        """Sets the release_package_id of this BTCommentInfo.


        :param release_package_id: The release_package_id of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._release_package_id = release_package_id

    @property
    def element_occurrences(self):
        """Gets the element_occurrences of this BTCommentInfo.  # noqa: E501


        :return: The element_occurrences of this BTCommentInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._element_occurrences

    @element_occurrences.setter
    def element_occurrences(self, element_occurrences):
        """Sets the element_occurrences of this BTCommentInfo.


        :param element_occurrences: The element_occurrences of this BTCommentInfo.  # noqa: E501
        :type: list[str]
        """

        self._element_occurrences = element_occurrences

    @property
    def assembly_features(self):
        """Gets the assembly_features of this BTCommentInfo.  # noqa: E501


        :return: The assembly_features of this BTCommentInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._assembly_features

    @assembly_features.setter
    def assembly_features(self, assembly_features):
        """Sets the assembly_features of this BTCommentInfo.


        :param assembly_features: The assembly_features of this BTCommentInfo.  # noqa: E501
        :type: list[str]
        """

        self._assembly_features = assembly_features

    @property
    def can_resolve_or_reopen(self):
        """Gets the can_resolve_or_reopen of this BTCommentInfo.  # noqa: E501


        :return: The can_resolve_or_reopen of this BTCommentInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_resolve_or_reopen

    @can_resolve_or_reopen.setter
    def can_resolve_or_reopen(self, can_resolve_or_reopen):
        """Sets the can_resolve_or_reopen of this BTCommentInfo.


        :param can_resolve_or_reopen: The can_resolve_or_reopen of this BTCommentInfo.  # noqa: E501
        :type: bool
        """

        self._can_resolve_or_reopen = can_resolve_or_reopen

    @property
    def message(self):
        """Gets the message of this BTCommentInfo.  # noqa: E501


        :return: The message of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BTCommentInfo.


        :param message: The message of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def state(self):
        """Gets the state of this BTCommentInfo.  # noqa: E501


        :return: The state of this BTCommentInfo.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTCommentInfo.


        :param state: The state of this BTCommentInfo.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def href(self):
        """Gets the href of this BTCommentInfo.  # noqa: E501


        :return: The href of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTCommentInfo.


        :param href: The href of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTCommentInfo.  # noqa: E501


        :return: The view_ref of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTCommentInfo.


        :param view_ref: The view_ref of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTCommentInfo.  # noqa: E501


        :return: The name of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTCommentInfo.


        :param name: The name of this BTCommentInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTCommentInfo.  # noqa: E501


        :return: The id of this BTCommentInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTCommentInfo.


        :param id: The id of this BTCommentInfo.  # noqa: E501
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
        if not isinstance(other, BTCommentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
