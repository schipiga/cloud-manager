"""
------
Config
------

Supported formats are json, yaml.
Example in json:

{
    "services": {
        "keystone": {"id": "apache2", "type": "linux"},
        "horizon": {"id": "apache2", "type": "linux"},
        "rabbitmq": {"id": "p_rabbitmq-server", "type": "pcs"}
    },
    "cloud": {
        "type": "mos",
        "ssh": {"username": "admin", "password": "admin"},
        "nodes": [
            {"hosts": ["192.168.0.1", "192.168.1.1"],
             "ssh": {"username": "root", "password": "root"},
             "services": ["keystone", "horizon", "nova"]
            },
            {"hosts": ["192.168.0.2", "192.168.1.2"]}
        ]
    },
    "hardware": {"type": "virtual"}
}
"""

__all__ = ['Configurable']


class Configurable(object):

    def __init__(self, config):
        self._config = config
