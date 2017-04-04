from .base import CloudDriver

__all__ = ['DevstackDriver']


class DevstackDriver(CloudDriver):

    _services = {
        'keystone': {'id': 'apache2',
                     'type': 'linux'}
    }
