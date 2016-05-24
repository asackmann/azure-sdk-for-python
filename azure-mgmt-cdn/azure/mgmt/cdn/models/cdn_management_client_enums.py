# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class SkuName(Enum):

    standard_verizon = "Standard_Verizon"
    premium_verizon = "Premium_Verizon"
    custom_verizon = "Custom_Verizon"
    standard_akamai = "Standard_Akamai"


class ProfileResourceState(Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"
    disabled = "Disabled"


class ProvisioningState(Enum):

    creating = "Creating"
    succeeded = "Succeeded"
    failed = "Failed"


class QueryStringCachingBehavior(Enum):

    ignore_query_string = "IgnoreQueryString"
    bypass_caching = "BypassCaching"
    use_query_string = "UseQueryString"
    not_set = "NotSet"


class EndpointResourceState(Enum):

    creating = "Creating"
    deleting = "Deleting"
    running = "Running"
    starting = "Starting"
    stopped = "Stopped"
    stopping = "Stopping"


class OriginResourceState(Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"


class CustomDomainResourceState(Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"


class ResourceType(Enum):

    microsoft_cdn_profiles_endpoints = "Microsoft.Cdn/Profiles/Endpoints"
