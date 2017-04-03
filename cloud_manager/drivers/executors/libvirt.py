from .base import MachineExecutor


class LibvirtExecutor(MachineExecutor):

    def poweron(self, host):
        self._find_domain(host).create()

    def poweroff(self, host):
        self._find_domain(host).destroy()
