import os.path
import pytest

from latest.config import _Config


@pytest.fixture(scope='session')
def res_dir():
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'res' + os.path.sep)


@pytest.fixture(scope='session')
def config_file(res_dir):
    return os.path.abspath(os.path.join(res_dir, 'test.cfg'))


@pytest.fixture(scope='session')
def config(config_file):
    return _Config(config_file)


@pytest.fixture(scope='session')
def non_existing_config_file(res_dir):
    return os.path.abspath(os.path.join(res_dir, 'non_existing.cfg'))


@pytest.fixture(scope='session')
def non_existing_config(non_existing_config_file):
    return _Config(non_existing_config_file)


