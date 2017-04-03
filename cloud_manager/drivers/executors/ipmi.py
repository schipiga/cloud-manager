from .base import MachineExecutor


class IpmiExecutor(MachineExecutor):

    def poweron(self, host):
        self._power_cmd(host, cmd='on', expected_state='on')

    def poweroff(self, host):
        self._power_cmd(host, cmd='off', expected_state='off')
