from .drivers import DevstackDriver, McpDriver, MosDriver
from .node import NodeCollection
from .service import ServiceCollection


class Cloud(object):

    def __init__(self, config=None, config_path=None):
        self._config = config
        driver_cls = {'devstack': DevstackDriver,
                      'mcp': McpDriver,
                      'mos': MosDriver}[self._config['cloud_type']]
        self._driver = driver_cls(hardware_type=self._config['hardware_type'])

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_nodes(self, any_services=None, all_services=None):
        return NodeCollection(
            self._driver, self._config['nodes'], any_services, all_services)

    def get_services(self, any_nodes=None, all_nodes=None):
        return ServiceCollection(
            self._driver, self._config['services'], any_nodes, all_nodes)
