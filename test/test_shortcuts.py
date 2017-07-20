import os.path
import pytest

from latest.shortcuts import *


@pytest.fixture
def template_file(res_dir):
    return os.path.join(res_dir, 'example.tmpl')


@pytest.fixture(params=[
    ('example.yaml', 'yml'),
    ('example.json', 'json'),
])
def data_file(request, res_dir):
    return (os.path.join(res_dir, request.param[0]), request.param[1])


@pytest.fixture
def expected(res_dir):
    expected_file = os.path.join(res_dir, 'example.tex')
    with open(expected_file, 'r') as f:
        return f.read()


def test_render(template_file, data_file, expected):
    (data, format) = data_file
    if format in ('yaml', 'yml'):
        try:
            import yaml
        except:
            return
    assert render(template_file, data, format=format) == expected


