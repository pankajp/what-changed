# Standard library.
from os.path import abspath, join, dirname
import unittest

# Local imports.
from whatchanged.parser import parse
from whatchanged.tree import Package

HERE = abspath(dirname(__file__))

class TestNode(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_create_package(self):
        # Given
        path = join(HERE, 'data_v1', 'sample')

        # When
        package = parse(path)

        # Then
        self.assertEqual(package.name, 'sample')
        self.assertEqual(package.path, path)

    def test_should_create_children_from_package(self):
        # Given
        path = join(HERE, 'data_v1', 'sample')

        # When
        package = parse(path)

        # Then
        self.assertGreater(len(package.children), 0)
        self.assertIsInstance(package.find_child_by_name('bar'), Package)


if __name__ == "__main__":
    unittest.main()