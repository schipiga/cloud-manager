from cloud_manager.config import Configurable


class CommandExecutor(Configurable):

    def execute(self):
        pass


class MachineExecutor(Configurable):

    def poweroff(self):
        pass

    def poweron(self):
        pass

    def reset(self):
        pass

    def shutdown(self):
        pass

    def snapshot(self):
        pass

    def revert(self):
        pass
