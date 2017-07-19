""":mod:`main` module defines the main :mod:`latest` command line script.


"""

import argparse
import os

from .util import path
from .config import create_config
from .config import config as Config
from .shortcuts import render


def main():
    args = parse_args()
    output = process(args)
    write(output, args)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('template')
    parser.add_argument('data')
    parser.add_argument('--config', '-c')
    parser.add_argument('--output', '-o')
    return parser.parse_args()


def process(args):

    config = create_config(args.config) if args.config else Config
    return render(args.template, args.data, config=config)


def write(output, args):
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)


