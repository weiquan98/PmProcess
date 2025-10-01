# test_pm2process.py
"""
Tests for Pm2Process module.
"""

import unittest
from pm2process import Pm2Process

class TestPm2Process(unittest.TestCase):
    """Test cases for Pm2Process class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Pm2Process()
        self.assertIsInstance(instance, Pm2Process)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Pm2Process()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
