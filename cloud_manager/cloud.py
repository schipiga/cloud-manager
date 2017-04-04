from .config import Configurable, Config
from .node import NodeCollection
from .service import ServiceCollection


class Cloud(Configurable):

    def __init__(self, config=None, config_path=None):
        config = config or Config.from_file(config_path)
        super(Cloud, self).__init__(config)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_nodes(self, any_services=None, all_services=None):
        return NodeCollection(self._config, any_services, all_services)

    def get_services(self, any_hosts=None, all_hosts=None):
        return ServiceCollection(self._config, any_hosts, all_hosts)
