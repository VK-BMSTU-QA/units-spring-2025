import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 2), 4)
        self.assertEqual(self.calculator.multiplication(5, 5), 25)
        self.assertEqual(self.calculator.multiplication(-1, 5), -5)
        self.assertEqual(self.calculator.multiplication(0, 5), 0)
        self.assertEqual(self.calculator.multiplication(2, 5.0), 10.0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(5, 5), 0)
        self.assertEqual(self.calculator.subtraction(-1, 5), -6)
        self.assertEqual(self.calculator.subtraction(0, 5), -5)
        self.assertEqual(self.calculator.subtraction(2, 5.0), -3.0)

    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.division(9, 3), 3)
        self.assertEqual(self.calculator.division(-6, 3), -2)
        self.assertEqual(self.calculator.division(5, 2), 2.5)
        self.assertEqual(self.calculator.division(5, 0), None) 

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(-0), 0)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(3, 2), 9)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertEqual(self.calculator.degree(0, 5), 0)
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(1), 0)
        with self.assertRaises(ValueError):
            self.calculator.ln(0) 

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3)
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)
        self.assertAlmostEqual(self.calculator.log(81, 3), 4)
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)  
        with self.assertRaises(ValueError):
            self.calculator.log(10, 1) 

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.sqrt(0), 0)
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-1) 

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
        self.assertEqual(self.calculator.nth_root(81, 2), 9)
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        with self.assertRaises(ValueError):
            self.calculator.nth_root(-16, 2) 
        with self.assertRaises(ValueError):
            self.calculator.nth_root(16, 0)


if __name__ == "__main__":
    unittest.main()
