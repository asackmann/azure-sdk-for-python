# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class IntegrationRuntimeNodesOperations:
    """IntegrationRuntimeNodesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.synapse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        workspace_name: str,
        integration_runtime_name: str,
        node_name: str,
        **kwargs
    ) -> "_models.SelfHostedIntegrationRuntimeNode":
        """Get integration runtime node.

        Get an integration runtime node.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param integration_runtime_name: Integration runtime name.
        :type integration_runtime_name: str
        :param node_name: Integration runtime node name.
        :type node_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SelfHostedIntegrationRuntimeNode, or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.SelfHostedIntegrationRuntimeNode
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SelfHostedIntegrationRuntimeNode"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'integrationRuntimeName': self._serialize.url("integration_runtime_name", integration_runtime_name, 'str'),
            'nodeName': self._serialize.url("node_name", node_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SelfHostedIntegrationRuntimeNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}'}  # type: ignore

    async def update(
        self,
        resource_group_name: str,
        workspace_name: str,
        integration_runtime_name: str,
        node_name: str,
        update_integration_runtime_node_request: "_models.UpdateIntegrationRuntimeNodeRequest",
        **kwargs
    ) -> "_models.SelfHostedIntegrationRuntimeNode":
        """Create integration runtime node.

        Create an integration runtime node.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param integration_runtime_name: Integration runtime name.
        :type integration_runtime_name: str
        :param node_name: Integration runtime node name.
        :type node_name: str
        :param update_integration_runtime_node_request: The parameters for updating an integration
         runtime node.
        :type update_integration_runtime_node_request: ~azure.mgmt.synapse.models.UpdateIntegrationRuntimeNodeRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SelfHostedIntegrationRuntimeNode, or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.SelfHostedIntegrationRuntimeNode
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SelfHostedIntegrationRuntimeNode"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'integrationRuntimeName': self._serialize.url("integration_runtime_name", integration_runtime_name, 'str'),
            'nodeName': self._serialize.url("node_name", node_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(update_integration_runtime_node_request, 'UpdateIntegrationRuntimeNodeRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SelfHostedIntegrationRuntimeNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        workspace_name: str,
        integration_runtime_name: str,
        node_name: str,
        **kwargs
    ) -> None:
        """Delete integration runtime node.

        Delete an integration runtime node.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param integration_runtime_name: Integration runtime name.
        :type integration_runtime_name: str
        :param node_name: Integration runtime node name.
        :type node_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'integrationRuntimeName': self._serialize.url("integration_runtime_name", integration_runtime_name, 'str'),
            'nodeName': self._serialize.url("node_name", node_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}'}  # type: ignore
