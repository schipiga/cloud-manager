from .base import CloudDriver

__all__ = ['McpDriver']


class McpDriver(CloudDriver):

    def start_service(self, service_name, hosts):
        service = self._config['cloud']['services'][service_name]
        if service['type'] == 'salt':
            cmd = ('salt-call --local --retcode-passthrough service.start ' +
                   service['id'])

        self._command_executor.execute(cmd, hosts)
