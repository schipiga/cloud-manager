from .base import CommandExecutor

__all__ = ['AnsibleExecutor']


class AnsibleExecutor(CommandExecutor):

    def execute(self, cmd, hosts):
        task = {'hosts': hosts, 'tasks': [{'shell': cmd}]}
        result = self.run_playbook(task)
        return result
