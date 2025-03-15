import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition_positive_and_negative_values(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertAlmostEqual(self.calculator.addition(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calculator.addition(-1.5, -2.5), -4.0)
        self.assertAlmostEqual(self.calculator.addition(1.5, -2.5), -1.0)

    def test_addition_zero_value(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(5, 0), 5)
        self.assertEqual(self.calculator.addition(0, 5), 5)

    def test_addition_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(None, 2)
        with self.assertRaises(TypeError):
            self.calculator.addition(2, None)

    def test_addition_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.addition(float('nan'), 2)))
        self.assertTrue(math.isnan(self.calculator.addition(2, float('nan'))))

    def test_addition_inf_input(self):
        self.assertEqual(self.calculator.addition(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.addition(2, float('inf')), float('inf'))

    def test_addition_negative_inf_input(self):
        self.assertEqual(self.calculator.addition(float('-inf'), 2), float('-inf'))
        self.assertEqual(self.calculator.addition(2, float('-inf')), float('-inf'))

    def test_addition_complex_input(self):
        self.assertEqual(self.calculator.addition(2 + 3j, 2), 4 + 3j)
        self.assertEqual(self.calculator.addition(2, 3 + 2j), 5 + 2j)

    def test_addition_array_input(self):
        with self.assertRaises(TypeError):
            self.calculator.addition([2, 3], 2)
        with self.assertRaises(TypeError):
            self.calculator.addition(2, [2, 3])

    def test_addition_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.addition("5", 3)
        with self.assertRaises(TypeError):
            self.calculator.addition(5, "3")

    def test_multiplication_positive_and_negative_values(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)
        self.assertAlmostEqual(self.calculator.multiplication(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calculator.multiplication(-2.5, -4), 10.0)
        self.assertAlmostEqual(self.calculator.multiplication(2.5, -4), -10.0)

    def test_multiplication_zero_value(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(5, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 5), 0)

    def test_multiplication_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, 2)
        with self.assertRaises(TypeError):
            self.calculator.multiplication(2, None)

    def test_multiplication_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(float('nan'), 2)))
        self.assertTrue(math.isnan(self.calculator.multiplication(2, float('nan'))))

    def test_multiplication_inf_input(self):
        self.assertEqual(self.calculator.multiplication(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.multiplication(2, float('inf')), float('inf'))

    def test_multiplication_negative_inf_input(self):
        self.assertEqual(self.calculator.multiplication(float('-inf'), 2), float('-inf'))
        self.assertEqual(self.calculator.multiplication(2, float('-inf')), float('-inf'))

    def test_multiplication_complex_input(self):
        self.assertEqual(self.calculator.multiplication(2 + 3j, 2), 4 + 6j)
        self.assertEqual(self.calculator.multiplication(2, 3 + 2j), 6 + 4j)

    def test_multiplication_array_input(self):
        self.assertEqual(self.calculator.multiplication([2], 3), [2, 2, 2])
        self.assertEqual(self.calculator.multiplication([2, 3], 2), [2, 3, 2, 3])


    def test_multiplication_string_input(self):
        self.assertEqual(self.calculator.multiplication("3", 2), "33")
        with self.assertRaises(TypeError):
            self.calculator.multiplication("5", "3")

    def test_subtraction_positive_and_negative_values(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertEqual(self.calculator.subtraction(3, 5), -2)
        self.assertAlmostEqual(self.calculator.subtraction(2.5, 1.5), 1.0)
        self.assertAlmostEqual(self.calculator.subtraction(-2.5, -1.5), -1.0)
        self.assertAlmostEqual(self.calculator.subtraction(2.5, -1.5), 4.0)

    def test_subtraction_zero_value(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(5, 0), 5)
        self.assertEqual(self.calculator.subtraction(0, 5), -5)

    def test_subtraction_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, 2)
        with self.assertRaises(TypeError):
            self.calculator.subtraction(2, None)

    def test_subtraction_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float('nan'), 2)))
        self.assertTrue(math.isnan(self.calculator.subtraction(2, float('nan'))))

    def test_subtraction_inf_input(self):
        self.assertEqual(self.calculator.subtraction(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.subtraction(2, float('inf')), float('-inf'))

    def test_subtraction_negative_inf_input(self):
        self.assertEqual(self.calculator.subtraction(float('-inf'), 2), float('-inf'))
        self.assertEqual(self.calculator.subtraction(2, float('-inf')), float('inf'))

    def test_subtraction_complex_input(self):
        self.assertEqual(self.calculator.subtraction(2 + 3j, 2), 3j)
        self.assertEqual(self.calculator.subtraction(2, 3 + 2j), -1 - 2j)

    def test_subtraction_array_input(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction([2, 3], 2)
        with self.assertRaises(TypeError):
            self.calculator.subtraction(2, [2, 3])

    def test_subtraction_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction("5", 3)
        with self.assertRaises(TypeError):
            self.calculator.subtraction(5, "3")

    def test_division_positive_and_negative_values(self):
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(7, 2), 3.5)
        self.assertEqual(self.calculator.division(-9, 3), -3)
        self.assertEqual(self.calculator.division(0, 5), 0)
        self.assertAlmostEqual(self.calculator.division(-7.5, 2.5), -3.0)
        self.assertAlmostEqual(self.calculator.division(7.5, -2.5), -3.0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))
        self.assertIsNone(self.calculator.division(0, 0))

    def test_division_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.division(None, 2)
        with self.assertRaises(TypeError):
            self.calculator.division(2, None)

    def test_division_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.division(float('nan'), 2)))
        self.assertTrue(math.isnan(self.calculator.division(2, float('nan'))))

    def test_division_inf_input(self):
        self.assertEqual(self.calculator.division(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.division(2, float('inf')), 0)

    def test_division_negative_inf_input(self):
        self.assertEqual(self.calculator.division(float('-inf'), 2), float('-inf'))
        self.assertEqual(self.calculator.division(2, float('-inf')), 0)

    def test_division_complex_input(self):
        self.assertEqual(self.calculator.division(2 + 3j, 2), 1 + 1.5j)
        self.assertEqual(self.calculator.division(2, 3 + 2j), 0.46153846153846156 - 0.3076923076923077j)

    def test_division_array_input(self):
        with self.assertRaises(TypeError):
            self.calculator.division([2, 3], 2)
        with self.assertRaises(TypeError):
            self.calculator.division(2, [2, 3])

    def test_division_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.division("6", 3)
        with self.assertRaises(TypeError):
            self.calculator.division(6, "3")

    def test_absolute_positive_and_negative_values(self):
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertAlmostEqual(self.calculator.absolute(-5.7), 5.7)
        self.assertAlmostEqual(self.calculator.absolute(5.7), 5.7)

    def test_absolute_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute(None)

    def test_absolute_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.absolute(float('nan'))))

    def test_absolute_inf_input(self):
        self.assertEqual(self.calculator.absolute(float('inf')), float('inf'))

    def test_absolute_negative_inf_input(self):
        self.assertEqual(self.calculator.absolute(float('-inf')), float('inf'))

    def test_absolute_array_input(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute([5, -5])

    def test_absolute_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute("-5")

    def test_degree_positive_values(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2)
        self.assertAlmostEqual(self.calculator.degree(-4.2, 2), 17.64)
        self.assertAlmostEqual(self.calculator.degree(4.2, -2), 1 / 17.64)

    def test_degree_zero_base(self):
        self.assertEqual(self.calculator.degree(0, 3), 0)
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_zero_negative_exponent(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.degree(0, -1)

    def test_degree_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(None, 3)
        with self.assertRaises(TypeError):
            self.calculator.degree(2, None)

    def test_degree_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.degree(float('nan'), 3)))
        self.assertTrue(math.isnan(self.calculator.degree(2, float('nan'))))

    def test_degree_inf_input(self):
        self.assertEqual(self.calculator.degree(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.degree(2, float('inf')), float('inf'))

    def test_degree_negative_inf_input(self):
        self.assertEqual(self.calculator.degree(float('-inf'), 2), float('inf'))
        self.assertEqual(self.calculator.degree(float('-inf'), 3), float('-inf'))
        self.assertEqual(self.calculator.degree(2, float('-inf')), 0)

    def test_degree_array_input(self):
        with self.assertRaises(TypeError):
            self.calculator.degree([2, 3], 2)
        with self.assertRaises(TypeError):
            self.calculator.degree(2, [2, 3])

    def test_degree_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.degree("2", 3)
        with self.assertRaises(TypeError):
            self.calculator.degree(2, "3")

    def test_ln_positive_values(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(2), math.log(2))

    def test_ln_negative_value(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_ln_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.ln(None)

    def test_ln_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.ln(float('nan'))))

    def test_ln_inf_input(self):
        self.assertEqual(self.calculator.ln(float('inf')), float('inf'))

    def test_ln_negative_inf_input(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(float('-inf'))

    # **Обычные случаи**
    def test_log_positive_values(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(27, 3), 3)

    # **log(1) по любому основанию**
    def test_log_one_any_base(self):
        self.assertEqual(self.calculator.log(1, 2), 0)
        self.assertEqual(self.calculator.log(1, 10), 0)
        self.assertEqual(self.calculator.log(1, math.e), 0)

    # **Отрицательное число**
    def test_log_negative_value(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_log_negative_base(self):
        with self.assertRaises(ValueError):
            self.calculator.log(8, -2)

    def test_log_base_equal_one(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(8, 1)

    def test_log_zero_value(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 2)

    def test_log_zero_base(self):
        with self.assertRaises(ValueError):
            self.calculator.log(8, 0)

    def test_log_fractional_values(self):
        self.assertAlmostEqual(self.calculator.log(0.25, 2), -2)
        self.assertAlmostEqual(self.calculator.log(2.25, 1.5), 2.0)

    def test_log_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.log(None, 2)
        with self.assertRaises(TypeError):
            self.calculator.log(8, None)

    def test_log_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.log(float('nan'), 2)))
        self.assertTrue(math.isnan(self.calculator.log(8, float('nan'))))

    def test_log_inf_input(self):
        self.assertEqual(self.calculator.log(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.log(8, float('inf')), 0)

    def test_log_negative_inf_input(self):
        with self.assertRaises(ValueError):
            self.calculator.log(float('-inf'), 2)
        with self.assertRaises(ValueError):
            self.calculator.log(8, float('-inf'))

    def test_log_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.log("8", 2)
        with self.assertRaises(TypeError):
            self.calculator.log(8, "2")

    def test_sqrt_positive_roots(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2))

    def test_sqrt_fractional_roots(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.25), 1.5)
        self.assertAlmostEqual(self.calculator.sqrt(0.49), 0.7)

    def test_sqrt_negative_roots(self):
        result = self.calculator.sqrt(-9)
        self.assertAlmostEqual(result.real, 0)
        self.assertAlmostEqual(result.imag, 3)

    def test_sqrt_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)

    def test_sqrt_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(float('nan'))))

    def test_sqrt_inf_input(self):
        self.assertEqual(self.calculator.sqrt(float('inf')), float('inf'))

    def test_sqrt_negative_inf_input(self):
        result = self.calculator.sqrt(float('-inf'))
        self.assertTrue(math.isinf(result))

    def test_sqrt_string_input(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt("9")

    def test_nth_root_positive_roots(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
        self.assertEqual(self.calculator.nth_root(2, 2), math.sqrt(2))
        self.assertEqual(self.calculator.nth_root(8.0, 3), 2.0)

    def test_nth_root_negative_roots(self):
        result = self.calculator.nth_root(-8.0, 2)
        self.assertAlmostEqual(result.real, 1.7319121124709868e-16)
        self.assertAlmostEqual(result.imag, 2.8284271247461903)

    def test_nth_root_none_input(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root(None, 3)
        with self.assertRaises(TypeError):
            self.calculator.nth_root(27, None)

    def test_nth_root_nan_input(self):
        self.assertTrue(math.isnan(self.calculator.nth_root(float('nan'), 3)))
        self.assertTrue(math.isnan(self.calculator.nth_root(27, float('nan'))))

    def test_nth_root_inf_input(self):
        self.assertEqual(self.calculator.nth_root(float('inf'), 3), float('inf'))
        self.assertEqual(self.calculator.nth_root(27, float('inf')), 1)

    def test_nth_root_negative_degree(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, -3), 1 / 3)

    def test_nth_root_zero_degree(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(27, 0)

if __name__ == "__main__":
    unittest.main()
