# Standard library.
from os.path import isdir

# Local imports.
from whatchanged.tree import Package

def parse(path):
    if isdir(path):
        return Package(path=path)