import yaml
import latest.core


def render(template, datafile):
    with open(template, 'r') as f:
        doc = f.read()
    with open(datafile, 'r') as f:
        data = yaml.load(f)
    return latest.core.Doc(doc).bind(data)
