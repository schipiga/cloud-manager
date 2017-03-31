from .node import NodeCollection


class ServiceCollection(object):

    def __init__(self, driver, config, any_nodes=None, all_nodes=None):
        self._driver = driver

    def restart(self):
        self.driver.restart_service(service_name, hosts)

    def poweron(self):
        pass

    def poweroff(self):
        pass

    def terminate(self):
        pass

    def get_nodes(self):
        return NodeCollection(self._driver, self._config, any_services=self)
