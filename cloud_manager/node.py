from .driver import Driverable
from .service import ServiceCollection


class NodeCollection(Driverable):

    def __init__(self,
                 config,
                 hosts=None,
                 any_services=None,
                 all_services=None):
        super(NodeCollection, self).__init__(config)

        self._hosts = set()
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
        return ServiceCollection(self._config, any_hosts=self._hosts)
