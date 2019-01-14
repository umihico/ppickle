__all__ = ['dump', 'load']

import codecs
import ast
from pprint import pformat


def dump(filename, data):
    """
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(pformat(data))
    """
    stringed_data = pformat(data)
    try:
        ast.literal_eval(stringed_data)
    except Exception as e:
        raise Exception("given data is not evaluable by ast.literal_eval")
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(stringed_data)


def load(filename):
    """
    with codecs.open(filename, 'r', 'utf-8') as f:
        return ast.literal_eval(f.read())
    """
    with codecs.open(filename, 'r', 'utf-8') as f:
        return ast.literal_eval(f.read())
