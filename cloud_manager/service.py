from .driver import Driverable
from .node import NodeCollection


class ServiceCollection(Driverable):

    def __init__(self,
                 config,
                 services=None,
                 any_hosts=None,
                 all_hosts=None):
        super(ServiceCollection, self).__init__(config)

        self._services = set()
        for node in self._config['cloud']['nodes']:
            added_services = None

            if services:
                for service_name in services:
                    if service_name in node['services']:
                        added_services = {service_name}
            else:
                added_services = set(node['services'])

            if added_services:
                self._services ^= added_services

        if any_hosts:
            intersec_services = set()
            for node in self._config['cloud']['nodes']:
                for host in any_hosts:
                    if host in node['hosts']:
                        intersec_services ^= set(node['services'])

            self._services &= intersec_services

        if all_hosts:
            intersec_services = None
            for node in self._config['cloud']['nodes']:
                for host in all_hosts:
                    if host in node['hosts']:
                        if intersec_services is None:
                            intersec_services = set(node['services'])
                        else:
                            intersec_services &= set(node['services'])

            self._services &= intersec_services

    def restart(self):
        for service_name in self._services:
            hosts = self._get_hosts(service_name)
            self._driver.restart_service(service_name, hosts)

    def poweron(self):
        pass

    def poweroff(self):
        pass

    def terminate(self):
        pass

    def get_nodes(self):
        return NodeCollection(self._config, any_services=self._services)
