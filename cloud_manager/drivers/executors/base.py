import abc

from cloud_manager.config import Configurable

__all__ = ['CommandExecutor', 'MachineExecutor']


class CommandExecutor(Configurable):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass


class MachineExecutor(Configurable):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def poweroff(self):
        pass

    @abc.abstractmethod
    def poweron(self):
        pass

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def shutdown(self):
        pass

    @abc.abstractmethod
    def snapshot(self):
        pass

    @abc.abstractmethod
    def revert(self):
        pass
