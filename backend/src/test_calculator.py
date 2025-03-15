import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # addition
    def test_add_int_pos(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_int_neg(self):
        self.assertAlmostEqual(self.calculator.addition(-1, -2), -3)

    def test_add_int_zero(self):
        self.assertAlmostEqual(self.calculator.addition(1, 0), 1)

    def test_add_float_pos(self):
        self.assertEqual(self.calculator.addition(1.1, 1.2), 2.3)

    def test_add_float_neg(self):
        self.assertEqual(self.calculator.addition(-1.1, -1.2), -2.3)

    def test_add_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_add_invalid_string(self):
        self.assertRaises(TypeError, self.calculator.addition, "abc", None)

    def test_add_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.addition, [1, 2, 3], 1)

    # multiplication
    def test_mul_int_pos(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_mul_int_neg(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_mul_int_mixed_sign(self):
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)

    def test_mul_float_pos(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.5, 2.5), 3.75)

    def test_mul_float_neg(self):
        self.assertAlmostEqual(self.calculator.multiplication(-1.5, -2.5), 3.75)

    def test_mul_float_mixed_sign(self):
        self.assertAlmostEqual(self.calculator.multiplication(-1.5, 2.5), -3.75)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(5, 0), 0)

    def test_mul_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)

    def test_mul_invalid_string(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "abc", None)

    def test_mul_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2, 3], [1, 2])

    # subtraction
    def test_sub_int_pos(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_sub_int_neg(self):
        self.assertEqual(self.calculator.subtraction(-5, -3), -2)

    def test_sub_int_mixed_sign(self):
        self.assertEqual(self.calculator.subtraction(-5, 3), -8)

    def test_sub_float_pos(self):
        self.assertAlmostEqual(self.calculator.subtraction(5.5, 3.3), 2.2)

    def test_sub_float_neg(self):
        self.assertAlmostEqual(self.calculator.subtraction(-5.5, -3.3), -2.2)

    def test_sub_float_mixed_sign(self):
        self.assertAlmostEqual(self.calculator.subtraction(-5.5, 3.3), -8.8)

    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(5, 0), 5)

    def test_sub_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)

    def test_sub_invalid_string(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", None)

    def test_sub_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2, 3], [1, 2])

    # division
    def test_div_int_pos(self):
        self.assertEqual(self.calculator.division(6, 3), 2)

    def test_div_int_neg(self):
        self.assertEqual(self.calculator.division(-6, -3), 2)

    def test_div_int_mixed_sign(self):
        self.assertEqual(self.calculator.division(-6, 3), -2)

    def test_div_float_pos(self):
        self.assertAlmostEqual(self.calculator.division(6.6, 3.3), 2.0)

    def test_div_float_neg(self):
        self.assertAlmostEqual(self.calculator.division(-6.6, -3.3), 2.0)

    def test_div_float_mixed_sign(self):
        self.assertAlmostEqual(self.calculator.division(-6.6, 3.3), -2.0)

    def test_div_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))

    def test_div_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    def test_div_invalid_string(self):
        self.assertRaises(TypeError, self.calculator.division, "abc", None)

    def test_div_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.division, [1, 2, 3], [1, 2])

    # absolute
    def test_abs_int_pos(self):
        self.assertEqual(self.calculator.absolute(1), 1)

    def test_abs_int_neg(self):
        self.assertEqual(self.calculator.absolute(-1), 1)

    def test_abs_int_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_abs_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.absolute, None, None)

    def test_abs_invalid_string(self):
        self.assertRaises(TypeError, self.calculator.absolute, "abc")

    def test_abs_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.absolute, [1, 2, 3])

    # degree
    def test_degree_int_pos_to_int_pos(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_int_pos_to_int_neg(self):
        self.assertEqual(self.calculator.degree(2, -3), 0.125)

    def test_degree_int_pos_to_zero(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree_int_to_float(self):
        self.assertAlmostEqual(self.calculator.degree(2, 2.5), 5.6568542)

    def test_degree_float_pos_to_int_pos(self):
        self.assertAlmostEqual(self.calculator.degree(2.5, 2), 6.25)

    def test_degree_float_pos_to_int_neg(self):
        self.assertAlmostEqual(self.calculator.degree(2.5, -2), 0.16)

    def test_degree_float_pos_to_zero(self):
        self.assertEqual(self.calculator.degree(2.5, 0), 1)

    def test_degree_float_to_float(self):
        self.assertAlmostEqual(self.calculator.degree(3.5, 2.5), 22.9176515)

    def test_degree_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.degree, None, None)

    def test_degree_invalid_str(self):
        self.assertRaises(TypeError, self.calculator.degree, "abc", 2)

    def test_degree_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.degree, [1, 2, 3], [1, 2])

    # ln
    def test_ln_pos(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_ln_euler(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_float_pos(self):
        self.assertAlmostEqual(self.calculator.ln(10.3), 2.3321439)

    def test_ln_invalid_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_invalid_neg(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_invalid_str(self):
        self.assertRaises(TypeError, self.calculator.ln, "abc")

    def test_ln_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.ln, [1, 2, 3])

    # log
    def test_log_int_pos(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_float_pos(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_invalid_base_one(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 10, 1)

    def test_log_invalid_base_zero(self):
        self.assertRaises(ValueError, self.calculator.log, 10, 0)

    def test_log_invalid_base_neg(self):
        self.assertRaises(ValueError, self.calculator.log, 10, -2)

    def test_log_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.log, None, None)

    def test_log_invalid_str(self):
        self.assertRaises(TypeError, self.calculator.log, "abc", 2)

    def test_log_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.log, [1, 2, 3])

    # sqrt
    def test_sqrt_int_pos(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_float_pos(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.25), 1.5)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_neg(self):
        self.assertAlmostEqual(self.calculator.sqrt(-4), 2j)

    def test_sqrt_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_invalid_str(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "abc")

    def test_sqrt_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2, 3])

    # nth_root
    def test_nth_root_int_pos(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_float_pos(self):
        self.assertAlmostEqual(self.calculator.nth_root(1.4641, 3), 1.1, places=1)

    def test_nth_root_neg_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(10, -2), 0.3162278)

    def test_nth_root_zero_base(self):
        self.assertEqual(self.calculator.nth_root(0, 2), 0)

    def test_nth_root_invalid_zero_root(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 10, 0)

    def test_nth_root_invalid_None(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, None)

    def test_nth_root_invalid_str(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "abc", 2)

    def test_nth_root_invalid_arr(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
