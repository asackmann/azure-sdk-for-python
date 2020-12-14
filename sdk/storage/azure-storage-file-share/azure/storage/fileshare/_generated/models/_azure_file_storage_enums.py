# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class StorageErrorCode(str, Enum):

    account_already_exists = "AccountAlreadyExists"
    account_being_created = "AccountBeingCreated"
    account_is_disabled = "AccountIsDisabled"
    authentication_failed = "AuthenticationFailed"
    authorization_failure = "AuthorizationFailure"
    condition_headers_not_supported = "ConditionHeadersNotSupported"
    condition_not_met = "ConditionNotMet"
    empty_metadata_key = "EmptyMetadataKey"
    insufficient_account_permissions = "InsufficientAccountPermissions"
    internal_error = "InternalError"
    invalid_authentication_info = "InvalidAuthenticationInfo"
    invalid_header_value = "InvalidHeaderValue"
    invalid_http_verb = "InvalidHttpVerb"
    invalid_input = "InvalidInput"
    invalid_md5 = "InvalidMd5"
    invalid_metadata = "InvalidMetadata"
    invalid_query_parameter_value = "InvalidQueryParameterValue"
    invalid_range = "InvalidRange"
    invalid_resource_name = "InvalidResourceName"
    invalid_uri = "InvalidUri"
    invalid_xml_document = "InvalidXmlDocument"
    invalid_xml_node_value = "InvalidXmlNodeValue"
    md5_mismatch = "Md5Mismatch"
    metadata_too_large = "MetadataTooLarge"
    missing_content_length_header = "MissingContentLengthHeader"
    missing_required_query_parameter = "MissingRequiredQueryParameter"
    missing_required_header = "MissingRequiredHeader"
    missing_required_xml_node = "MissingRequiredXmlNode"
    multiple_condition_headers_not_supported = "MultipleConditionHeadersNotSupported"
    operation_timed_out = "OperationTimedOut"
    out_of_range_input = "OutOfRangeInput"
    out_of_range_query_parameter_value = "OutOfRangeQueryParameterValue"
    request_body_too_large = "RequestBodyTooLarge"
    resource_type_mismatch = "ResourceTypeMismatch"
    request_url_failed_to_parse = "RequestUrlFailedToParse"
    resource_already_exists = "ResourceAlreadyExists"
    resource_not_found = "ResourceNotFound"
    server_busy = "ServerBusy"
    unsupported_header = "UnsupportedHeader"
    unsupported_xml_node = "UnsupportedXmlNode"
    unsupported_query_parameter = "UnsupportedQueryParameter"
    unsupported_http_verb = "UnsupportedHttpVerb"
    cannot_delete_file_or_directory = "CannotDeleteFileOrDirectory"
    client_cache_flush_delay = "ClientCacheFlushDelay"
    delete_pending = "DeletePending"
    directory_not_empty = "DirectoryNotEmpty"
    file_lock_conflict = "FileLockConflict"
    invalid_file_or_directory_path_name = "InvalidFileOrDirectoryPathName"
    parent_not_found = "ParentNotFound"
    read_only_attribute = "ReadOnlyAttribute"
    share_already_exists = "ShareAlreadyExists"
    share_being_deleted = "ShareBeingDeleted"
    share_disabled = "ShareDisabled"
    share_not_found = "ShareNotFound"
    sharing_violation = "SharingViolation"
    share_snapshot_in_progress = "ShareSnapshotInProgress"
    share_snapshot_count_exceeded = "ShareSnapshotCountExceeded"
    share_snapshot_operation_not_supported = "ShareSnapshotOperationNotSupported"
    share_has_snapshots = "ShareHasSnapshots"
    container_quota_downgrade_not_allowed = "ContainerQuotaDowngradeNotAllowed"
    authorization_source_ip_mismatch = "AuthorizationSourceIPMismatch"
    authorization_protocol_mismatch = "AuthorizationProtocolMismatch"
    authorization_permission_mismatch = "AuthorizationPermissionMismatch"
    authorization_service_mismatch = "AuthorizationServiceMismatch"
    authorization_resource_type_mismatch = "AuthorizationResourceTypeMismatch"
    feature_version_mismatch = "FeatureVersionMismatch"


class LeaseDurationType(str, Enum):

    infinite = "infinite"
    fixed = "fixed"


class LeaseStateType(str, Enum):

    available = "available"
    leased = "leased"
    expired = "expired"
    breaking = "breaking"
    broken = "broken"


class LeaseStatusType(str, Enum):

    locked = "locked"
    unlocked = "unlocked"


class ShareRootSquash(str, Enum):

    no_root_squash = "NoRootSquash"
    root_squash = "RootSquash"
    all_squash = "AllSquash"


class ShareAccessTier(str, Enum):

    transaction_optimized = "TransactionOptimized"
    hot = "Hot"
    cool = "Cool"


class PermissionCopyModeType(str, Enum):

    source = "source"
    override = "override"


class DeleteSnapshotsOptionType(str, Enum):

    include = "include"
    include_leased = "include-leased"


class ListSharesIncludeType(str, Enum):

    snapshots = "snapshots"
    metadata = "metadata"
    deleted = "deleted"


class CopyStatusType(str, Enum):

    pending = "pending"
    success = "success"
    aborted = "aborted"
    failed = "failed"


class FileRangeWriteType(str, Enum):

    update = "update"
    clear = "clear"
