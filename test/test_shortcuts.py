import os.path
import pytest

from latest.shortcuts import *


@pytest.fixture
def template_file(res_dir):
    return os.path.join(res_dir, 'example.tmpl')


@pytest.fixture
def data_file(res_dir):
    return os.path.join(res_dir, 'example.yaml')


@pytest.fixture
def output_file(res_dir):
    expected_file = os.path.join(res_dir, 'example.tex')
    with open(expected_file, 'r') as f:
        return f.read()


def test_render(template_file, data_file, output_file):
    assert render(template_file, data_file) == output_file
