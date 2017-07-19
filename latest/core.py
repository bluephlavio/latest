""":mod:`core` contains core functions for templating.


"""


import re

from .util import select
from .config import config as Config
from .exceptions import *


def eval_code(code, ctx, config=Config):
    """Parses and evaluates code converting output to a string.

    Args:
        code (str): the code to be evaluated.
        ctx (dict): the context to be evaluated in.
        config (config._Config): configuration object.

    Returns:
        str: the output converted to a string.

    Raises:
        :class:`CodeError`: raised if a :class:`SyntaxError` is raised by the builtin :func:`eval` function.
        :class:`ContextError`: raised when the context names do not match code names
            and a :class:`NameError` is raised by the builtin :func:`eval` function.

    """
    try:
        result = eval(code, ctx)
        return str(result)
    except SyntaxError:
        raise CodeError
    except NameError:
        raise ContextError


def eval_expr(expr, ctx, config=Config):
    """Evaluate a :mod:`latest` *expression*.

    An *expression* is a string of normal text with eventual code islands in between.
    The evaluation proceeds evaluating code islands and then concatenating the results with the fragments of plain text.

    Args:
        expr (str): the expression to be evaluated.
        ctx (dict): the context to be evaluated in.
        config (config._Config): configuration object.

    Returns:
        str: the output obtained concatenating the plain text fragments with the evaluation of code islands.

    """
    frags = re.split(config.code_regex, expr)
    return str().join(map(lambda i, s: eval_code(s, ctx, config=config) if i % 2 == 1 else s, range(len(frags)), frags))


def eval_block(block, ctx, config=Config):
    """Evaluate a :mod:`latest` *block*.

    A *block* is a special :mod:`latest` syntax formed by two parts:
        * the `namespace` (optional) that define the branch of the context dictionary in which the `expression` must be evaluated.
        * the `expression` to be evaluated.

    Args:
        block (str): the block to be evaluated.
        ctx (dict): the context to be evaluated in.
        config (config._Config): configuration object.

    Returns:
        str: the output obtained evaluating the `expression` within the `namespace`.

    """
    m = re.match(config.inner_block_regex, block)
    if m:
        ns = m.group(config._NS_TAG)
        expr = m.group(config._EXPR_TAG)
        ctx = select(ctx, ns, sep=config.ns_operator)
        return eval_expr(expr, ctx, config=config)
    else:
        return eval_expr(block, ctx, config=config)


def eval_template(template, ctx, config=Config):
    """Evaluates an entire template.

    Args:
        template (str): the template.
        ctx (dict): the context.
        config (config._Config): configuration object.

    Returns:
        str: the evaluated document.

    """
    frags = re.split(config.outer_block_regex, template)
    return str().join(map(lambda i, s: eval_block(s, ctx, config=config) if i % 2 == 1 else s, range(len(frags)), frags))



