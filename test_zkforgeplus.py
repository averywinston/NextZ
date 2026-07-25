# test_zkforgeplus.py
"""
Tests for ZKForgePlus module.
"""

import unittest
from zkforgeplus import ZKForgePlus

class TestZKForgePlus(unittest.TestCase):
    """Test cases for ZKForgePlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKForgePlus()
        self.assertIsInstance(instance, ZKForgePlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKForgePlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
