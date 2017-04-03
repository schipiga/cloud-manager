from .config import Configurable
from .node import NodeCollection
from .service import ServiceCollection


class Cloud(Configurable):

    def __init__(self, config=None, config_path=None):
        super(Cloud, self).__init__(config)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_nodes(self, any_services=None, all_services=None):
        return NodeCollection(self._config, any_services, all_services)

    def get_services(self, any_nodes=None, all_nodes=None):
        return ServiceCollection(self._config, any_nodes, all_nodes)
