from .collection import CloudCollection
from .service import ServiceCollection


class NodeCollection(CloudCollection):

    def __init__(self,
                 config,
                 hosts=None,
                 any_services=None,
                 all_services=None):
        super(NodeCollection, self).__init__(config)

        self._hosts = self._resources
        for node in self._config['cloud']['nodes']:
            should_add = True
            added_host = None

            if hosts:
                for host in hosts:
                    if host in node['hosts']:
                        added_host = host
                        break
            else:
                added_host = node['hosts'][0]

            if any_services:
                for service_name in any_services:
                    if service_name in node['services']:
                        should_add = True
                        break
                else:
                    should_add = False

            if all_services:
                for service_name in any_services:
                    if service_name not in node['services']:
                        should_add = False
                        break
                else:
                    should_add = True

            if should_add and added_host:
                self._hosts.add(added_host)

    def poweron(self):
        self._driver.poweron(self._hosts)

    def poweroff(self):
        self._driver.poweroff(self._hosts)

    def reset(self):
        self._driver.reset(self._hosts)

    def reboot(self):
        self._driver.reboot(self._hosts)

    def shutdown(self):
        self._driver.shutdown(self._hosts)

    def snapshot(self):
        self._driver.snapshot(self._hosts)

    def revert(self):
        self._driver.revert(self._hosts)

    def execute(self, cmd):
        self._driver.execute(cmd, self._hosts)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_services(self):
        return ServiceCollection(self._config, any_hosts=self._hosts)
