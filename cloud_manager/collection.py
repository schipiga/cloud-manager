from .config import Configurable
from .drivers import DevstackDriver, McpDriver, MosDriver


class CloudCollection(Configurable):

    def __init__(self, config, resources=None):
        super(CloudCollection, self).__init__(config)
        self._resources = set(resources) or set()

        self._driver = {
            'devstack': DevstackDriver,
            'mcp': McpDriver,
            'mos': MosDriver
        }[self._config['cloud']['type']](self._config)

        for node in self._config['cloud']['nodes']:
            if not node.get('services'):
                node['services'] = self._driver.get_services(node['hosts'][0])

    def __sub__(self, collection):
        self._resources -= collection._resources

    def __and__(self, collection):
        self._resources &= collection._resources

    def __or__(self, collection):
        self._resources |= collection._resources

    def __xor__(self, collection):
        self._resources ^= collection._resources

    def __add__(self, collection):
        self.__or__(collection)

    def __len__(self):
        return len(self._resources)

    def __contains__(self, collection):
        return collection._resources.issubset(self._resources)

    def __iter__(self):
        for resource in self._resources:
            yield type(self)(self._config, [resource])
