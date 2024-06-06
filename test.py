# test_calculations.py

import doctest
import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite('scenario_sale.rst'))
    return tests

# Your unittest goes here...

if __name__ == "__main__":
    unittest.main()