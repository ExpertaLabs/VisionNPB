import unittest

from visionnpb.ksvisionlib import *

class TestSimple(unittest.TestCase):

    def test_verifyPythonLibAccessibility(self):
        self.assertIsNotNone(webAPIError(666))

if __name__ == '__main__':
    unittest.main()