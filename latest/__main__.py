import argparse
import os
import yaml
import latest

from latest.shortcuts import render
from latest.util import templates_dir


def main():

    args = parse_args()

    template = get_template(args.template)
    datafile = get_datafile(args.datafile)
    outfile = get_outfile(args.outfile)

    out = render(template, datafile)

    write(out, outfile)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('template')
    parser.add_argument('datafile')
    parser.add_argument('--outfile', '-o')
    return parser.parse_args()


def get_template(filename):
    template = os.path.abspath(filename)
    if not os.path.isfile(template):
        template = os.path.join(templates_dir(), filename)
    print(template)
    return template
    if not os.path.isfile(template):
        raise FileNotFoundError


def get_datafile(filename):
    datafile = os.path.abspath(filename)
    print(datafile)
    return datafile
    if not os.path.isfile(datafile):
        raise FileNotFoundError


def get_outfile(filename):
    outfile = filename
    if filename:
        outfile = os.path.abspath(filename)
    return outfile


def write(out, filename):
    if filename:
        with open(filename, 'w') as f:
            f.write(out)
    else:
        print(out)


