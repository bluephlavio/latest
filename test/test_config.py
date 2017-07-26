import os.path

try:
    import configparser
except:
    import ConfigParser as configparser

import pytest

from latest.util import path


def test_config(config):
    assert config.templates_dir == '~/.latest/templates/'
    assert config.cmd_entry == r'\{\$'
    assert config.cmd_exit == r'\$\}'
    assert config.cmd_regex == r'\{\$(?P<code>.*?)\$\}'
    assert config.env_entry == r'<<<'
    assert config.env_exit == r'>>>'
    assert config.env_regex == r'<<<(?P<expr>[\s\S]*?)>>>'
    assert config.ns_operator == r'::'


def test_non_existing_config(non_existing_config):
    assert non_existing_config.cmd_entry == r'\\latest(\[(?P<ns>.*?)\])?\{\$'
