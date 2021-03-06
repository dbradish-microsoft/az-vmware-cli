# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterUpdate(Model):
    """An update of a cluster resource.

    :param cluster_size: The cluster size
    :type cluster_size: int
    """

    _attribute_map = {
        'cluster_size': {'key': 'properties.clusterSize', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ClusterUpdate, self).__init__(**kwargs)
        self.cluster_size = kwargs.get('cluster_size', None)
