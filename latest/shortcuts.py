import yaml

from .config import config as Config
from .core import eval_template


def render(template_filename, data_filename, config=Config):
    with open(template_filename, 'r') as f:
        template = f.read()
    with open(data_filename, 'r') as f:
        context = yaml.load(f)
    return eval_template(template, context, config=config)


