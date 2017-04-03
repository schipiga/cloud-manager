from cloud_manager.config import Configurable

from .executors import AnsibleExecutor, IpmiExecutor, LibvirtExecutor


class CloudDriver(Configurable):

    def __init__(self, config):
        super(CloudDriver, self).__init__(config)
        self._command_executor = AnsibleExecutor(self._config)
        self._machine_executor = {
            'virtual': LibvirtExecutor,
            'bare': IpmiExecutor
        }[self._config['hardware']['type']](self._config)

    def poweron(self, host):
        self._machine_executor.poweron(host)

    def start_service(self, service_name, host):
        pass

    def stop_service(self, service_name, host):
        pass

    def restart_service(self, service_name, host):
        pass
