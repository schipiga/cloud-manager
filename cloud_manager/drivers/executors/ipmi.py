from .base import MachineExecutor

__all__ = ['IpmiExecutor']


class IpmiExecutor(MachineExecutor):

    def poweron(self, host):
        self._power_cmd(host, cmd='on', expected_state='on')

    def poweroff(self, host):
        self._power_cmd(host, cmd='off', expected_state='off')
