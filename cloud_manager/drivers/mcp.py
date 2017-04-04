from .base import CloudDriver

__all__ = ['McpDriver']


class McpDriver(CloudDriver):

    _services = {
        'keystone': {'id': 'keystone',
                     'type': 'salt'}
    }
