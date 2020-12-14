# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import RecoveryServicesClientConfiguration
from .operations import VaultCertificatesOperations
from .operations import RegisteredIdentitiesOperations
from .operations import ReplicationUsagesOperations
from .operations import PrivateLinkResourcesOperations
from .operations import RecoveryServicesOperations
from .operations import VaultsOperations
from .operations import Operations
from .operations import VaultExtendedInfoOperations
from .operations import UsagesOperations
from . import models


class RecoveryServicesClient(object):
    """Recovery Services Client.

    :ivar vault_certificates: VaultCertificatesOperations operations
    :vartype vault_certificates: azure.mgmt.recoveryservices.operations.VaultCertificatesOperations
    :ivar registered_identities: RegisteredIdentitiesOperations operations
    :vartype registered_identities: azure.mgmt.recoveryservices.operations.RegisteredIdentitiesOperations
    :ivar replication_usages: ReplicationUsagesOperations operations
    :vartype replication_usages: azure.mgmt.recoveryservices.operations.ReplicationUsagesOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.recoveryservices.operations.PrivateLinkResourcesOperations
    :ivar recovery_services: RecoveryServicesOperations operations
    :vartype recovery_services: azure.mgmt.recoveryservices.operations.RecoveryServicesOperations
    :ivar vaults: VaultsOperations operations
    :vartype vaults: azure.mgmt.recoveryservices.operations.VaultsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservices.operations.Operations
    :ivar vault_extended_info: VaultExtendedInfoOperations operations
    :vartype vault_extended_info: azure.mgmt.recoveryservices.operations.VaultExtendedInfoOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.recoveryservices.operations.UsagesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = RecoveryServicesClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.vault_certificates = VaultCertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.registered_identities = RegisteredIdentitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_usages = ReplicationUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recovery_services = RecoveryServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vaults = VaultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vault_extended_info = VaultExtendedInfoOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> RecoveryServicesClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
