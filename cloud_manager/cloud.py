import yaml

from .config import Configurable
from .node import NodeCollection
from .service import ServiceCollection

__all__ = ['Cloud']


class Cloud(Configurable):

    def __init__(self, config=None, config_path=None):
        if not config:
            with open(config_path) as config_file:
                config = yaml.safe_load(config_file.read())
        super(Cloud, self).__init__(config)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_nodes(self, any_services=None, all_services=None):
        return NodeCollection(self._config, any_services, all_services)

    def get_services(self, any_hosts=None, all_hosts=None):
        return ServiceCollection(self._config, any_hosts, all_hosts)
