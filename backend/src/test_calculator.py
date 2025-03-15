import unittest
import math
from backend.src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calculator.addition(1.5, 2.3), 3.8, delta=1e-9)

    def test_add_infinity(self):
        inf = float('inf')
        self.assertTrue(math.isinf(self.calculator.addition(inf, 5)))
        self.assertTrue(math.isinf(self.calculator.addition(-inf, -5)))

    def test_add_negative(self):
        self.assertAlmostEqual(self.calculator.addition(-1, -3), -4)

    def test_add_nan(self):
        nan = float('nan')
        self.assertTrue(math.isnan(self.calculator.addition(nan, 5)))
        self.assertTrue(math.isnan(self.calculator.addition(5, nan)))
        self.assertTrue(math.isnan(self.calculator.addition(nan, nan)))

    def test_add_very_small_numbers(self):
        self.assertAlmostEqual(self.calculator.addition(1e-15, 2e-15), 3e-15, delta=1e-20)

    def test_add_very_large_numbers(self):
        large_num = 1e+308
        self.assertAlmostEqual(self.calculator.multiplication(large_num, 2), 2e+308, delta=1e+300)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.5, 2.0), 3.0, delta=1e-9)

    def test_multiply_infinity(self):
        inf = float('inf')
        self.assertTrue(math.isinf(self.calculator.multiplication(inf, 2)))
        self.assertTrue(math.isinf(self.calculator.multiplication(-inf, 2)))

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(3, 1), 2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calculator.subtraction(5.5, 2.2), 3.3, delta=1e-9)

    def test_subtract_infinity(self):
        inf = float('inf')
        self.assertTrue(math.isinf(self.calculator.subtraction(inf, 1000)))
        self.assertTrue(math.isinf(self.calculator.subtraction(-inf, -1000)))

    def test_subtract_nan(self):
        nan = float('nan')
        self.assertTrue(math.isnan(self.calculator.subtraction(nan, 5)))
        self.assertTrue(math.isnan(self.calculator.subtraction(5, nan)))
        self.assertTrue(math.isnan(self.calculator.subtraction(nan, nan)))

    def test_divide(self):
        self.assertEqual(self.calculator.division(3, 1), 3)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calculator.division(5.0, 2.0), 2.5, delta=1e-9)

    def test_divide_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))
        self.assertIsNone(self.calculator.division(0, 0))

    def test_divide_infinity(self):
        inf = float('inf')
        self.assertEqual(self.calculator.division(inf, 1), inf)
        self.assertEqual(self.calculator.division(-inf, -1), inf)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-3), 3)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(2), 2)

    def test_degree_positive(self):
        self.assertEqual(self.calculator.degree(2, 2), 4)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_degree_with_fractional_exponent(self):
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2.0, delta=1e-9)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_with_small_value(self):
        self.assertAlmostEqual(self.calculator.ln(1 + 1e-9), 1e-9, delta=1e-12)

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_log(self):
        self.assertEqual(self.calculator.log(3, 9), 0.5)

    def test_log_with_base_one(self):
        with self.assertRaises(ValueError):
            self.calculator.log(3, 1)

    def test_log_with_negative_base(self):
        with self.assertRaises(ValueError):
            self.calculator.log(3, -2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_with_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.0), math.sqrt(2), delta=1e-9)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-1)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)

    def test_nth_root_with_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(16.0, 4), 2.0, delta=1e-9)

    def test_nth_root_negative(self):
        self.assertEqual(self.calculator.nth_root(-27, 3), -3)  # Нечетный корень

    def test_nth_root_even_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.nth_root(-16, 4)  # Четный корень из отрицательного числа

if __name__ == "__main__":
    unittest.main()
