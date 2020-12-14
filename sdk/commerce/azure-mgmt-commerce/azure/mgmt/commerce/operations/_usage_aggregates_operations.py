# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UsageAggregatesOperations(object):
    """UsageAggregatesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.commerce.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        reported_start_time,  # type: datetime.datetime
        reported_end_time,  # type: datetime.datetime
        show_details=None,  # type: Optional[bool]
        aggregation_granularity="Daily",  # type: Optional[Union[str, "models.AggregationGranularity"]]
        continuation_token_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.UsageAggregationListResult"]
        """Query aggregated Azure subscription consumption data for a date range.

        :param reported_start_time: The start of the time range to retrieve data for.
        :type reported_start_time: ~datetime.datetime
        :param reported_end_time: The end of the time range to retrieve data for.
        :type reported_end_time: ~datetime.datetime
        :param show_details: ``True`` returns usage data in instance-level detail, ``false`` causes
         server-side aggregation with fewer details. For example, if you have 3 website instances, by
         default you will get 3 line items for website consumption. If you specify showDetails = false,
         the data will be aggregated as a single line item for website consumption within the time
         period (for the given subscriptionId, meterId, usageStartTime and usageEndTime).
        :type show_details: bool
        :param aggregation_granularity: ``Daily`` (default) returns the data in daily granularity,
         ``Hourly`` returns the data in hourly granularity.
        :type aggregation_granularity: str or ~azure.mgmt.commerce.models.AggregationGranularity
        :param continuation_token_parameter: Used when a continuation token string is provided in the
         response body of the previous call, enabling paging through a large result set. If not present,
         the data is retrieved from the beginning of the day/hour (based on the granularity) passed in.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either UsageAggregationListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.commerce.models.UsageAggregationListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.UsageAggregationListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-06-01-preview"
        accept = "application/json, text/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['reportedStartTime'] = self._serialize.query("reported_start_time", reported_start_time, 'iso-8601')
                query_parameters['reportedEndTime'] = self._serialize.query("reported_end_time", reported_end_time, 'iso-8601')
                if show_details is not None:
                    query_parameters['showDetails'] = self._serialize.query("show_details", show_details, 'bool')
                if aggregation_granularity is not None:
                    query_parameters['aggregationGranularity'] = self._serialize.query("aggregation_granularity", aggregation_granularity, 'str')
                if continuation_token_parameter is not None:
                    query_parameters['continuationToken'] = self._serialize.query("continuation_token_parameter", continuation_token_parameter, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('UsageAggregationListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Commerce/UsageAggregates'}  # type: ignore
