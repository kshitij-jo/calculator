#!/usr/bin/env python

import unittest
from calculator import multiply

class TestMultiplyFunction(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(100, 0), 0)

if __name__ == '__main__':
    unittest.main()
