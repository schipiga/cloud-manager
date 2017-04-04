from .base import MachineExecutor

__all__ = ['LibvirtExecutor']


class LibvirtExecutor(MachineExecutor):

    def poweron(self, host):
        self._find_domain(host).create()

    def poweroff(self, host):
        self._find_domain(host).destroy()
