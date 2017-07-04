import os
import sys
import configparser
import re
import functools
import yaml
import copy
import argparse
from functools import *

from latest.util import *



class Expr(object):


    def __init__(self, expr):
        self.parse(expr)


    def get(self):
        return self.__expr


    def parse(self, expr):
        self.__expr = expr


    def bind(self, glob, loc):
        result = self.__expr
        for m in re.finditer(python_regex(), self.get()):
            to_repl = re.escape(m.group())
            g, l = globals(), locals()
            g.update(copy.deepcopy(glob))
            l.update(copy.deepcopy(loc))
            repl_with = str(eval(m.group(1), g, l))
            result = re.sub(to_repl, repl_with, result)
        return repr(result)[1:-1]


    expr = property(get, parse)



class Block(object):


    def __init__(self, block):
        self.parse(block)


    def get(self):
        return self.__block['code']


    def parse(self, block):
        self.__block = {'code': block.strip(block_wrapper())}
        parts = self.get().split(namespace_operator())
        self.__block['namespace'] = namespace_operator().join(parts[:-1])
        self.__block['expr'] = Expr(parts[-1])


    def namespace(self):
        return self.__block['namespace']


    def expr(self):
        return self.__block['expr']


    def bind(self, data):
        glob = data
        loc = select(data, self.namespace(), namespace_operator())
        return '\n'.join(self.expr().bind(glob, l) for l in loc)


    block = property(get, parse)



class Doc(object):


    def __init__(self, doc):
        self.parse(doc)


    def get(self):
        return self.__doc['code']


    def parse(self, doc):
        self.__doc = {'code': doc, 'blocks': []}
        for m in re.finditer(block_regex(), doc):
            self.__doc['blocks'].append(Block(m.group()))


    def bind(self, data):
        result = self.get()
        for m in re.finditer(block_regex(), self.get()):
            to_repl = re.escape(m.group())
            repl_with = Block(m.group()).bind(data)
            result = re.sub(to_repl, repl_with, result)
        return result


    doc = property(get, parse)



class LatestError(Exception):
    pass



class ParserError(LatestError):
    pass



class BindingError(LatestError):
    pass

