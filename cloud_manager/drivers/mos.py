from .base import CloudDriver

__all__ = ['MosDriver']


class MosDriver(CloudDriver):

    _services = {
        'keystone': {'id': 'apache2',
                     'type': 'linux'}
    }
