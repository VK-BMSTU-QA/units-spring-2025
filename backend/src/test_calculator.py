import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(1, -1), 0)

    def test_add_string_and_int(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, "1")

    def test_add_bool_int(self):
        self.assertEqual(self.calculator.addition(1, True), 2)

    def test_add_float_bool(self):
        self.assertEqual(self.calculator.addition(1/3, False), 1/3)

    def test_add_list_bool(self):
        self.assertRaises(TypeError, self.calculator.addition,
                          [1, 2, 3, 4, 4], False)

    def test_add_string(self):
        self.assertEqual(self.calculator.addition("1", "1"), "11")

    def test_add_more_arguments(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, 1, 1, 1, 0)

    def test_add_complex(self):
        self.assertEqual(self.calculator.addition(1j, 1j), 2j)

    def test_multiplication_int(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(5, -5), -25)

    def test_multiplication_int_string(self):
        self.assertEqual(self.calculator.multiplication(2, "1"), "11")

    def test_multiplication_int_bool(self):
        self.assertEqual(self.calculator.multiplication(2, True), 2)

    def test_multiplication_float_bool(self):
        self.assertEqual(self.calculator.multiplication(1/3, False), 0)

    def test_multiplication_list_bool(self):
        self.assertEqual(self.calculator.multiplication(
            [1, 2, 3, 4, 4], False), [])

    def test_multiplication_string_and_string(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "1", "11")

    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(0.25, 1/4), 0.0625)

    def test_multiplication_more_argument(self):
        self.assertRaises(
            TypeError, self.calculator.multiplication, 1, 1, 1, 1, 1, 1)

    def test_multiplication_complex_and_int(self):
        self.assertEqual(self.calculator.multiplication(1j+3, 3), 3j+9)

    def test_multiplication_two_complex(self):
        self.assertEqual(self.calculator.multiplication(1j, 1j), -1)

    def test_subtraction_int(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(5, -5), 10)

    def test_subtraction_int_string(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 2, "1")

    def test_subtraction_int_bool(self):
        self.assertEqual(self.calculator.subtraction(2, True), 1)

    def test_subtraction_float_bool(self):
        self.assertEqual(self.calculator.subtraction(1/3, False), 1/3)

    def test_subtraction_list_bool(self):
        self.assertRaises(TypeError, self.calculator.subtraction,
                          [1, 2, 3, 4, 4], False)

    def test_subtraction_strings(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "1", "11")

    def test_subtraction_float(self):
        self.assertEqual(self.calculator.subtraction(0.25, 1/4), 0)

    def test_subtraction_more_arguments(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 1, 1)

    def test_subtraction_int_and_complex(self):
        self.assertEqual(self.calculator.subtraction(0.25, 1j), 0.25-1j)

    def test_division_int(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(5, -5), -1)

    def test_division_int_string(self):
        self.assertRaises(TypeError, self.calculator.division, 2, "1")

    def test_division_int_bool(self):
        self.assertEqual(self.calculator.division(2, True), 2)

    def test_division_float_bool(self):
        self.assertEqual(self.calculator.division(1/3, False), None)

    def test_division_list_int(self):
        self.assertRaises(TypeError, self.calculator.division,
                          [1, 2, 3, 4, 4], 1.2)

    def test_division_strings(self):
        self.assertRaises(TypeError, self.calculator.division, "1", "11")

    def test_division_float(self):
        self.assertEqual(self.calculator.division(0.25, 1/4), 1)

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_division_more_argument(self):
        self.assertRaises(
            TypeError, self.calculator.division, 1, 1, 1, 1, 1, 1)

    def test_division_int_complex(self):
        self.assertEqual(self.calculator.division(0.25, 1j), -0.25j)

    def test_division_complex_int(self):
        self.assertEqual(self.calculator.division(6 + 3j, 3), 2 + 1j)

    def test_division_complex_numbers(self):
        self.assertEqual(self.calculator.division(6 + 3j, 6 + 3j), 1)

    def test_absolute_default(self):
        self.assertEqual(self.calculator.absolute(2), 2)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_string(self):
        self.assertRaises(TypeError, self.calculator.absolute, "1")

    def test_absolute_bool(self):
        self.assertEqual(self.calculator.absolute(True), 1)

    def test_absolute_negative_float(self):
        self.assertEqual(self.calculator.absolute(-1/3), 1/3)

    def test_absolute_more_argument(self):
        self.assertRaises(TypeError, self.calculator.absolute,
                          [1, 2, 3, 4, 4], False)

    def test_absolute_list(self):
        self.assertRaises(TypeError, self.calculator.absolute, [1, 2, 3, 4, 5])

    def test_absolute_complex(self):
        self.assertEqual(self.calculator.absolute(3 + 4j), 5)

    def test_degree_int_bool(self):
        self.assertEqual(self.calculator.degree(200, False), 1)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(5, -2), 1/25)

    def test_degree_string_power(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, "1",)

    def test_degree_int_bool(self):
        self.assertEqual(self.calculator.degree(2, True), 2)

    def test_degree_bool_float(self):
        self.assertEqual(self.calculator.degree(False, 1/3), 0)

    def test_degree_list(self):
        self.assertRaises(TypeError, self.calculator.degree,
                          False, [1, 2, 3, 4, 4])

    def test_degree_string_int(self):
        self.assertRaises(TypeError, self.calculator.degree, "1", 4)

    def test_degree_fractional_power(self):
        self.assertEqual(self.calculator.degree(16, 1/4), 2)

    def test_degree_more_argument(self):
        self.assertRaises(
            TypeError, self.calculator.degree, 1, 1, 1, 1, 1, 1)

    def test_degree_complex_number_sqr(self):
        self.assertEqual(self.calculator.degree(1j, 2), -1)

    def test_degree_complex_number(self):
        self.assertEqual(self.calculator.degree(1j+2, 3), 2+11j)

    def test_degree_negative_number(self):
        self.assertEqual(self.calculator.degree(-5, 3), -125)

    def test_degree_negative_number_fractional_power(self):
        self.assertAlmostEqual(self.calculator.degree(-1, 1/2), 1j)

    def test_ln_default(self):
        self.assertEqual(self.calculator.ln(math.exp(4)), 4)

    def test_ln_from_1(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_string(self):
        self.assertRaises(TypeError, self.calculator.ln, "1")

    def test_ln_bool(self):
        self.assertEqual(self.calculator.ln(True), 0)

    def test_ln_negative_power_exp(self):
        self.assertEqual(self.calculator.ln(math.exp(-2)), -2)

    def test_ln_bool_and_zero(self):
        self.assertRaises(ValueError, self.calculator.ln,
                          False)

    def test_ln_list(self):
        self.assertRaises(TypeError, self.calculator.ln, [1, 2, 3, 4, 5])

    def test_ln_complex(self):
        self.assertRaises(TypeError, self.calculator.ln, 5 + 1j)

    def test_ln_more_argument(self):
        self.assertRaises(TypeError, self.calculator.ln, -10, 10)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -10)

    def test_log_default(self):
        self.assertEqual(self.calculator.log(100, 10), 2)

    def test_log_anorher_base(self):
        self.assertEqual(self.calculator.log(16, 2), 4)

    def test_log_string(self):
        self.assertRaises(TypeError, self.calculator.log, 1, "1")

    def test_log_bool(self):
        self.assertEqual(self.calculator.log(True, 1000), 0)

    def test_log_negative_result(self):
        self.assertEqual(self.calculator.log(1/9, 3), -2)

    def test_log_bool_and_zero_by_base(self):
        self.assertRaises(ValueError, self.calculator.log,
                          False, 10)

    def test_log_list(self):
        self.assertRaises(TypeError, self.calculator.log, [1, 2, 3, 4, 5])

    def test_log_complex_number(self):
        self.assertRaises(TypeError, self.calculator.log, 5 + 1j, 10)

    def test_log_negative_bu_number(self):
        self.assertRaises(ValueError, self.calculator.log, -10, 10)

    def test_log_complex_by_base(self):
        self.assertRaises(TypeError, self.calculator.log, 1, 1j)

    def test_log_base_1(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 10, 1)

    def test_log_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, 10, -1)

    def test_sqrt_default(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_string(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "1")

    def test_sqrt_bool(self):
        self.assertEqual(self.calculator.sqrt(True), 1)

    # По факту должно быть два решения (+- 2j).
    # Для простоты считаем, что оно одно
    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)

    def test_sqrt_more_argument(self):
        self.assertRaises(TypeError, self.calculator.sqrt,
                          1, 2, 3, )

    def test_sqrt_list(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2, 3, 4, 5])

    def test_sqrt_complex_number(self):
        self.assertAlmostEqual(self.calculator.sqrt(2j), 1+1j)

    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(0.81), 0.9)

    def test_nth_root_default(self):
        self.assertEqual(self.calculator.nth_root(200, 1), 200)

    def test_nth_root_negative_base(self):
        self.assertEqual(self.calculator.nth_root(25, -2), 1/5)

    def test_nth_root_string_base(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, "1",)

    def test_nth_root_bool_and(self):
        self.assertRaises(ZeroDivisionError,
                          self.calculator.nth_root, 2, False)
        
    def test_nth_root_zero_base(self):
        self.assertRaises(ZeroDivisionError,
                          self.calculator.nth_root, 2, 0)

    def test_nth_root_zero_number(self):
        self.assertEqual(self.calculator.nth_root(0, 1/3), 0)

    def test_nth_root_list(self):
        self.assertRaises(TypeError, self.calculator.nth_root,
                          False, [1, 2, 3, 4, 4])

    def test_nth_root_string(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "1", 4)

    def test_nth_root_fractional_power(self):
        self.assertEqual(self.calculator.nth_root(16, 1/4), 65536)

    def test_nth_root_more_argument(self):
        self.assertRaises(
            TypeError, self.calculator.nth_root, 1, 1, 1, 1, 1, 1)

    def test_nth_root_complex_number(self):
        self.assertAlmostEqual(self.calculator.nth_root(2j, 3), 1.09+0.63j, 2)

    def test_nth_root_n_more_2(self):
        self.assertEqual(self.calculator.nth_root(1024, 10), 2)

    def test_nth_root_complex_power(self):
        self.assertAlmostEqual(self.calculator.nth_root(1024, 1j), 0.8-0.6j, 2)


if __name__ == "__main__":
    unittest.main()
