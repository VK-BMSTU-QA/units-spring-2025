import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_strings(self):
        self.assertEqual(self.calculator.addition('abc', 'def'), 'abcdef')

    def test_add_different_types(self):
        self.assertRaises(TypeError, self.calculator.addition, 'abc', 1)
    
    def test_add_complex(self):
        self.assertEqual(self.calculator.addition(1 + 2j, 3 - 4j), 4 - 2j)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_strings(self):
        self.assertEqual(self.calculator.multiplication('a', 5), 'aaaaa')
    
    def test_multiplication_complex(self):
        self.assertEqual(self.calculator.multiplication(1 + 2j, 3 - 4j), 11 + 2j)

    def test_multiplication_incorrect_types(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'b')

    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
    
    def test_substraction_complex(self):
        self.assertEqual(self.calculator.subtraction(3 + 4j, 1 + 2j), 2 + 2j)

    def test_substraction_incorrect_types(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'a', 'b')

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_division_complex(self):
        self.assertEqual(self.calculator.division(11 + 2j, 1 + 2j), 3 - 4j)

    def test_division_incorrect_types(self):
        self.assertRaises(TypeError, self.calculator.division, 'a', 'b')

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-9), 9)
        self.assertEqual(self.calculator.absolute(9), 9)
    
    def test_absolute_incorrect_type(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'a')

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(2, -2), 0.25)
        self.assertEqual(self.calculator.degree(16, 0.25), 2)

    def test_degree_less_zero(self):
        self.assertAlmostEqual(self.calculator.degree(-1, 0.5), 1j)
    
    def test_degree_complex(self):
        self.assertEqual(self.calculator.degree((2 + 1j), 2), 3 + 4j)
    
    def test_degree_incorrect_types(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'b')

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_less_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_complex(self):
        self.assertRaises(TypeError, self.calculator, 1 + 2j)

    def test_ln_incorrect_type(self):
        self.assertRaises(TypeError, self.calculator.ln, 'a')

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertRaises(ValueError, self.calculator.log, -1, 10)

    def test_log_complex(self):
        self.assertRaises(TypeError, self.calculator.log, 1 + 2j, 2)

    def test_log_incorrect_types(self):
        self.assertRaises(TypeError, self.calculator.log, 'a', 'b')

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)

    def test_sqrt_complex(self):
        self.assertEqual(self.calculator.sqrt(3 + 4j), 2 + 1j)

    def test_sqrt_incorrect_type(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(2, 0.5), 4)
        self.assertEqual(self.calculator.nth_root(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(-8, 3), 1 + 1.7320508j)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 2, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 0, -2)

    def test_nth_root_complex(self):
        self.assertAlmostEqual(self.calculator.nth_root(2 - 11j, 3), 2 - 1j)

    def test_nth_root_incorrect_types(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 'b')
    
    def test_too_many_args(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.multiplication, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.division, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.absolute, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.degree, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.ln, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.log, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.sqrt, 1, 1, 1)
        self.assertRaises(TypeError, self.calculator.nth_root, 1, 1, 1)


if __name__ == "__main__":
    unittest.main()
