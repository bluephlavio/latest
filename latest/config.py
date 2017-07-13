import os.path
import re

try:
    import configparser
except:
    import ConfigParser as configparser

import latest
from .util import path, getopt



class _Config(object):


    _CONFIG_DIR = path('~/.' + latest.__project__ + '/')
    _CONFIG_FILE = os.path.join(_CONFIG_DIR, latest.__project__ + 'cfg')
    _OPTIONS = (
        # section, key, default
        ('general', 'templates_dir', os.path.join(_CONFIG_DIR, 'templates/')),
        ('lang', 'code_entry', '$'),
        ('lang', 'code_exit', '$'),
        ('lang', 'ns_operator', '::'),
        ('lang', 'block_entry', '<<<'),
        ('lang', 'block_exit', '>>>'),
    )
    _CODE_TAG = 'code'
    _NS_TAG = 'ns'
    _EXPR_TAG = 'expr'
    _BLOCK_TAG = 'block'


    def __init__(self, config_file=_CONFIG_FILE):
        self.read(config_file)


    def read(self, config_file):
        self.config_file = path(config_file)
        self.config_dir = os.path.dirname(self.config_file)
        parser = configparser.RawConfigParser()
        parser.read(self.config_file)
        for section, key, default in self._OPTIONS:
            value = getopt(parser, section, key, default)
            setattr(self, key, value)


    @property
    def code_regex(self):
        return re.escape(self.code_entry) + r'(?P<code>.*?)' + re.escape(self.code_exit)


    @property
    def inner_block_regex(self):
        return r'(?P<ns>.*)' + re.escape(self.ns_operator) + '(?P<expr>.*)'


    @property
    def outer_block_regex(self):
        return re.escape(self.block_entry) + r'(?P<block>.*?)' + re.escape(self.block_exit)



config = _Config()


