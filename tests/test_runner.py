# tests/test_runner.py
import unittest

# Discover and load all test cases from the 'tests' directory
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
