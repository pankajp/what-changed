# Standard library imports.
from os import listdir
from os.path import basename, isdir, join, splitext


class Node(object):

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def children(self):
        raise NotImplementedError

    def find_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

        return None

class Module(Node):

    def __init__(self, path):
        self.path = path
        self.name = splitext(basename(path))

class Package(Node):

    def __init__(self, path):
        self.path = path
        self.name = basename(path)

    @property
    def children(self):
        children = []
        for name in listdir(self.path):
            path = join(self.path, name)

            if isdir(path):
                children.append(Package(path=path))

            elif name.endswith('.py'):
                children.append(Module(path=path))

        return children
