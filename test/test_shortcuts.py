import os.path
import pytest

from latest.shortcuts import *


@pytest.fixture
def template_file(res_dir):
    return os.path.join(res_dir, 'template.tmpl')


@pytest.fixture
def data_file(res_dir):
    return os.path.join(res_dir, 'data.yaml')


@pytest.fixture
def expected(res_dir):
    expected_file = os.path.join(res_dir, 'expected.txt')
    with open(expected_file, 'r') as f:
        return f.read()


def test_render(config, template_file, data_file, expected):
    assert render(template_file, data_file, config=config) == expected
