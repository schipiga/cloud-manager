class NodeCollection(object):

    def __init__(self, driver, nodes_config, any_services=None):
        self._driver = driver
        self._nodes_config = nodes_config

        for node in self._nodes_config:
            if not node.get('services'):
                self._driver.get_processes

        for service_name in any_services:
            for node in self._nodes_config:
                node['hosts'][0]

    def poweron(self):
        for host in self._nodes_config['hosts']:
            self._driver.poweron(host)

    def poweroff(self):
        pass

    def reset(self):
        pass

    def reboot(self):
        pass

    def shutdown(self):
        pass

    def snapshot(self):
        pass

    def revert(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_services(self):
        pass
