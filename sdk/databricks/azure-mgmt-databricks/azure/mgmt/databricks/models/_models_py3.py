# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._databricks_client_enums import *


class AddressSpace(msrest.serialization.Model):
    """AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network.

    :param address_prefixes: A list of address blocks reserved for this virtual network in CIDR
     notation.
    :type address_prefixes: list[str]
    """

    _attribute_map = {
        'address_prefixes': {'key': 'addressPrefixes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        address_prefixes: Optional[List[str]] = None,
        **kwargs
    ):
        super(AddressSpace, self).__init__(**kwargs)
        self.address_prefixes = address_prefixes


class CreatedBy(msrest.serialization.Model):
    """Provides details of the entity that created/updated the workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar oid: The Object ID that created the workspace.
    :vartype oid: str
    :ivar puid: The Personal Object ID corresponding to the object ID above.
    :vartype puid: str
    :ivar application_id: The application ID of the application that initiated the creation of the
     workspace. For example, Azure Portal.
    :vartype application_id: str
    """

    _validation = {
        'oid': {'readonly': True},
        'puid': {'readonly': True},
        'application_id': {'readonly': True},
    }

    _attribute_map = {
        'oid': {'key': 'oid', 'type': 'str'},
        'puid': {'key': 'puid', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreatedBy, self).__init__(**kwargs)
        self.oid = None
        self.puid = None
        self.application_id = None


class Encryption(msrest.serialization.Model):
    """The object that contains details of encryption used on the workspace.

    :param key_source: The encryption keySource (provider). Possible values (case-insensitive):
     Default, Microsoft.Keyvault. Possible values include: "Default", "Microsoft.Keyvault". Default
     value: "Default".
    :type key_source: str or ~azure.mgmt.databricks.models.KeySource
    :param key_name: The name of KeyVault key.
    :type key_name: str
    :param key_version: The version of KeyVault key.
    :type key_version: str
    :param key_vault_uri: The Uri of KeyVault.
    :type key_vault_uri: str
    """

    _attribute_map = {
        'key_source': {'key': 'keySource', 'type': 'str'},
        'key_name': {'key': 'KeyName', 'type': 'str'},
        'key_version': {'key': 'keyversion', 'type': 'str'},
        'key_vault_uri': {'key': 'keyvaulturi', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key_source: Optional[Union[str, "KeySource"]] = "Default",
        key_name: Optional[str] = None,
        key_version: Optional[str] = None,
        key_vault_uri: Optional[str] = None,
        **kwargs
    ):
        super(Encryption, self).__init__(**kwargs)
        self.key_source = key_source
        self.key_name = key_name
        self.key_version = key_version
        self.key_vault_uri = key_vault_uri


class ErrorDetail(msrest.serialization.Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error's code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param target: Indicates which property in the request is responsible for the error.
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class ErrorInfo(msrest.serialization.Model):
    """The code and message for an error.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. A machine readable error code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param details: error details.
    :type details: list[~azure.mgmt.databricks.models.ErrorDetail]
    :param innererror: Inner error details if they exist.
    :type innererror: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        details: Optional[List["ErrorDetail"]] = None,
        innererror: Optional[str] = None,
        **kwargs
    ):
        super(ErrorInfo, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details
        self.innererror = innererror


class ErrorResponse(msrest.serialization.Model):
    """Contains details when the response code indicates an error.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. The error details.
    :type error: ~azure.mgmt.databricks.models.ErrorInfo
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorInfo'},
    }

    def __init__(
        self,
        *,
        error: "ErrorInfo",
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ManagedIdentityConfiguration(msrest.serialization.Model):
    """The Managed Identity details for storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The objectId of the Managed Identity that is linked to the Managed Storage
     account.
    :vartype principal_id: str
    :ivar tenant_id: The tenant Id where the Managed Identity is created.
    :vartype tenant_id: str
    :ivar type: The type of Identity created. It can be either SystemAssigned or UserAssigned.
    :vartype type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ManagedIdentityConfiguration, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = None


class Operation(msrest.serialization.Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.databricks.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.ResourceProvider.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Resource Provider operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Resource Provider operations supported by the Resource Provider resource
     provider.
    :type value: list[~azure.mgmt.databricks.models.Operation]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class Resource(msrest.serialization.Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Sku(msrest.serialization.Model):
    """SKU for the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name.
    :type name: str
    :param tier: The SKU tier.
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        tier: Optional[str] = None,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class VirtualNetworkPeering(msrest.serialization.Model):
    """Peerings in a VirtualNetwork resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Name of the virtual network peering resource.
    :vartype name: str
    :ivar id: Resource ID.
    :vartype id: str
    :ivar type: type of the virtual network peering resource.
    :vartype type: str
    :param allow_virtual_network_access: Whether the VMs in the local virtual network space would
     be able to access the VMs in remote virtual network space.
    :type allow_virtual_network_access: bool
    :param allow_forwarded_traffic: Whether the forwarded traffic from the VMs in the local virtual
     network will be allowed/disallowed in remote virtual network.
    :type allow_forwarded_traffic: bool
    :param allow_gateway_transit: If gateway links can be used in remote virtual networking to link
     to this virtual network.
    :type allow_gateway_transit: bool
    :param use_remote_gateways: If remote gateways can be used on this virtual network. If the flag
     is set to true, and allowGatewayTransit on remote peering is also true, virtual network will
     use gateways of remote virtual network for transit. Only one peering can have this flag set to
     true. This flag cannot be set if virtual network already has a gateway.
    :type use_remote_gateways: bool
    :param databricks_virtual_network: The remote virtual network should be in the same region. See
     here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-
     guide/cloud-configurations/azure/vnet-peering).
    :type databricks_virtual_network:
     ~azure.mgmt.databricks.models.VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork
    :param databricks_address_space: The reference to the databricks virtual network address space.
    :type databricks_address_space: ~azure.mgmt.databricks.models.AddressSpace
    :param remote_virtual_network: Required. The remote virtual network should be in the same
     region. See here to learn more (https://docs.microsoft.com/en-
     us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
    :type remote_virtual_network:
     ~azure.mgmt.databricks.models.VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork
    :param remote_address_space: The reference to the remote virtual network address space.
    :type remote_address_space: ~azure.mgmt.databricks.models.AddressSpace
    :ivar peering_state: The status of the virtual network peering. Possible values include:
     "Initiated", "Connected", "Disconnected".
    :vartype peering_state: str or ~azure.mgmt.databricks.models.PeeringState
    :ivar provisioning_state: The provisioning state of the virtual network peering resource.
     Possible values include: "Succeeded", "Updating", "Deleting", "Failed".
    :vartype provisioning_state: str or ~azure.mgmt.databricks.models.PeeringProvisioningState
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'remote_virtual_network': {'required': True},
        'peering_state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'allow_virtual_network_access': {'key': 'properties.allowVirtualNetworkAccess', 'type': 'bool'},
        'allow_forwarded_traffic': {'key': 'properties.allowForwardedTraffic', 'type': 'bool'},
        'allow_gateway_transit': {'key': 'properties.allowGatewayTransit', 'type': 'bool'},
        'use_remote_gateways': {'key': 'properties.useRemoteGateways', 'type': 'bool'},
        'databricks_virtual_network': {'key': 'properties.databricksVirtualNetwork', 'type': 'VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork'},
        'databricks_address_space': {'key': 'properties.databricksAddressSpace', 'type': 'AddressSpace'},
        'remote_virtual_network': {'key': 'properties.remoteVirtualNetwork', 'type': 'VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork'},
        'remote_address_space': {'key': 'properties.remoteAddressSpace', 'type': 'AddressSpace'},
        'peering_state': {'key': 'properties.peeringState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        remote_virtual_network: "VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork",
        allow_virtual_network_access: Optional[bool] = None,
        allow_forwarded_traffic: Optional[bool] = None,
        allow_gateway_transit: Optional[bool] = None,
        use_remote_gateways: Optional[bool] = None,
        databricks_virtual_network: Optional["VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork"] = None,
        databricks_address_space: Optional["AddressSpace"] = None,
        remote_address_space: Optional["AddressSpace"] = None,
        **kwargs
    ):
        super(VirtualNetworkPeering, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None
        self.allow_virtual_network_access = allow_virtual_network_access
        self.allow_forwarded_traffic = allow_forwarded_traffic
        self.allow_gateway_transit = allow_gateway_transit
        self.use_remote_gateways = use_remote_gateways
        self.databricks_virtual_network = databricks_virtual_network
        self.databricks_address_space = databricks_address_space
        self.remote_virtual_network = remote_virtual_network
        self.remote_address_space = remote_address_space
        self.peering_state = None
        self.provisioning_state = None


class VirtualNetworkPeeringList(msrest.serialization.Model):
    """Gets all virtual network peerings under a workspace.

    :param value: List of virtual network peerings on workspace.
    :type value: list[~azure.mgmt.databricks.models.VirtualNetworkPeering]
    :param next_link: URL to get the next set of virtual network peering list results if there are
     any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[VirtualNetworkPeering]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["VirtualNetworkPeering"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(VirtualNetworkPeeringList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork(msrest.serialization.Model):
    """The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).

    :param id: The Id of the databricks virtual network.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork, self).__init__(**kwargs)
        self.id = id


class VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork(msrest.serialization.Model):
    """The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).

    :param id: The Id of the remote virtual network.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork, self).__init__(**kwargs)
        self.id = id


class Workspace(TrackedResource):
    """Information about workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.databricks.models.Sku
    :param managed_resource_group_id: Required. The managed resource group Id.
    :type managed_resource_group_id: str
    :param parameters: The workspace's custom parameters.
    :type parameters: ~azure.mgmt.databricks.models.WorkspaceCustomParameters
    :ivar provisioning_state: The workspace provisioning state. Possible values include:
     "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled",
     "Failed", "Succeeded", "Updating".
    :vartype provisioning_state: str or ~azure.mgmt.databricks.models.ProvisioningState
    :param ui_definition_uri: The blob URI where the UI definition file is located.
    :type ui_definition_uri: str
    :param authorizations: The workspace provider authorizations.
    :type authorizations: list[~azure.mgmt.databricks.models.WorkspaceProviderAuthorization]
    :param created_by: Indicates the Object ID, PUID and Application ID of entity that created the
     workspace.
    :type created_by: ~azure.mgmt.databricks.models.CreatedBy
    :param updated_by: Indicates the Object ID, PUID and Application ID of entity that last updated
     the workspace.
    :type updated_by: ~azure.mgmt.databricks.models.CreatedBy
    :ivar created_date_time: Specifies the date and time when the workspace is created.
    :vartype created_date_time: ~datetime.datetime
    :ivar workspace_id: The unique identifier of the databricks workspace in databricks control
     plane.
    :vartype workspace_id: str
    :ivar workspace_url: The workspace URL which is of the format
     'adb-{workspaceId}.{random}.azuredatabricks.net'.
    :vartype workspace_url: str
    :param storage_account_identity: The details of Managed Identity of Storage Account.
    :type storage_account_identity: ~azure.mgmt.databricks.models.ManagedIdentityConfiguration
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_resource_group_id': {'required': True},
        'provisioning_state': {'readonly': True},
        'created_date_time': {'readonly': True},
        'workspace_id': {'readonly': True},
        'workspace_url': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'WorkspaceCustomParameters'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'ui_definition_uri': {'key': 'properties.uiDefinitionUri', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[WorkspaceProviderAuthorization]'},
        'created_by': {'key': 'properties.createdBy', 'type': 'CreatedBy'},
        'updated_by': {'key': 'properties.updatedBy', 'type': 'CreatedBy'},
        'created_date_time': {'key': 'properties.createdDateTime', 'type': 'iso-8601'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
        'workspace_url': {'key': 'properties.workspaceUrl', 'type': 'str'},
        'storage_account_identity': {'key': 'properties.storageAccountIdentity', 'type': 'ManagedIdentityConfiguration'},
    }

    def __init__(
        self,
        *,
        location: str,
        managed_resource_group_id: str,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["Sku"] = None,
        parameters: Optional["WorkspaceCustomParameters"] = None,
        ui_definition_uri: Optional[str] = None,
        authorizations: Optional[List["WorkspaceProviderAuthorization"]] = None,
        created_by: Optional["CreatedBy"] = None,
        updated_by: Optional["CreatedBy"] = None,
        storage_account_identity: Optional["ManagedIdentityConfiguration"] = None,
        **kwargs
    ):
        super(Workspace, self).__init__(tags=tags, location=location, **kwargs)
        self.sku = sku
        self.managed_resource_group_id = managed_resource_group_id
        self.parameters = parameters
        self.provisioning_state = None
        self.ui_definition_uri = ui_definition_uri
        self.authorizations = authorizations
        self.created_by = created_by
        self.updated_by = updated_by
        self.created_date_time = None
        self.workspace_id = None
        self.workspace_url = None
        self.storage_account_identity = storage_account_identity


class WorkspaceCustomBooleanParameter(msrest.serialization.Model):
    """The value which should be used for this field.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of variable that this is. Possible values include: "Bool", "Object",
     "String".
    :vartype type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: bool
    """

    _validation = {
        'type': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        value: bool,
        **kwargs
    ):
        super(WorkspaceCustomBooleanParameter, self).__init__(**kwargs)
        self.type = None
        self.value = value


class WorkspaceCustomObjectParameter(msrest.serialization.Model):
    """The value which should be used for this field.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of variable that this is. Possible values include: "Bool", "Object",
     "String".
    :vartype type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: object
    """

    _validation = {
        'type': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        value: object,
        **kwargs
    ):
        super(WorkspaceCustomObjectParameter, self).__init__(**kwargs)
        self.type = None
        self.value = value


class WorkspaceCustomParameters(msrest.serialization.Model):
    """Custom Parameters used for Cluster Creation.

    :param aml_workspace_id: The ID of a Azure Machine Learning workspace to link with Databricks
     workspace.
    :type aml_workspace_id: ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_virtual_network_id: The ID of a Virtual Network where this Databricks Cluster
     should be created.
    :type custom_virtual_network_id: ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_public_subnet_name: The name of a Public Subnet within the Virtual Network.
    :type custom_public_subnet_name: ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_private_subnet_name: The name of the Private Subnet within the Virtual Network.
    :type custom_private_subnet_name: ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param enable_no_public_ip: Should the Public IP be Disabled?.
    :type enable_no_public_ip: ~azure.mgmt.databricks.models.WorkspaceCustomBooleanParameter
    :param prepare_encryption: Prepare the workspace for encryption. Enables the Managed Identity
     for managed storage account.
    :type prepare_encryption: ~azure.mgmt.databricks.models.WorkspaceCustomBooleanParameter
    :param encryption: Contains the encryption details for Customer-Managed Key (CMK) enabled
     workspace.
    :type encryption: ~azure.mgmt.databricks.models.WorkspaceEncryptionParameter
    :param require_infrastructure_encryption: A boolean indicating whether or not the DBFS root
     file system will be enabled with secondary layer of encryption with platform managed keys for
     data at rest.
    :type require_infrastructure_encryption:
     ~azure.mgmt.databricks.models.WorkspaceCustomBooleanParameter
    """

    _attribute_map = {
        'aml_workspace_id': {'key': 'amlWorkspaceId', 'type': 'WorkspaceCustomStringParameter'},
        'custom_virtual_network_id': {'key': 'customVirtualNetworkId', 'type': 'WorkspaceCustomStringParameter'},
        'custom_public_subnet_name': {'key': 'customPublicSubnetName', 'type': 'WorkspaceCustomStringParameter'},
        'custom_private_subnet_name': {'key': 'customPrivateSubnetName', 'type': 'WorkspaceCustomStringParameter'},
        'enable_no_public_ip': {'key': 'enableNoPublicIp', 'type': 'WorkspaceCustomBooleanParameter'},
        'prepare_encryption': {'key': 'prepareEncryption', 'type': 'WorkspaceCustomBooleanParameter'},
        'encryption': {'key': 'encryption', 'type': 'WorkspaceEncryptionParameter'},
        'require_infrastructure_encryption': {'key': 'requireInfrastructureEncryption', 'type': 'WorkspaceCustomBooleanParameter'},
    }

    def __init__(
        self,
        *,
        aml_workspace_id: Optional["WorkspaceCustomStringParameter"] = None,
        custom_virtual_network_id: Optional["WorkspaceCustomStringParameter"] = None,
        custom_public_subnet_name: Optional["WorkspaceCustomStringParameter"] = None,
        custom_private_subnet_name: Optional["WorkspaceCustomStringParameter"] = None,
        enable_no_public_ip: Optional["WorkspaceCustomBooleanParameter"] = None,
        prepare_encryption: Optional["WorkspaceCustomBooleanParameter"] = None,
        encryption: Optional["WorkspaceEncryptionParameter"] = None,
        require_infrastructure_encryption: Optional["WorkspaceCustomBooleanParameter"] = None,
        **kwargs
    ):
        super(WorkspaceCustomParameters, self).__init__(**kwargs)
        self.aml_workspace_id = aml_workspace_id
        self.custom_virtual_network_id = custom_virtual_network_id
        self.custom_public_subnet_name = custom_public_subnet_name
        self.custom_private_subnet_name = custom_private_subnet_name
        self.enable_no_public_ip = enable_no_public_ip
        self.prepare_encryption = prepare_encryption
        self.encryption = encryption
        self.require_infrastructure_encryption = require_infrastructure_encryption


class WorkspaceCustomStringParameter(msrest.serialization.Model):
    """The Value.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of variable that this is. Possible values include: "Bool", "Object",
     "String".
    :vartype type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: str
    """

    _validation = {
        'type': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: str,
        **kwargs
    ):
        super(WorkspaceCustomStringParameter, self).__init__(**kwargs)
        self.type = None
        self.value = value


class WorkspaceEncryptionParameter(msrest.serialization.Model):
    """The object that contains details of encryption used on the workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The type of variable that this is. Possible values include: "Bool", "Object",
     "String".
    :vartype type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: The value which should be used for this field.
    :type value: ~azure.mgmt.databricks.models.Encryption
    """

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'Encryption'},
    }

    def __init__(
        self,
        *,
        value: Optional["Encryption"] = None,
        **kwargs
    ):
        super(WorkspaceEncryptionParameter, self).__init__(**kwargs)
        self.type = None
        self.value = value


class WorkspaceListResult(msrest.serialization.Model):
    """List of workspaces.

    :param value: The array of workspaces.
    :type value: list[~azure.mgmt.databricks.models.Workspace]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Workspace]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Workspace"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(WorkspaceListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class WorkspaceProviderAuthorization(msrest.serialization.Model):
    """The workspace provider authorization.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. The provider's principal identifier. This is the identity that
     the provider will use to call ARM to manage the workspace resources.
    :type principal_id: str
    :param role_definition_id: Required. The provider's role definition identifier. This role will
     define all the permissions that the provider must have on the workspace's container resource
     group. This role definition cannot have permission to delete the resource group.
    :type role_definition_id: str
    """

    _validation = {
        'principal_id': {'required': True},
        'role_definition_id': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        principal_id: str,
        role_definition_id: str,
        **kwargs
    ):
        super(WorkspaceProviderAuthorization, self).__init__(**kwargs)
        self.principal_id = principal_id
        self.role_definition_id = role_definition_id


class WorkspaceUpdate(msrest.serialization.Model):
    """An update to a workspace.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(WorkspaceUpdate, self).__init__(**kwargs)
        self.tags = tags
