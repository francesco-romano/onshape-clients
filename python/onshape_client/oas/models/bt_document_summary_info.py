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


class BTDocumentSummaryInfo(object):
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
        'default_element_id': 'str',
        'default_workspace': 'BTBaseInfo',
        'parent_id': 'str',
        'permission_set': 'object',
        'trash': 'bool',
        'total_workspaces_updating': 'int',
        'total_workspaces_scheduled_for_update': 'int',
        'can_unshare': 'bool',
        'thumbnail': 'BTThumbnailInfo',
        'support_team_user_and_shared': 'bool',
        'liked_by_current_user': 'bool',
        'document_labels': 'list[BTDocumentLabelInfo]',
        'number_of_times_referenced': 'int',
        'number_of_times_copied': 'int',
        'likes': 'int',
        'recent_version': 'BTBaseInfo',
        'has_relevant_insertables': 'bool',
        'created_with_education_plan': 'bool',
        'not_revision_managed': 'bool',
        'anonymous_access_allowed': 'bool',
        'anonymous_allows_export': 'bool',
        'tags': 'list[str]',
        'trashed_at': 'datetime',
        'is_orphaned': 'bool',
        'public': 'bool',
        'user_account_limits_breached': 'bool',
        'is_using_managed_workflow': 'bool',
        'permission': 'str',
        'has_release_revisionable_objects': 'bool'
    }

    attribute_map = {
        'default_element_id': 'defaultElementId',
        'default_workspace': 'defaultWorkspace',
        'parent_id': 'parentId',
        'permission_set': 'permissionSet',
        'trash': 'trash',
        'total_workspaces_updating': 'totalWorkspacesUpdating',
        'total_workspaces_scheduled_for_update': 'totalWorkspacesScheduledForUpdate',
        'can_unshare': 'canUnshare',
        'thumbnail': 'thumbnail',
        'support_team_user_and_shared': 'supportTeamUserAndShared',
        'liked_by_current_user': 'likedByCurrentUser',
        'document_labels': 'documentLabels',
        'number_of_times_referenced': 'numberOfTimesReferenced',
        'number_of_times_copied': 'numberOfTimesCopied',
        'likes': 'likes',
        'recent_version': 'recentVersion',
        'has_relevant_insertables': 'hasRelevantInsertables',
        'created_with_education_plan': 'createdWithEducationPlan',
        'not_revision_managed': 'notRevisionManaged',
        'anonymous_access_allowed': 'anonymousAccessAllowed',
        'anonymous_allows_export': 'anonymousAllowsExport',
        'tags': 'tags',
        'trashed_at': 'trashedAt',
        'is_orphaned': 'isOrphaned',
        'public': 'public',
        'user_account_limits_breached': 'userAccountLimitsBreached',
        'is_using_managed_workflow': 'isUsingManagedWorkflow',
        'permission': 'permission',
        'has_release_revisionable_objects': 'hasReleaseRevisionableObjects'
    }

    def __init__(self, default_element_id=None, default_workspace=None, parent_id=None, permission_set=None, trash=None, total_workspaces_updating=None, total_workspaces_scheduled_for_update=None, can_unshare=None, thumbnail=None, support_team_user_and_shared=None, liked_by_current_user=None, document_labels=None, number_of_times_referenced=None, number_of_times_copied=None, likes=None, recent_version=None, has_relevant_insertables=None, created_with_education_plan=None, not_revision_managed=None, anonymous_access_allowed=None, anonymous_allows_export=None, tags=None, trashed_at=None, is_orphaned=None, public=None, user_account_limits_breached=None, is_using_managed_workflow=None, permission=None, has_release_revisionable_objects=None):  # noqa: E501
        """BTDocumentSummaryInfo - a model defined in OpenAPI"""  # noqa: E501

        self._default_element_id = None
        self._default_workspace = None
        self._parent_id = None
        self._permission_set = None
        self._trash = None
        self._total_workspaces_updating = None
        self._total_workspaces_scheduled_for_update = None
        self._can_unshare = None
        self._thumbnail = None
        self._support_team_user_and_shared = None
        self._liked_by_current_user = None
        self._document_labels = None
        self._number_of_times_referenced = None
        self._number_of_times_copied = None
        self._likes = None
        self._recent_version = None
        self._has_relevant_insertables = None
        self._created_with_education_plan = None
        self._not_revision_managed = None
        self._anonymous_access_allowed = None
        self._anonymous_allows_export = None
        self._tags = None
        self._trashed_at = None
        self._is_orphaned = None
        self._public = None
        self._user_account_limits_breached = None
        self._is_using_managed_workflow = None
        self._permission = None
        self._has_release_revisionable_objects = None
        self.discriminator = None

        if default_element_id is not None:
            self.default_element_id = default_element_id
        if default_workspace is not None:
            self.default_workspace = default_workspace
        if parent_id is not None:
            self.parent_id = parent_id
        if permission_set is not None:
            self.permission_set = permission_set
        if trash is not None:
            self.trash = trash
        if total_workspaces_updating is not None:
            self.total_workspaces_updating = total_workspaces_updating
        if total_workspaces_scheduled_for_update is not None:
            self.total_workspaces_scheduled_for_update = total_workspaces_scheduled_for_update
        if can_unshare is not None:
            self.can_unshare = can_unshare
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if support_team_user_and_shared is not None:
            self.support_team_user_and_shared = support_team_user_and_shared
        if liked_by_current_user is not None:
            self.liked_by_current_user = liked_by_current_user
        if document_labels is not None:
            self.document_labels = document_labels
        if number_of_times_referenced is not None:
            self.number_of_times_referenced = number_of_times_referenced
        if number_of_times_copied is not None:
            self.number_of_times_copied = number_of_times_copied
        if likes is not None:
            self.likes = likes
        if recent_version is not None:
            self.recent_version = recent_version
        if has_relevant_insertables is not None:
            self.has_relevant_insertables = has_relevant_insertables
        if created_with_education_plan is not None:
            self.created_with_education_plan = created_with_education_plan
        if not_revision_managed is not None:
            self.not_revision_managed = not_revision_managed
        if anonymous_access_allowed is not None:
            self.anonymous_access_allowed = anonymous_access_allowed
        if anonymous_allows_export is not None:
            self.anonymous_allows_export = anonymous_allows_export
        if tags is not None:
            self.tags = tags
        if trashed_at is not None:
            self.trashed_at = trashed_at
        if is_orphaned is not None:
            self.is_orphaned = is_orphaned
        if public is not None:
            self.public = public
        if user_account_limits_breached is not None:
            self.user_account_limits_breached = user_account_limits_breached
        if is_using_managed_workflow is not None:
            self.is_using_managed_workflow = is_using_managed_workflow
        if permission is not None:
            self.permission = permission
        if has_release_revisionable_objects is not None:
            self.has_release_revisionable_objects = has_release_revisionable_objects

    @property
    def default_element_id(self):
        """Gets the default_element_id of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The default_element_id of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_element_id

    @default_element_id.setter
    def default_element_id(self, default_element_id):
        """Sets the default_element_id of this BTDocumentSummaryInfo.


        :param default_element_id: The default_element_id of this BTDocumentSummaryInfo.  # noqa: E501
        :type: str
        """

        self._default_element_id = default_element_id

    @property
    def default_workspace(self):
        """Gets the default_workspace of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The default_workspace of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: BTBaseInfo
        """
        return self._default_workspace

    @default_workspace.setter
    def default_workspace(self, default_workspace):
        """Sets the default_workspace of this BTDocumentSummaryInfo.


        :param default_workspace: The default_workspace of this BTDocumentSummaryInfo.  # noqa: E501
        :type: BTBaseInfo
        """

        self._default_workspace = default_workspace

    @property
    def parent_id(self):
        """Gets the parent_id of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The parent_id of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTDocumentSummaryInfo.


        :param parent_id: The parent_id of this BTDocumentSummaryInfo.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def permission_set(self):
        """Gets the permission_set of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The permission_set of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: object
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this BTDocumentSummaryInfo.


        :param permission_set: The permission_set of this BTDocumentSummaryInfo.  # noqa: E501
        :type: object
        """

        self._permission_set = permission_set

    @property
    def trash(self):
        """Gets the trash of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The trash of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._trash

    @trash.setter
    def trash(self, trash):
        """Sets the trash of this BTDocumentSummaryInfo.


        :param trash: The trash of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._trash = trash

    @property
    def total_workspaces_updating(self):
        """Gets the total_workspaces_updating of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The total_workspaces_updating of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_workspaces_updating

    @total_workspaces_updating.setter
    def total_workspaces_updating(self, total_workspaces_updating):
        """Sets the total_workspaces_updating of this BTDocumentSummaryInfo.


        :param total_workspaces_updating: The total_workspaces_updating of this BTDocumentSummaryInfo.  # noqa: E501
        :type: int
        """

        self._total_workspaces_updating = total_workspaces_updating

    @property
    def total_workspaces_scheduled_for_update(self):
        """Gets the total_workspaces_scheduled_for_update of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The total_workspaces_scheduled_for_update of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_workspaces_scheduled_for_update

    @total_workspaces_scheduled_for_update.setter
    def total_workspaces_scheduled_for_update(self, total_workspaces_scheduled_for_update):
        """Sets the total_workspaces_scheduled_for_update of this BTDocumentSummaryInfo.


        :param total_workspaces_scheduled_for_update: The total_workspaces_scheduled_for_update of this BTDocumentSummaryInfo.  # noqa: E501
        :type: int
        """

        self._total_workspaces_scheduled_for_update = total_workspaces_scheduled_for_update

    @property
    def can_unshare(self):
        """Gets the can_unshare of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The can_unshare of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_unshare

    @can_unshare.setter
    def can_unshare(self, can_unshare):
        """Sets the can_unshare of this BTDocumentSummaryInfo.


        :param can_unshare: The can_unshare of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._can_unshare = can_unshare

    @property
    def thumbnail(self):
        """Gets the thumbnail of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The thumbnail of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: BTThumbnailInfo
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this BTDocumentSummaryInfo.


        :param thumbnail: The thumbnail of this BTDocumentSummaryInfo.  # noqa: E501
        :type: BTThumbnailInfo
        """

        self._thumbnail = thumbnail

    @property
    def support_team_user_and_shared(self):
        """Gets the support_team_user_and_shared of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The support_team_user_and_shared of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._support_team_user_and_shared

    @support_team_user_and_shared.setter
    def support_team_user_and_shared(self, support_team_user_and_shared):
        """Sets the support_team_user_and_shared of this BTDocumentSummaryInfo.


        :param support_team_user_and_shared: The support_team_user_and_shared of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._support_team_user_and_shared = support_team_user_and_shared

    @property
    def liked_by_current_user(self):
        """Gets the liked_by_current_user of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The liked_by_current_user of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._liked_by_current_user

    @liked_by_current_user.setter
    def liked_by_current_user(self, liked_by_current_user):
        """Sets the liked_by_current_user of this BTDocumentSummaryInfo.


        :param liked_by_current_user: The liked_by_current_user of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._liked_by_current_user = liked_by_current_user

    @property
    def document_labels(self):
        """Gets the document_labels of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The document_labels of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: list[BTDocumentLabelInfo]
        """
        return self._document_labels

    @document_labels.setter
    def document_labels(self, document_labels):
        """Sets the document_labels of this BTDocumentSummaryInfo.


        :param document_labels: The document_labels of this BTDocumentSummaryInfo.  # noqa: E501
        :type: list[BTDocumentLabelInfo]
        """

        self._document_labels = document_labels

    @property
    def number_of_times_referenced(self):
        """Gets the number_of_times_referenced of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The number_of_times_referenced of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._number_of_times_referenced

    @number_of_times_referenced.setter
    def number_of_times_referenced(self, number_of_times_referenced):
        """Sets the number_of_times_referenced of this BTDocumentSummaryInfo.


        :param number_of_times_referenced: The number_of_times_referenced of this BTDocumentSummaryInfo.  # noqa: E501
        :type: int
        """

        self._number_of_times_referenced = number_of_times_referenced

    @property
    def number_of_times_copied(self):
        """Gets the number_of_times_copied of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The number_of_times_copied of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._number_of_times_copied

    @number_of_times_copied.setter
    def number_of_times_copied(self, number_of_times_copied):
        """Sets the number_of_times_copied of this BTDocumentSummaryInfo.


        :param number_of_times_copied: The number_of_times_copied of this BTDocumentSummaryInfo.  # noqa: E501
        :type: int
        """

        self._number_of_times_copied = number_of_times_copied

    @property
    def likes(self):
        """Gets the likes of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The likes of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._likes

    @likes.setter
    def likes(self, likes):
        """Sets the likes of this BTDocumentSummaryInfo.


        :param likes: The likes of this BTDocumentSummaryInfo.  # noqa: E501
        :type: int
        """

        self._likes = likes

    @property
    def recent_version(self):
        """Gets the recent_version of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The recent_version of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: BTBaseInfo
        """
        return self._recent_version

    @recent_version.setter
    def recent_version(self, recent_version):
        """Sets the recent_version of this BTDocumentSummaryInfo.


        :param recent_version: The recent_version of this BTDocumentSummaryInfo.  # noqa: E501
        :type: BTBaseInfo
        """

        self._recent_version = recent_version

    @property
    def has_relevant_insertables(self):
        """Gets the has_relevant_insertables of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The has_relevant_insertables of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_relevant_insertables

    @has_relevant_insertables.setter
    def has_relevant_insertables(self, has_relevant_insertables):
        """Sets the has_relevant_insertables of this BTDocumentSummaryInfo.


        :param has_relevant_insertables: The has_relevant_insertables of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._has_relevant_insertables = has_relevant_insertables

    @property
    def created_with_education_plan(self):
        """Gets the created_with_education_plan of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The created_with_education_plan of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._created_with_education_plan

    @created_with_education_plan.setter
    def created_with_education_plan(self, created_with_education_plan):
        """Sets the created_with_education_plan of this BTDocumentSummaryInfo.


        :param created_with_education_plan: The created_with_education_plan of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._created_with_education_plan = created_with_education_plan

    @property
    def not_revision_managed(self):
        """Gets the not_revision_managed of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The not_revision_managed of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._not_revision_managed

    @not_revision_managed.setter
    def not_revision_managed(self, not_revision_managed):
        """Sets the not_revision_managed of this BTDocumentSummaryInfo.


        :param not_revision_managed: The not_revision_managed of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._not_revision_managed = not_revision_managed

    @property
    def anonymous_access_allowed(self):
        """Gets the anonymous_access_allowed of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The anonymous_access_allowed of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_access_allowed

    @anonymous_access_allowed.setter
    def anonymous_access_allowed(self, anonymous_access_allowed):
        """Sets the anonymous_access_allowed of this BTDocumentSummaryInfo.


        :param anonymous_access_allowed: The anonymous_access_allowed of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._anonymous_access_allowed = anonymous_access_allowed

    @property
    def anonymous_allows_export(self):
        """Gets the anonymous_allows_export of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The anonymous_allows_export of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_allows_export

    @anonymous_allows_export.setter
    def anonymous_allows_export(self, anonymous_allows_export):
        """Sets the anonymous_allows_export of this BTDocumentSummaryInfo.


        :param anonymous_allows_export: The anonymous_allows_export of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._anonymous_allows_export = anonymous_allows_export

    @property
    def tags(self):
        """Gets the tags of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The tags of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BTDocumentSummaryInfo.


        :param tags: The tags of this BTDocumentSummaryInfo.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def trashed_at(self):
        """Gets the trashed_at of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The trashed_at of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._trashed_at

    @trashed_at.setter
    def trashed_at(self, trashed_at):
        """Sets the trashed_at of this BTDocumentSummaryInfo.


        :param trashed_at: The trashed_at of this BTDocumentSummaryInfo.  # noqa: E501
        :type: datetime
        """

        self._trashed_at = trashed_at

    @property
    def is_orphaned(self):
        """Gets the is_orphaned of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The is_orphaned of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_orphaned

    @is_orphaned.setter
    def is_orphaned(self, is_orphaned):
        """Sets the is_orphaned of this BTDocumentSummaryInfo.


        :param is_orphaned: The is_orphaned of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_orphaned = is_orphaned

    @property
    def public(self):
        """Gets the public of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The public of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BTDocumentSummaryInfo.


        :param public: The public of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def user_account_limits_breached(self):
        """Gets the user_account_limits_breached of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The user_account_limits_breached of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._user_account_limits_breached

    @user_account_limits_breached.setter
    def user_account_limits_breached(self, user_account_limits_breached):
        """Sets the user_account_limits_breached of this BTDocumentSummaryInfo.


        :param user_account_limits_breached: The user_account_limits_breached of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._user_account_limits_breached = user_account_limits_breached

    @property
    def is_using_managed_workflow(self):
        """Gets the is_using_managed_workflow of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The is_using_managed_workflow of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_using_managed_workflow

    @is_using_managed_workflow.setter
    def is_using_managed_workflow(self, is_using_managed_workflow):
        """Sets the is_using_managed_workflow of this BTDocumentSummaryInfo.


        :param is_using_managed_workflow: The is_using_managed_workflow of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_using_managed_workflow = is_using_managed_workflow

    @property
    def permission(self):
        """Gets the permission of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The permission of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this BTDocumentSummaryInfo.


        :param permission: The permission of this BTDocumentSummaryInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOACCESS", "ANONYMOUS_ACCESS", "READ", "READ_COPY_EXPORT", "COMMENT", "WRITE", "RESHARE", "FULL", "OWNER"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def has_release_revisionable_objects(self):
        """Gets the has_release_revisionable_objects of this BTDocumentSummaryInfo.  # noqa: E501


        :return: The has_release_revisionable_objects of this BTDocumentSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_release_revisionable_objects

    @has_release_revisionable_objects.setter
    def has_release_revisionable_objects(self, has_release_revisionable_objects):
        """Sets the has_release_revisionable_objects of this BTDocumentSummaryInfo.


        :param has_release_revisionable_objects: The has_release_revisionable_objects of this BTDocumentSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._has_release_revisionable_objects = has_release_revisionable_objects

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
        if not isinstance(other, BTDocumentSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
