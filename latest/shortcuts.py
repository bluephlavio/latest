""":mod:`shortcuts` module contains shortcut functions built upon core functionality of :mod:`latest` package.


"""

import yaml
import json

from .config import config as Config
from .exceptions import FormatNotSupportedError
from .core import eval_template


def render(template_filename, data_filename, format=json, config=Config):
    """Render a template in a file within a context defined by a yaml data file.

    Args:
        template_filename (str): the path of the template file.
        data_filename (str): the path of the data .yaml file.
        format (str): format of data file.
        config (config._Config): configuration object.

    Returns:
        str: the output of the evaluation process as defined by :mod:`latest` core functions.

    """
    with open(template_filename, 'r') as f:
        template = f.read()
    with open(data_filename, 'r') as f:
        if format == 'json':
            context = json.load(f.read())
        elif format == 'yaml':
            context = yaml.load(f)
        else:
            raise FormatNotSupportedError
    return eval_template(template, context, config=config)




