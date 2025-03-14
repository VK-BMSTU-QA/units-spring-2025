import unittest
from src.calculator import Calculator
import math

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(-11, 2), -22)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(11, 2), 9)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 2), 5.0)
    
    def test_absolute_otr(self):
        self.assertEqual(self.calculator.absolute(-10), 10)

    def test_absolute_polo(self):
        self.assertEqual(self.calculator.absolute(11), 11)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(11,2), 121)

    def test_ln_zero(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_classic(self):
        self.assertEqual(self.calculator.ln(10), math.log(10))

    def test_log(self):
        self.assertEqual(self.calculator.log(121, 11), 2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(100), 10.0)
    
    def test_nth_root(self):
            self.assertEqual(self.calculator.nth_root(100, 2), 10.0)

if __name__ == "__main__":
    unittest.main()
