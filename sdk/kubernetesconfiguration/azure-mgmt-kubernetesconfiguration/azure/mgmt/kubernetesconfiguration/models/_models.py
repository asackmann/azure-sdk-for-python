# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ComplianceStatus(msrest.serialization.Model):
    """Compliance Status details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_state: The compliance state of the configuration. Possible values include:
     "Pending", "Compliant", "Noncompliant", "Installed", "Failed".
    :vartype compliance_state: str or
     ~azure.mgmt.kubernetesconfiguration.models.ComplianceStateType
    :param last_config_applied: Datetime the configuration was last applied.
    :type last_config_applied: ~datetime.datetime
    :param message: Message from when the configuration was applied.
    :type message: str
    :param message_level: Level of the message. Possible values include: "Error", "Warning",
     "Information".
    :type message_level: str or ~azure.mgmt.kubernetesconfiguration.models.MessageLevelType
    """

    _validation = {
        'compliance_state': {'readonly': True},
    }

    _attribute_map = {
        'compliance_state': {'key': 'complianceState', 'type': 'str'},
        'last_config_applied': {'key': 'lastConfigApplied', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'message_level': {'key': 'messageLevel', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ComplianceStatus, self).__init__(**kwargs)
        self.compliance_state = None
        self.last_config_applied = kwargs.get('last_config_applied', None)
        self.message = kwargs.get('message', None)
        self.message_level = kwargs.get('message_level', None)


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Service specific error code which serves as the substatus for the HTTP
     error code.
    :type code: str
    :param message: Required. Description of the error.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: Error definition.
    :vartype error: ~azure.mgmt.kubernetesconfiguration.models.ErrorDefinition
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = None


class HelmOperatorProperties(msrest.serialization.Model):
    """Properties for Helm operator.

    :param chart_version: Version of the operator Helm chart.
    :type chart_version: str
    :param chart_values: Values override for the operator Helm chart.
    :type chart_values: str
    """

    _attribute_map = {
        'chart_version': {'key': 'chartVersion', 'type': 'str'},
        'chart_values': {'key': 'chartValues', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(HelmOperatorProperties, self).__init__(**kwargs)
        self.chart_version = kwargs.get('chart_version', None)
        self.chart_values = kwargs.get('chart_values', None)


class Resource(msrest.serialization.Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata https://github.com/Azure/azure-resource-manager-
     rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.models.SystemData
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
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = kwargs.get('system_data', None)


class ProxyResource(Resource):
    """ARM proxy resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata https://github.com/Azure/azure-resource-manager-
     rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.models.SystemData
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
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operation of this resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param name: Operation name, in format of {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~azure.mgmt.kubernetesconfiguration.models.ResourceProviderOperationDisplay
    :ivar is_data_action: The flag that indicates whether the operation applies to data plane.
    :vartype is_data_action: bool
    """

    _validation = {
        'is_data_action': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.is_data_action = None


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft KubernetesConfiguration.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ResourceProviderOperationList(msrest.serialization.Model):
    """Result of the request to list operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of operations supported by this resource provider.
    :type value: list[~azure.mgmt.kubernetesconfiguration.models.ResourceProviderOperation]
    :ivar next_link: URL to the next set of results, if any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None


class Result(msrest.serialization.Model):
    """Sample result definition.

    :param sample_property: Sample property of type string.
    :type sample_property: str
    """

    _attribute_map = {
        'sample_property': {'key': 'sampleProperty', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Result, self).__init__(**kwargs)
        self.sample_property = kwargs.get('sample_property', None)


class SourceControlConfiguration(Resource):
    """The SourceControl Configuration object returned in Get & Put response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata https://github.com/Azure/azure-resource-manager-
     rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.models.SystemData
    :param repository_url: Url of the SourceControl Repository.
    :type repository_url: str
    :param operator_namespace: The namespace to which this operator is installed to. Maximum of 253
     lower case alphanumeric characters, hyphen and period only.
    :type operator_namespace: str
    :param operator_instance_name: Instance name of the operator - identifying the specific
     configuration.
    :type operator_instance_name: str
    :param operator_type: Type of the operator. Possible values include: "Flux".
    :type operator_type: str or ~azure.mgmt.kubernetesconfiguration.models.OperatorType
    :param operator_params: Any Parameters for the Operator instance in string format.
    :type operator_params: str
    :param configuration_protected_settings: Name-value pairs of protected configuration settings
     for the configuration.
    :type configuration_protected_settings: dict[str, str]
    :param operator_scope: Scope at which the operator will be installed. Possible values include:
     "cluster", "namespace". Default value: "cluster".
    :type operator_scope: str or ~azure.mgmt.kubernetesconfiguration.models.OperatorScopeType
    :ivar repository_public_key: Public Key associated with this SourceControl configuration
     (either generated within the cluster or provided by the user).
    :vartype repository_public_key: str
    :param ssh_known_hosts_contents: Base64-encoded known_hosts contents containing public SSH keys
     required to access private Git instances.
    :type ssh_known_hosts_contents: str
    :param enable_helm_operator: Option to enable Helm Operator for this git configuration.
     Possible values include: "true", "false".
    :type enable_helm_operator: str or
     ~azure.mgmt.kubernetesconfiguration.models.EnableHelmOperatorType
    :param helm_operator_properties: Properties for Helm operator.
    :type helm_operator_properties:
     ~azure.mgmt.kubernetesconfiguration.models.HelmOperatorProperties
    :ivar provisioning_state: The provisioning state of the resource provider. Possible values
     include: "Accepted", "Deleting", "Running", "Succeeded", "Failed".
    :vartype provisioning_state: str or
     ~azure.mgmt.kubernetesconfiguration.models.ProvisioningStateType
    :ivar compliance_status: Compliance Status of the Configuration.
    :vartype compliance_status: ~azure.mgmt.kubernetesconfiguration.models.ComplianceStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'repository_public_key': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'compliance_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'repository_url': {'key': 'properties.repositoryUrl', 'type': 'str'},
        'operator_namespace': {'key': 'properties.operatorNamespace', 'type': 'str'},
        'operator_instance_name': {'key': 'properties.operatorInstanceName', 'type': 'str'},
        'operator_type': {'key': 'properties.operatorType', 'type': 'str'},
        'operator_params': {'key': 'properties.operatorParams', 'type': 'str'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
        'operator_scope': {'key': 'properties.operatorScope', 'type': 'str'},
        'repository_public_key': {'key': 'properties.repositoryPublicKey', 'type': 'str'},
        'ssh_known_hosts_contents': {'key': 'properties.sshKnownHostsContents', 'type': 'str'},
        'enable_helm_operator': {'key': 'properties.enableHelmOperator', 'type': 'str'},
        'helm_operator_properties': {'key': 'properties.helmOperatorProperties', 'type': 'HelmOperatorProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'compliance_status': {'key': 'properties.complianceStatus', 'type': 'ComplianceStatus'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourceControlConfiguration, self).__init__(**kwargs)
        self.repository_url = kwargs.get('repository_url', None)
        self.operator_namespace = kwargs.get('operator_namespace', "default")
        self.operator_instance_name = kwargs.get('operator_instance_name', None)
        self.operator_type = kwargs.get('operator_type', None)
        self.operator_params = kwargs.get('operator_params', None)
        self.configuration_protected_settings = kwargs.get('configuration_protected_settings', None)
        self.operator_scope = kwargs.get('operator_scope', "cluster")
        self.repository_public_key = None
        self.ssh_known_hosts_contents = kwargs.get('ssh_known_hosts_contents', None)
        self.enable_helm_operator = kwargs.get('enable_helm_operator', None)
        self.helm_operator_properties = kwargs.get('helm_operator_properties', None)
        self.provisioning_state = None
        self.compliance_status = None


class SourceControlConfigurationList(msrest.serialization.Model):
    """Result of the request to list Source Control Configurations.  It contains a list of SourceControlConfiguration objects and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Source Control Configurations within a Kubernetes cluster.
    :vartype value: list[~azure.mgmt.kubernetesconfiguration.models.SourceControlConfiguration]
    :ivar next_link: URL to get the next set of configuration objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SourceControlConfiguration]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourceControlConfigurationList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class SystemData(msrest.serialization.Model):
    """Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar created_by: A string identifier for the identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource: user, application,
     managedIdentity, key.
    :vartype created_by_type: str
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: A string identifier for the identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource: user,
     application, managedIdentity, key.
    :vartype last_modified_by_type: str
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _validation = {
        'created_by': {'readonly': True},
        'created_by_type': {'readonly': True},
        'created_at': {'readonly': True},
        'last_modified_by': {'readonly': True},
        'last_modified_by_type': {'readonly': True},
        'last_modified_at': {'readonly': True},
    }

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = None
        self.created_by_type = None
        self.created_at = None
        self.last_modified_by = None
        self.last_modified_by_type = None
        self.last_modified_at = None
