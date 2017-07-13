import argparse
import os

from .util import path
from .config import _Config
from .config import config as Config
from .shortcuts import render


def main():

    args = parse_args()

    config = get_config(args.config)
    template = get_template(args.template)
    datafile = get_datafile(args.datafile)
    outfile = get_outfile(args.outfile)

    out = render(template, datafile, config=config)

    write(out, outfile)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('template')
    parser.add_argument('datafile')
    parser.add_argument('--outfile', '-o')
    parser.add_argument('--config', '-c')
    return parser.parse_args()


def get_config(filename):
    if filename:
        return _Config(config_file=path(filename))
    return Config


def get_template(filename):
    template = path(filename)
    if not os.path.isfile(template):
        raise FileNotFoundError
    return template


def get_datafile(filename):
    datafile = path(filename)
    if not os.path.isfile(datafile):
        raise FileNotFoundError
    return datafile


def get_outfile(filename):
    if filename:
        return path(filename)
    else:
        return None


def write(content, filename):
    if filename:
        with open(filename, 'w') as f:
            f.write(content)
    else:
        print(content)


