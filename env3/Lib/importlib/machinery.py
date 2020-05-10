"""The machinery of importlib: finders, loaders, hooks, etc."""

from ._bootstrap_external import (SOURCE_SUFFIXES, BYTECODE_SUFFIXES,
                                  EXTENSION_SUFFIXES)


def all_suffixes():
    """Returns a list of all recognized module suffixes for this process"""
    return SOURCE_SUFFIXES + BYTECODE_SUFFIXES + EXTENSION_SUFFIXES
