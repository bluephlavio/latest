import os.path
import pytest

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


@pytest.fixture(scope = 'session', params=[
    ('data.yaml', 'yaml'),
    ('data.yml', 'yml'),
    ('data.json', 'json'),
    ('data.txt', config(config_file(res_dir())).default_data_fmt),
    ('data', config(config_file(res_dir())).default_data_fmt),
])
def data_file(request, config, res_dir):
    return (os.path.join(res_dir, request.param[0]), request.param[1])



