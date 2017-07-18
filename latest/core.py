import re

from .util import select
from .config import config as Config
from .exceptions import *


def eval_code(code, ctx, config=Config):
    try:
        result = eval(code, ctx)
        return str(result)
    except SyntaxError:
        raise CodeError
    except NameError:
        raise ContextError


def eval_expr(expr, ctx, config=Config):
    frags = re.split(config.code_regex, expr)
    return str().join(map(lambda i, s: eval_code(s, ctx) if i % 2 == 1 else s, range(len(frags)), frags))


def eval_block(block, ctx, config=Config):
    m = re.match(config.inner_block_regex, block)
    if m:
        ns = m.group(config._NS_TAG)
        expr = m.group(config._EXPR_TAG)
        ctx = select(ctx, ns, sep=config.ns_operator)
        return eval_expr(expr, ctx)
    else:
        return eval_expr(block, ctx)


def eval_template(template, ctx, config=Config):
    """Evaluate a template with a context dictionary.

    Args:
        template (str): the template.

    Returns:
        str: the evaluated document.

    """
    frags = re.split(config.outer_block_regex, template)
    return str().join(map(lambda i, s: eval_block(s, ctx) if i % 2 == 1 else s, range(len(frags)), frags))



