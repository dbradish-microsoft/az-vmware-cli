# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .quota_py3 import Quota
    from .resource_py3 import Resource
    from .tracked_resource_py3 import TrackedResource
    from .api_error_base_py3 import ApiErrorBase
    from .api_error_py3 import ApiError, ApiErrorException
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .express_route_authorization_py3 import ExpressRouteAuthorization
    from .circuit_py3 import Circuit
    from .endpoints_py3 import Endpoints
    from .identity_source_py3 import IdentitySource
    from .sku_py3 import Sku
    from .default_cluster_properties_py3 import DefaultClusterProperties
    from .private_cloud_properties_py3 import PrivateCloudProperties
    from .private_cloud_py3 import PrivateCloud
    from .cluster_properties_py3 import ClusterProperties
    from .cluster_py3 import Cluster
    from .admin_credentials_py3 import AdminCredentials
except (SyntaxError, ImportError):
    from .quota import Quota
    from .resource import Resource
    from .tracked_resource import TrackedResource
    from .api_error_base import ApiErrorBase
    from .api_error import ApiError, ApiErrorException
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .express_route_authorization import ExpressRouteAuthorization
    from .circuit import Circuit
    from .endpoints import Endpoints
    from .identity_source import IdentitySource
    from .sku import Sku
    from .default_cluster_properties import DefaultClusterProperties
    from .private_cloud_properties import PrivateCloudProperties
    from .private_cloud import PrivateCloud
    from .cluster_properties import ClusterProperties
    from .cluster import Cluster
    from .admin_credentials import AdminCredentials
from .operation_paged import OperationPaged
from .private_cloud_paged import PrivateCloudPaged
from .cluster_paged import ClusterPaged
from .virtustream_client_enums import (
    QuotaEnabled,
    SslEnum,
    PrivateCloudProvisioningState,
    InternetEnum,
    ClusterProvisioningState,
)

__all__ = [
    'Quota',
    'Resource',
    'TrackedResource',
    'ApiErrorBase',
    'ApiError', 'ApiErrorException',
    'OperationDisplay',
    'Operation',
    'ExpressRouteAuthorization',
    'Circuit',
    'Endpoints',
    'IdentitySource',
    'Sku',
    'DefaultClusterProperties',
    'PrivateCloudProperties',
    'PrivateCloud',
    'ClusterProperties',
    'Cluster',
    'AdminCredentials',
    'OperationPaged',
    'PrivateCloudPaged',
    'ClusterPaged',
    'QuotaEnabled',
    'SslEnum',
    'PrivateCloudProvisioningState',
    'InternetEnum',
    'ClusterProvisioningState',
]
