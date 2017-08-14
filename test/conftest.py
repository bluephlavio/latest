import pytest
import os.path

from latest.config import create_config


@pytest.fixture(scope='session')
def res_dir():
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'res' + os.path.sep)


@pytest.fixture(scope='session')
def config_file(res_dir):
    return os.path.abspath(os.path.join(res_dir, 'config.cfg'))


@pytest.fixture(scope='session')
def config(config_file):
    return create_config(config_file)


@pytest.fixture(scope='session')
def non_existing_config_file(res_dir):
    return os.path.abspath(os.path.join(res_dir, 'non_existing.cfg'))


@pytest.fixture(scope='session')
def non_existing_config(non_existing_config_file):
    return create_config(non_existing_config_file)


@pytest.fixture(scope='session', params=[
    'data.yml',
    'data.json',
])
def data_file(request, res_dir):
    return os.path.join(res_dir, request.param)
