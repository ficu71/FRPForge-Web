import sys
import os
import unittest

# Dodaj katalog backend/ do sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

if __name__ == '__main__':
    # Odkryj i uruchom wszystkie testy w katalogu tests/
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
