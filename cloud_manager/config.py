import attrdict
import yaml


class Configurable(object):

    def __init__(self, config):
        self._config = config


class Config(object):

    devstack = {
        'services': {
            'keystone': {'id': 'apache2',
                         'type': 'linux'}
        }
    }

    mcp = {
        'services': {
            'keystone': {'id': 'keystone',
                         'type': 'salt'}
        }
    }

    mos = {
        'services': {
            'keystone': {'id': 'apache2',
                         'type': 'linux'}
        }
    }

    @classmethod
    def from_file(cls, config_path):
        with open(config_path) as config_file:
            config = yaml.safe_load(config_file.read())
        return cls._merge_with_default(config)

    @classmethod
    def _merge_with_default(cls, config):
        default = {'devstack': cls.devstack,
                   'mcp': cls.mcp,
                   'mos': cls.mos}[config['cloud']['type']]
        return attrdict.merge.merge(default, config)
