from cloud_manager.config import Configurable

from .executors import AnsibleExecutor, IpmiExecutor, LibvirtExecutor

__all__ = ['CloudDriver']


class CloudDriver(Configurable):

    def __init__(self, config):
        super(CloudDriver, self).__init__(config)
        self._inject_services()

        self._command_executor = AnsibleExecutor(self._config)
        self._machine_executor = {
            'virtual': LibvirtExecutor,
            'bare': IpmiExecutor
        }[self._config['hardware']['type']](self._config)

    def poweron(self, hosts):
        self._machine_executor.poweron(hosts)

    def poweroff(self, hosts):
        self._machine_executor.poweroff(hosts)

    def reset(self, hosts):
        self._machine_executor.reset(hosts)

    def shutdown(self, hosts):
        self._machine_executor.shutdown(hosts)

    def snapshot(self, hosts):
        self._machine_executor.snapshot(hosts)

    def revert(self, hosts):
        self._machine_executor.revert(hosts)

    def execute(self, cmd, hosts):
        self._command_executor.execute(cmd, hosts)

    def start_service(self, service_name, hosts):
        cmd = self._service_cmd(service_name, cmd_type='start')
        self._command_executor.execute(cmd, hosts)

    def stop_service(self, service_name, hosts):
        cmd = self._service_cmd(service_name, cmd_type='stop')
        self._command_executor.execute(cmd, hosts)

    def restart_service(self, service_name, hosts):
        cmd = self._service_cmd(service_name, cmd_type='restart')
        self._command_executor.execute(cmd, hosts)

    def get_services(self, host):
        pass

    def _service_cmd(self, service_name, cmd_type):
        assert cmd_type in ('start', 'stop', 'restart')
        service = self._config['services'][service_name]
        s_type = service['type']
        s_id = service['id']

        if s_type == 'salt':
            cmd = ('salt-call --local --retcode-passthrough '
                   'service.{} {}'.format(cmd_type, s_id))

        if s_type == 'linux':
            cmd = 'service {} {}'.format(s_id, cmd_type)

        if s_type == 'pcs':
            cmd_type = {'start': 'clear',
                        'stop': 'ban'}.get(cmd_type, cmd_type)
            cmd = 'pcs resource {} {} $(hostname)'.format(cmd_type, s_id)

        if s_type == 'screen':
            if cmd_type == 'start':
                cmd = ("screen -S stack -p {} -X "
                       "stuff $'\\033[A'$(printf \\\\r)".format(s_id))
            if cmd_type == 'stop':
                cmd = ("screen -S stack -p {} -X "
                       "stuff $'\\003'".format(s_id))
            if cmd_type == 'restart':
                cmd = ("screen -S stack -p {} -X "
                       "stuff $'\\003'$'\\033[A'$(printf \\\\r)".format(s_id))

        else:
            raise ValueError('Undefined service type: ' + s_type)

        return cmd

    def _inject_services(self):
        config_services = self._config.setdefault('services', {})
        for key, val in self._services:
            config_services.setdefault(key, val)

    @property
    def _services(self):
        raise NotImplemented()
