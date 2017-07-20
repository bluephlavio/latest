""":mod:`shortcuts` module contains shortcut functions built upon core functionality of :mod:`latest` package.


"""

import os.path
from os import linesep as ls
import json

from .config import config as Config
from .exceptions import FormatNotSupportedError
from .core import eval_template


def render(template_filename, data_filename, config=Config, format=None):
    """Render a template in a file within a context defined by a yaml data file.

    Args:
        template_filename (str): the path of the template file.
        data_filename (str): the path of the data .yaml file.
        format (str): format of data file; accepted: *json*, *yaml* (or *yml*).
        config (config._Config): configuration object.

    Returns:
        str: the output of the evaluation process as defined by :mod:`latest` core functions.

    """

    if format:
        data_format = format.lower()
    else:
        format_guess = os.path.splitext(data_filename)[-1].strip('.').lower()
        if format_guess in ('json', 'yaml', 'yml'):
            data_format = format_guess
        else:
            data_format = config.data_format.lower()

    with open(template_filename, 'r') as f:
        template = f.read()

    with open(data_filename, 'r') as f:
        if data_format in ('json',):
            try:
                context = json.load(f)
            except ValueError as e:
                raise ValueError('Error parsing json data file:' + ls + str(e))
        elif data_format in ('yaml', 'yml'):
            try:
                import yaml
                context = yaml.load(f)
            except ImportError as e:
                raise ImportError(str(e) + ls + 'You need to install pyyaml!' + ls + 'Try:' + ls + '   $ pip install pyyaml')
            except yaml.YAMLError as e:
                raise yaml.YAMLError('Error parsing yaml data file!' + ls + str(e))
        else:
            raise FormatNotSupportedError(data_format + ' format not supported!')

    return eval_template(template, context, config=config)



