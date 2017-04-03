from .config import Configurable
from .drivers import DevstackDriver, McpDriver, MosDriver


class Driverable(Configurable):

    def __init__(self, config):
        super(Driverable, self).__init__(config)

        self._driver = {
            'devstack': DevstackDriver,
            'mcp': McpDriver,
            'mos': MosDriver
        }[self._config['cloud']['type']](self._config)

        for node in self._config['cloud']['nodes']:
            if not node.get('services'):
                node['services'] = self._driver.get_services(node['hosts'][0])
