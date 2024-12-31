"""
Test suite for calculator operations.

This module contains unit tests for the calculator programme,
verifying correct operation of arithmetic functions including
edge cases and error handling.

Usage:
    Run tests using: python -m unittest calculator_test.py
"""

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculatorOperations(unittest.TestCase):
    """
    Test cases for verifying calculator operations.
    
    Tests standard arithmetic operations, edge cases, and error conditions
    to ensure reliable calculator function.
    """
    
    def test_addition(self):
        """
        Test addition with various number combinations.
        Verifies correct handling of positive, negative, and decimal numbers.
        """
        self.assertEqual(add(3, 5), 8, "Integer addition failed")
        self.assertEqual(add(-1, 1), 0, "Addition with negative number failed")
        self.assertEqual(add(0.1, 0.2), 0.3, "Decimal addition failed")
        self.assertEqual(add(0, 0), 0, "Zero addition failed")
    
    def test_subtraction(self):
        """
        Test subtraction with various number combinations.
        Verifies correct handling of positive, negative, and decimal numbers.
        """
        self.assertEqual(subtract(5, 3), 2, "Integer subtraction failed")
        self.assertEqual(subtract(-1, -1), 0, "Negative number subtraction failed")
        self.assertEqual(subtract(0.3, 0.1), 0.2, "Decimal subtraction failed")
        self.assertEqual(subtract(0, 0), 0, "Zero subtraction failed")
    
    def test_multiplication(self):
        """
        Test multiplication with various number combinations.
        Verifies correct handling of positive, negative, and decimal numbers.
        """
        self.assertEqual(multiply(3, 5), 15, "Integer multiplication failed")
        self.assertEqual(multiply(-2, 3), -6, "Multiplication with negative failed")
        self.assertEqual(multiply(0.5, 2), 1.0, "Decimal multiplication failed")
        self.assertEqual(multiply(0, 5), 0, "Multiplication by zero failed")
    
    def test_division(self):
        """
        Test division with various number combinations.
        Verifies correct handling of positive, negative, decimal numbers,
        and division by zero errors.
        """
        self.assertEqual(divide(6, 2), 3, "Integer division failed")
        self.assertEqual(divide(-6, 2), -3, "Division with negative failed")
        self.assertEqual(divide(2.5, 2), 1.25, "Decimal division failed")
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
    
    def test_float_precision(self):
        """
        Test handling of floating-point precision.
        Verifies correct handling of decimal calculations.
        """
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(multiply(0.1, 0.3), 0.03, places=7)
    
    def test_type_handling(self):
        """
        Test handling of different numeric types.
        Verifies correct operation with integers and floats.
        """
        self.assertEqual(add(3, 2.0), 5.0, "Mixed type addition failed")
        self.assertEqual(multiply(2, 3.0), 6.0, "Mixed type multiplication failed")

if __name__ == '__main__':
    unittest.main(verbosity=2)