""":mod:`shortcuts` module contains shortcut functions built upon core functionality of :mod:`latest` package.


"""

import yaml

from .config import config as Config
from .core import eval_template


def render(template_filename, data_filename, config=Config):
    """Render a template in a file within a context defined by a yaml data file.

    Args:
        template_filename (str): the path of the template file.
        data_filename (str): the path of the data .yaml file.
        config (config._Config): configuration object.

    Returns:
        str: the output of the evaluation process as defined by :mod:`latest` core functions.

    """
    with open(template_filename, 'r') as f:
        template = f.read()
    with open(data_filename, 'r') as f:
        context = yaml.load(f)
    return eval_template(template, context, config=config)




