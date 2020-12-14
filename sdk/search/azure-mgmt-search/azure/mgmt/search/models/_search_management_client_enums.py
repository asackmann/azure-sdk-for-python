# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AdminKeyKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PRIMARY = "primary"
    SECONDARY = "secondary"

class HostingMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density
    partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed
    for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For
    all other SKUs, this value must be 'default'.
    """

    DEFAULT = "default"
    HIGH_DENSITY = "highDensity"

class IdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"

class PrivateLinkServiceConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the the private link service connection. Can be Pending, Approved, Rejected, or
    Disconnected.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the last provisioning operation performed on the search service. Provisioning is
    an intermediate state that occurs while service capacity is being established. After capacity
    is set up, provisioningState changes to either 'succeeded' or 'failed'. Client applications can
    poll provisioning status (the recommended polling interval is from 30 seconds to one minute) by
    using the Get Search Service operation to see when an operation is completed. If you are using
    the free service, this value tends to come back as 'succeeded' directly in the call to Create
    search service. This is because the free service uses capacity that is already set up.
    """

    SUCCEEDED = "succeeded"
    PROVISIONING = "provisioning"
    FAILED = "failed"

class PublicNetworkAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """This value can be set to 'enabled' to avoid breaking changes on existing customer resources and
    templates. If set to 'disabled', traffic over public interface is not allowed, and private
    endpoint connections would be the exclusive access method.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"

class SearchServiceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the search service. Possible values include: 'running': The search service is
    running and no provisioning operations are underway. 'provisioning': The search service is
    being provisioned or scaled up or down. 'deleting': The search service is being deleted.
    'degraded': The search service is degraded. This can occur when the underlying search units are
    not healthy. The search service is most likely operational, but performance might be slow and
    some requests might be dropped. 'disabled': The search service is disabled. In this state, the
    service will reject all API requests. 'error': The search service is in an error state. If your
    service is in the degraded, disabled, or error states, it means the Azure Cognitive Search team
    is actively investigating the underlying issue. Dedicated services in these states are still
    chargeable based on the number of search units provisioned.
    """

    RUNNING = "running"
    PROVISIONING = "provisioning"
    DELETING = "deleting"
    DEGRADED = "degraded"
    DISABLED = "disabled"
    ERROR = "error"

class SharedPrivateLinkResourceAsyncOperationResult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the long running asynchronous shared private link resource operation.
    """

    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class SharedPrivateLinkResourceProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the shared private link resource. Can be Updating, Deleting, Failed,
    Succeeded or Incomplete.
    """

    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    INCOMPLETE = "Incomplete"

class SharedPrivateLinkResourceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the shared private link resource. Can be Pending, Approved, Rejected or Disconnected.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated
    service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12
    replicas. 'standard2': Similar to standard, but with more capacity per search unit.
    'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3
    partitions with more indexes if you also set the hostingMode property to 'highDensity').
    'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions.
    'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
    """

    FREE = "free"
    BASIC = "basic"
    STANDARD = "standard"
    STANDARD2 = "standard2"
    STANDARD3 = "standard3"
    STORAGE_OPTIMIZED_L1 = "storage_optimized_l1"
    STORAGE_OPTIMIZED_L2 = "storage_optimized_l2"

class UnavailableNameReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason why the name is not available. 'Invalid' indicates the name provided does not match
    the naming requirements (incorrect length, unsupported characters, etc.). 'AlreadyExists'
    indicates that the name is already in use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"
