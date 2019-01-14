__all__ = ['dump', 'load']

import codecs
import ast
from pprint import pformat


def dump(filename, data):
    """
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(pformat(data))
    """
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(pformat(data))


def load(filename):
    """
    with codecs.open(filename, 'r', 'utf-8') as f:
        return ast.literal_eval(f.read())
    """
    with codecs.open(filename, 'r', 'utf-8') as f:
        return ast.literal_eval(f.read())
