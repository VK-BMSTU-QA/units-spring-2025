import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # addition tests
    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(1, 0), 1)

    def test_add_zeros(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_positive_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative_int(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_mixed_int(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)
        
    def test_add_positive_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.0, 2.0), 3.0)

    def test_add_negative_float(self):
        self.assertAlmostEqual(self.calculator.addition(-1.0, -2.0), -3.0)

    def test_add_mixed_float(self):
        self.assertAlmostEqual(self.calculator.addition(-1.0, 2.0), 1.0)

    def test_add_mixed_types_int_float(self):
        self.assertAlmostEqual(self.calculator.addition(-1, 2.0), 1.0)

    def test_add_big_nums(self):
        self.assertEqual(self.calculator.addition(1e100, 3e100), 4e100)
    
    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(float("inf"), 1), float("inf"))

    def test_add_complexs(self):
        self.assertEqual(self.calculator.addition(1+1j, 2-2j), 3-1j)

    def test_add_complex_int(self):
        self.assertEqual(self.calculator.addition(1+1j, 1), 2+1j)

    def test_add_complex_float(self):
        self.assertEqual(self.calculator.addition(1+1j, 1.0), 2+1j)

    def test_add_complex_zero(self):
        self.assertEqual(self.calculator.addition(0+0j, 0), 0+0j)

    def test_add_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.addition, "abc", 1)

    """ def test_add_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.addition, "abc", "def") """

    def test_add_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.addition, [1,2,3], 1)

    def test_add_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.addition, {1,2,3}, 1)

    def test_add_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.addition, (1,2,3), 1)

    def test_add_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.addition, {1:1, 2:2, 3:3}, 1)

    def test_add_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, 1)

    """ def test_add_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.addition, True, 1) """

    
    # subtraction tests
    def test_subtract_zero(self):
        self.assertEqual(self.calculator.subtraction(1, 0), 1)

    def test_subtract_zeros(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtract_positive_int(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtract_negative_int(self):
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)

    def test_subtract_mixed_int(self):
        self.assertEqual(self.calculator.subtraction(-1, 2), -3)
        
    def test_subtract_positive_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(1.0, 2.0), -1.0)

    def test_subtract_negative_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(-1.0, -2.0), 1.0)

    def test_subtract_mixed_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(-1.0, 2.0), -3.0)

    def test_subtract_mixed_types_int_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(-1, 2.0), -3.0)

    def test_subtract_big_nums(self):
        self.assertEqual(self.calculator.subtraction(1e100, 2e100), -1e100)
    
    def test_subtract_inf(self):
        self.assertEqual(self.calculator.subtraction(float("inf"), 1), float("inf"))

    def test_subtract_complexs(self):
        self.assertEqual(self.calculator.subtraction(1+1j, 2-2j), -1+3j)

    def test_subtract_complex_int(self):
        self.assertEqual(self.calculator.subtraction(1+1j, 1), 0+1j)

    def test_subtract_complex_float(self):
        self.assertEqual(self.calculator.subtraction(1+1j, 1.0), 0+1j)

    def test_subtract_complex_zero(self):
        self.assertEqual(self.calculator.subtraction(0+0j, 0), 0+0j)

    def test_subtract_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", 1)

    def test_subtract_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", "def")

    def test_subtract_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [1,2,3], 1)

    def test_subtract_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.subtraction, {1,2,3}, 1)

    def test_subtract_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.subtraction, (1,2,3), 1)

    def test_subtract_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.subtraction, {1:1, 2:2, 3:3}, 1)

    def test_subtract_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)

    """ def test_subtract_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.subtraction, True, 1) """


    # multiplication tests
    def test_multiply_zero(self):
        self.assertEqual(self.calculator.multiplication(1, 0), 0)

    def test_multiply_zeros(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiply_positive_int(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multiply_negative_int(self):
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)

    def test_multiply_mixed_int(self):
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        
    def test_multiply_positive_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.0, 2.0), 2.0)

    def test_multiply_negative_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(-1.0, -2.0), 2.0)

    def test_multiply_mixed_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(-1.0, 2.0), -2.0)

    def test_multiply_mixed_types_int_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(-1, 2.0), -2.0)

    def test_multiply_big_nums(self):
        self.assertEqual(self.calculator.multiplication(1e100, 2e100), 2e200)
    
    def test_multiply_inf(self):
        self.assertEqual(self.calculator.multiplication(float("inf"), 1), float("inf"))

    def test_multiply_complexs(self):
        self.assertEqual(self.calculator.multiplication(1+1j, 2-2j), 4+0j)

    def test_multiply_complex_int(self):
        self.assertEqual(self.calculator.multiplication(1+1j, 2), 2+2j)

    def test_multiply_complex_float(self):
        self.assertEqual(self.calculator.multiplication(1+1j, 1.0), 1+1j)

    def test_multiply_complex_zero(self):
        self.assertEqual(self.calculator.multiplication(0+0j, 0), 0+0j)

    """ def test_multiply_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "abc", 1) """

    def test_multiply_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "abc", "def")

    """ def test_multiply_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.multiplication, [1,2,3], 1) """

    def test_multiply_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.multiplication, {1,2,3}, 1)

    """ def test_multiply_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.multiplication, (1,2,3), 1) """

    def test_multiply_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.multiplication, {1:1, 2:2, 3:3}, 1)

    def test_multiply_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, 1)

    """ def test_multiply_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.multiplication, True, 1) """


    # division tests
    def test_divide_zero(self):
        self.assertEqual(self.calculator.division(0, 1), 0)

    def test_divide_zero_division(self):
        self.assertIsNone(self.calculator.division(1, 0))

    def test_divide_positive_int(self):
        self.assertAlmostEqual(self.calculator.division(1, 2), 0.5)

    def test_divide_negative_int(self):
        self.assertAlmostEqual(self.calculator.division(-1, -2), 0.5)

    def test_divide_mixed_int(self):
        self.assertAlmostEqual(self.calculator.division(-1, 2), -0.5)
        
    def test_divide_positive_float(self):
        self.assertAlmostEqual(self.calculator.division(1.0, 2.0), 0.5)

    def test_divide_negative_float(self):
        self.assertAlmostEqual(self.calculator.division(-1.0, -2.0), 0.5)

    def test_divide_mixed_float(self):
        self.assertAlmostEqual(self.calculator.division(-1.0, 2.0), -0.5)

    def test_divide_mixed_types_int_float(self):
        self.assertAlmostEqual(self.calculator.division(-1, 2.0), -0.5)

    def test_divide_big_nums(self):
        self.assertEqual(self.calculator.division(2e200, 1e100), 2e100)
    
    def test_divide_inf(self):
        self.assertEqual(self.calculator.division(float("inf"), 1), float("inf"))

    def test_divide_complexs(self):
        self.assertAlmostEqual(self.calculator.division(1+1j, 2-2j), 0+0.5j)

    def test_divide_complex_int(self):
        self.assertAlmostEqual(self.calculator.division(1+1j, 2), 0.5+0.5j)

    def test_divide_complex_float(self):
        self.assertEqual(self.calculator.division(1+1j, 1.0), 1+1j)

    def test_divide_complex_zero(self):
        self.assertEqual(self.calculator.division(0+0j, 2), 0+0j)

    def test_divide_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.division, "abc", 1)

    def test_divide_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.division, "abc", "def")

    def test_divide_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.division, [1,2,3], 1)

    def test_divide_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.division, {1,2,3}, 1)

    def test_divide_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.division, (1,2,3), 1)

    def test_divide_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.division, {1:1, 2:2, 3:3}, 1)

    def test_divide_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, 1)

    """ def test_divide_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.division, True, 1) """

    
    # degree tests
    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(1, 0), 1)

    def test_degree_zeros(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_positive_int(self):
        self.assertEqual(self.calculator.degree(1, 2), 1)
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_negative_int(self):
        self.assertAlmostEqual(self.calculator.degree(-2, -2), 0.25)

    def test_degree_mixed_int(self):
        self.assertEqual(self.calculator.degree(-1, 2), 1)
        
    def test_degree_positive_float(self):
        self.assertAlmostEqual(self.calculator.degree(1.0, 2.0), 1.0)

    def test_degree_negative_float(self):
        self.assertAlmostEqual(self.calculator.degree(-1.0, -2.0), 1.0)

    def test_degree_mixed_float(self):
        self.assertAlmostEqual(self.calculator.degree(-1.0, 2.0), 1.0)

    def test_degree_mixed_types_int_float(self):
        self.assertAlmostEqual(self.calculator.degree(-1, 2.0), 1.0)
    
    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(float("inf"), 1), float("inf"))

    def test_degree_complexs(self):
        self.assertAlmostEqual(self.calculator.degree(1+1j, 2-2j), 6.14741753403898 + 7.40081267114005j)

    def test_degree_complex_int(self):
        self.assertEqual(self.calculator.degree(1+1j, 1), 1+1j)

    def test_degree_complex_float(self):
        self.assertAlmostEqual(self.calculator.degree(1+1j, 1.0), 1+1j)

    def test_degree_complex_zero(self):
        self.assertEqual(self.calculator.degree(0+0j, 0), 1+0j)

    def test_degree_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.degree, "abc", 1)

    def test_degree_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.degree, "abc", "def")

    def test_degree_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.degree, [1,2,3], 1)

    def test_degree_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.degree, {1,2,3}, 1)

    def test_degree_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.degree, (1,2,3), 1)

    def test_degree_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.degree, {1:1, 2:2, 3:3}, 1)

    def test_degree_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 1)

    """ def test_degree_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.degree, True, 1) """


    # nth_root tests
    def test_nth_root_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)

    def test_nth_root_zeros(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 0, 0)

    def test_nth_root_positive_int(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertAlmostEqual(self.calculator.nth_root(2, 3), 2 ** (1/3))

    def test_nth_root_negative_int(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2, -2), (-2) ** (-1./2))

    def test_nth_root_mixed_int(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2, 2), (-2)**(1/2))

    def test_nth_root_positive_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(1.0, 2.0), 1.0)
    
    def test_nth_root_negative_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(-1.0, -2.0), (-1.0) ** (-1./2))

    def test_nth_root_mixed_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2.0, 2.0), (-2.0)**(1/2.0))

    def test_nth_root_mixed_types_int_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2, 2.0), (-2)**(1/2.0))

    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(float("inf"), 1), float("inf"))

    def test_nth_root_complexs(self):
        self.assertAlmostEqual(self.calculator.nth_root(1+1j, 2-2j), (1+1j) ** (1/(2-2j)))

    def test_nth_root_complex_int(self):
        self.assertEqual(self.calculator.nth_root(1+1j, 1), 1+1j)

    def test_nth_root_complex_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(1+1j, 1.0), 1+1j)

    def test_nth_root_complex_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 0+0j, 0)

    def test_nth_root_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "abc", 1)

    def test_nth_root_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "abc", "def")

    def test_nth_root_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [1,2,3], 1)

    def test_nth_root_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.nth_root, {1,2,3}, 1)

    def test_nth_root_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.nth_root, (1,2,3), 1)

    def test_nth_root_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.nth_root, {1:1, 2:2, 3:3}, 1)

    def test_nth_root_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 1)

    """ def test_nth_root_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.nth_root, True, 1) """


    # log tests
    def test_log_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 1)

    def test_log_zeros(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 0)

    def test_log_positive_int(self):
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertAlmostEqual(self.calculator.log(2, 3), math.log(2, 3))

    def test_log_negative_int(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-2, -2)

    def test_log_mixed_int(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_log_positive_float(self):
        self.assertAlmostEqual(self.calculator.log(2.0, 2.0), 1.0)
    
    def test_log_negative_float(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1.0, -2.0)

    def test_log_mixed_float(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1.0, 2.0)

    def test_log_mixed_types_int_float(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2.0)

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(float("inf"), 2), float("inf"))

    def test_log_complexs(self):
        self.assertRaises(TypeError, self.calculator.log, 1+1j, 2-2j)

    def test_log_complex_int(self):
        self.assertRaises(TypeError, self.calculator.log, 1+1j, 1)

    def test_log_complex_float(self):
        self.assertRaises(TypeError, self.calculator.log, 3.0+4.0j, 1)

    def test_log_complex_zero(self):
        self.assertRaises(TypeError, self.calculator.log, 0.0+0.0j, 1)

    def test_log_mixed_types_string_int(self):
        self.assertRaises(TypeError, self.calculator.log, "abc", 1)

    def test_log_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.log, "abc", "def")

    def test_log_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.log, [1,2,3], 1)

    def test_log_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.log, {1,2,3}, 1)

    def test_log_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.log, (1,2,3), 1)

    def test_log_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.log, {1:1, 2:2, 3:3}, 1)

    def test_log_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, 1)

    """ def test_log_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.log, True, 2) """

    
    # absolute tests
    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_positive_int(self):
        self.assertEqual(self.calculator.absolute(1), 1)

    def test_absolute_negative_int(self):
        self.assertEqual(self.calculator.absolute(-2), 2)

    def test_absolute_positive_float(self):
        self.assertAlmostEqual(self.calculator.absolute(1.0), 1.0)
    
    def test_absolute_negative_float(self):
        self.assertAlmostEqual(self.calculator.absolute(-1.0), 1.0)

    def test_absolute_inf(self):
        self.assertEqual(self.calculator.absolute(float("inf")), float("inf"))

    def test_absolute_complex_int(self):
        self.assertAlmostEqual(self.calculator.absolute(1+1j), 2**(1/2))

    def test_absolute_complex_float(self):
        self.assertAlmostEqual(self.calculator.absolute(3.0+4.0j), 5.0)

    def test_absolute_complex_zero(self):
        self.assertAlmostEqual(self.calculator.absolute(0+0j), 0.0)

    def test_absolute_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.absolute, "abc")

    def test_absolute_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.absolute, [1,2,3])

    def test_absolute_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.absolute, {1,2,3})

    def test_absolute_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.absolute, (1,2,3))

    def test_absolute_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.absolute, {1:1, 2:2, 3:3})

    def test_absolute_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    """ def test_absolute_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.absolute, True) """

    
    # ln tests
    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_positive_int(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0.0)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1.0)

    def test_ln_negative_int(self):
        self.assertRaises(ValueError, self.calculator.ln, -2)

    def test_ln_positive_float(self):
        self.assertAlmostEqual(self.calculator.ln(1.0), 0.0)
    
    def test_ln_negative_float(self):
        self.assertRaises(ValueError, self.calculator.ln, -1.0)

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(float("inf")), float("inf"))

    def test_ln_complex_int(self):
        self.assertRaises(TypeError, self.calculator.ln, 1+1j)

    def test_ln_complex_float(self):
        self.assertRaises(TypeError, self.calculator.ln, 3.0+4.0j)

    def test_ln_complex_zero(self):
        self.assertRaises(TypeError, self.calculator.ln, 0+0j)

    def test_ln_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.ln, "abc")

    def test_ln_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.ln, [1,2,3])

    def test_ln_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.ln, {1,2,3})

    def test_ln_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.ln, (1,2,3))

    def test_ln_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.ln, {1:1, 2:2, 3:3})

    def test_ln_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    """ def test_ln_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.ln, True) """

    
    # sqrt tests
    def test_sqrt_zero(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0.0)

    def test_sqrt_positive_int(self):
        self.assertAlmostEqual(self.calculator.sqrt(1), 1.0)

    def test_sqrt_negative_int(self):
        self.assertAlmostEqual(self.calculator.sqrt(-2), (-2)**(1/2))

    def test_sqrt_positive_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(1.0), 1.0)
    
    def test_sqrt_negative_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(-2.0), (-2.0)**(1/2))

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(float("inf")), float("inf"))

    def test_sqrt_complex_int(self):
        result = self.calculator.sqrt(1+1j)
        expected = (1 + 1j) ** 0.5
        self.assertAlmostEqual(result.real, expected.real)
        self.assertAlmostEqual(result.imag, expected.imag)

    def test_sqrt_complex_float(self):
        result = self.calculator.sqrt(3.0+4.0j)
        expected = (3.0 + 4.0j) ** 0.5
        self.assertAlmostEqual(result.real, expected.real)
        self.assertAlmostEqual(result.imag, expected.imag)

    def test_sqrt_complex_zero(self):
        result = self.calculator.sqrt(0+0j)
        self.assertAlmostEqual(result.real, 0.0)
        self.assertAlmostEqual(result.imag, 0.0)

    def test_sqrt_wrong_types_strings(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "abc")

    def test_sqrt_wrong_types_list(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1,2,3])

    def test_sqrt_wrong_types_set(self):
        self.assertRaises(TypeError, self.calculator.sqrt, {1,2,3})

    def test_sqrt_wrong_types_tuple(self):
        self.assertRaises(TypeError, self.calculator.sqrt, (1,2,3))

    def test_sqrt_wrong_types_dict(self):
        self.assertRaises(TypeError, self.calculator.sqrt, {1:1, 2:2, 3:3})

    def test_sqrt_wrong_types_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    """ def test_sqrt_wrong_types_bool(self):
        self.assertRaises(TypeError, self.calculator.sqrt, True) """


if __name__ == "__main__":
    unittest.main()
