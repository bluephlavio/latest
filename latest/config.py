""":mod:`config` module contains configuration functions and classes for :mod:`latest` package.

:mod:`latest` is completely customizable even in its syntax.

Configuration file is found by default in `~/.latest/latest.cfg` but one can use his configuration objects/files.

The section `lang` of the configuration file is where one can define its own syntax.

Available options in `lang` section are:

    * `code_entry`
    * `code_exit`
    * `env_entry`
    * `env_exit`
    * `ns_operator`


"""

import os
import re

try:
    import configparser
except:
    import ConfigParser as configparser

import latest
from .util import path, getopt


_BASE_DIR = path('~/.' + latest.__project__ + '/')
_CONFIG_FILE = os.path.join(_BASE_DIR, latest.__project__ + 'cfg')
_TEMPLATES_DIR = os.path.join(_BASE_DIR, 'templates/')


class _Config(object):


    _OPTIONS = (
        # section, key, default
        ('general', 'templates_dir', _TEMPLATES_DIR),
        ('general', 'default_data_fmt', 'json'),
        ('general', 'join_items', str()),
        ('lang', 'cmd_entry', r'\\latest(\[(?P<ns>.*?)\])?\{\$'),
        ('lang', 'cmd_exit', r'\$\}'),
        ('lang', 'env_entry', r'\\begin\{latest\}(\[(?P<ns>.*?)\])?\s?'),
        ('lang', 'env_exit', r'\s?\\end\{latest\}'),
        ('lang', 'ns_operator', r'::'),
    )

    CMD_CONTENT_TAG = 'code'
    ENV_CONTENT_TAG = 'expr'
    NS_TAG = 'ns'


    def __init__(self, config_file=None):
        if config_file:
            self.read(config_file)
        else:
            self.set_defaults()


    def set_defaults(self):
        for section, key, default in self._OPTIONS:
            setattr(self, key, default)


    def read(self, filename):

        config_file = path(filename)
        if not hasattr(self, 'config_files'):
            self.config_files = list()
        self.config_files.append(config_file)

        parser = configparser.RawConfigParser()
        parser.read(config_file)
        for section, key, default in self._OPTIONS:
            value = getopt(parser, section, key, default)
            setattr(self, key, value)


    @property
    def cmd_regex(self):
        return self.cmd_entry + r'(?P<' + self.CMD_CONTENT_TAG + r'>.*?)' + self.cmd_exit


    @property
    def env_regex(self):
        return self.env_entry + r'(?P<' + self.ENV_CONTENT_TAG + r'>[\s\S]*?)' + self.env_exit



def create_config(config_file=None):
    return _Config(config_file)


config = _Config(config_file=_CONFIG_FILE)


