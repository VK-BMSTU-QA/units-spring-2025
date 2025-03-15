import unittest
from calculator import Calculator
import math
import cmath  # Модуль для работы с комплексными числами


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    
    # Тесты для сложения
    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)
    
    def test_add_fractional(self):
        self.assertAlmostEqual(self.calculator.addition(0.1, 0.2), 0.3)

    def test_add_large_numbers(self):
        self.assertEqual(self.calculator.addition(10**18, 10**18), 2 * 10**18)

    def test_add_complex_numbers(self):
        self.assertEqual(self.calculator.addition(1 + 2j, 3 + 4j), (4 + 6j))

    
    # Тесты для умножения
    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calculator.multiplication(5, 0), 0)

    def test_multiply_fractional(self):
        self.assertAlmostEqual(self.calculator.multiplication(0.5, 0.5), 0.25)

    def test_multiply_large_numbers(self):
        self.assertEqual(self.calculator.multiplication(10**9, 10**9), 10**18)

    def test_multiply_complex_numbers(self):
        self.assertEqual(self.calculator.multiplication(1 + 2j, 3 + 4j), (-5 + 10j))

    
    # Тесты для вычитания
    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(10, 1), 9)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtract_fractional(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.3, 0.1), 0.2)

    def test_subtract_complex_numbers(self):
        self.assertEqual(self.calculator.subtraction(3 + 4j, 1 + 2j), (2 + 2j))

    
    # Тесты для деления
    def test_divide(self):
        self.assertEqual(self.calculator.division(2, 3), 2 / 3)

    def test_divide_by_negative(self):
        self.assertEqual(self.calculator.division(10, -2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.division(1, 0))

    def test_divide_complex_numbers(self):
        self.assertEqual(self.calculator.division(1 + 2j, 1 + 1j), (1.5 + 0.5j))

    
    # Тесты для абсолютного значения
    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-1), 1)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_complex_numbers(self):
        self.assertAlmostEqual(self.calculator.absolute(3 + 4j), 5)

    
    # Тесты для возведения в степень
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 5), 32)

    def test_degree_negative_power(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_degree_zero_power(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)
    
    def test_degree_fractional(self):
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_large_numbers(self):
        self.assertEqual(self.calculator.degree(2, 64), 2**64)

    def test_degree_complex_numbers(self):
        self.assertEqual(self.calculator.degree(1 + 1j, 2), 2j)

    
    # Тесты для натурального логарифма
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_non_positive(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    
    # Тесты для логарифма с произвольным основанием
    def test_log(self):
        self.assertEqual(self.calculator.log(4, 2), 2)

    def test_log_non_positive(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 2)
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(4, 1)
        with self.assertRaises(ValueError):
            self.calculator.log(4, -2)

    
    # Тесты для квадратного корня
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_small_number(self):
        self.assertAlmostEqual(self.calculator.sqrt(1e-10), 1e-5)

    def test_sqrt_complex_numbers(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    
    # Тесты для корня n-й степени
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(32, 5), 2)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 5), 0)

    def test_nth_root_fractional(self):
        self.assertAlmostEqual(self.calculator.nth_root(16, 0.5), 256)

    def test_nth_root_small_number(self):
        self.assertAlmostEqual(self.calculator.nth_root(1e-10, 2), 1e-5)

    def test_nth_root_complex_numbers(self):
        self.assertAlmostEqual(self.calculator.nth_root(-1, 2), 1j)


if __name__ == "__main__":
    unittest.main()
