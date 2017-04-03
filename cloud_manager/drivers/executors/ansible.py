from .base import CommandExecutor


class AnsibleExecutor(CommandExecutor):

    def execute(self, cmd, hosts):
        task = {'hosts': hosts, 'tasks': [{'shell': cmd}]}
        result = self.run_playbook(task)
        return result
