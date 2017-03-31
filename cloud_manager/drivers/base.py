from .executors import AnsibleExecutor, IpmiExecutor, LibvirtExecutor


class CloudDriver(object):

    def __init__(self, config):
        self._config = config
        self._command_executor = AnsibleExecutor()
        self._machine_executor = {'virtual': LibvirtExecutor,
                                  'bare': IpmiExecutor}()

    def poweron(self, host):
        self._machine_executor.poweron(host)
