# Standard library.
from os.path import isdir

# Local imports.
from whatchanged.tree import Package, Module


def parse(path):
    if isdir(path):
        return Package(path=path)
    elif path.endswith('.py'):
        return Module(path=path)
