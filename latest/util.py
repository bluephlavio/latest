import os, configparser, re

import latest


def path(loc):
    return os.path.abspath(os.path.expanduser(loc))


def config_dir():
    return path('~/.' + latest.APP + '/')


def templates_dir():
    return os.path.join(config_dir(), 'templates/')


def config_file():
    return os.path.join(config_dir(), latest.APP + '.cfg')


def config():
    parser = configparser.RawConfigParser(delimiters=('=',))
    parser.read(config_file())
    return parser


def getopt(section, key, default):
    try:
        parser = config()
        return parser[section][key]
    except configparser.Error:
        return default


def python_wrapper():
    return getopt('lang', 'python_wrapper', '$')


def block_wrapper():
    return getopt('lang', 'block_wrapper', '%')


def namespace_operator():
    return getopt('lang', 'namespace', ':')


def wrap(string, char):
    return char + string + char


def python_regex():
    return wrap('(.*?)', re.escape(python_wrapper()))


def block_regex():
    return wrap('(.*?)', re.escape(block_wrapper()))


def is_scalar(obj):
    return isinstance(obj, (str, int, float, long, bool))


def is_vector(obj):
    return isinstance(obj, (list, tuple))


def is_tensor(obj):
    return (not is_scalar(obj)) and (not is_vector(obj))


def select(data, path, sep='/'):
    out = data
    if path:
        for key in path.strip(sep).split(sep):
            if is_vector(out):
                out = [item[key] for item in out]
            else:
                out = out[key]
        if not is_vector(out):
            out = [out]
    else:
        out = [data]
    for i in range(len(out)):
        out[i]['_index'] = i
        out[i]['_value'] = out[i]
    return out


