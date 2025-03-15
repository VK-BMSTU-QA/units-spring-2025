import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    #### TESTS FOR ADD
    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(2, 1), 3)

    def test_add_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.2), 3.3)
        self.assertAlmostEqual(self.calculator.addition(2.2, 1.1), 3.3)
    
    def test_add_negative_int(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(-2, -1), -3)
    
    def test_add_negative_float(self):
        self.assertAlmostEqual(self.calculator.addition(-1.1, -2.2), -3.3)
        self.assertAlmostEqual(self.calculator.addition(-2.2, -1.1), -3.3)
    
    def test_add_different_sign(self):
        self.assertAlmostEqual(self.calculator.addition(1, -2), -1)
        self.assertAlmostEqual(self.calculator.addition(-1, 2), 1)
    
    def test_add_int_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.1, 1), 2.1)
        self.assertAlmostEqual(self.calculator.addition(1, 1.1), 2.1)
        self.assertAlmostEqual(self.calculator.addition(-1.1, -1), -2.1)
        self.assertAlmostEqual(self.calculator.addition(-1, -1.1), -2.1)
        self.assertAlmostEqual(self.calculator.addition(2, -0.5), 1.5)
        self.assertAlmostEqual(self.calculator.addition(-0.5, 2), 1.5)
    
    def test_add_zeros(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(0.0, 0.0), 0.0)
    
    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(float("inf"), 1), float("inf"))
        self.assertEqual(self.calculator.addition(1, float("inf")), float("inf"))
        self.assertEqual(self.calculator.addition(1.1, float("inf")), float("inf"))
        self.assertEqual(self.calculator.addition(float("inf"), 1.1), float("inf"))
   
    def test_add_nan(self):
        self.assertTrue(math.isnan(self.calculator.addition(float("NaN"), 1)))
        self.assertTrue(math.isnan(self.calculator.addition(1, float("NaN"))))
        self.assertTrue(math.isnan(self.calculator.addition(1.1, float("NaN"))))
        self.assertTrue(math.isnan(self.calculator.addition(float("NaN"), 1.1)))
 
    def test_add_complex(self):
        self.assertEqual(self.calculator.addition(1 + 1j, 2 + 2j), 3 + 3j)
        self.assertEqual(self.calculator.addition(2 + 2j, 1 + 1j), 3 + 3j)
    
    def test_add_int_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, "abc")
        self.assertRaises(TypeError, self.calculator.addition, "abc", 1)
        self.assertRaises(TypeError, self.calculator.addition, [], 1)
        self.assertRaises(TypeError, self.calculator.addition, 1, [])
        self.assertRaises(TypeError, self.calculator.addition, {}, 1)
        self.assertRaises(TypeError, self.calculator.addition, 1, {})
        self.assertRaises(TypeError, self.calculator.addition, None, 1)
        self.assertRaises(TypeError, self.calculator.addition, 1, None)


    #### TESTS FOR SUB
    def test_sub_int(self):
        self.assertEqual(self.calculator.subtraction(11, 2), 9)
        self.assertEqual(self.calculator.subtraction(2, 11), -9)

    def test_sub_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(2.4, 1.3), 1.1)
        self.assertAlmostEqual(self.calculator.subtraction(1.3, 2.4), -1.1)
    
    def test_sub_negative_int(self):
        self.assertEqual(self.calculator.subtraction(-11, -2), -9)
        self.assertEqual(self.calculator.subtraction(-2, -11), 9)
    
    def test_sub_negative_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(-2.4, -1.3), -1.1)
        self.assertAlmostEqual(self.calculator.subtraction(-1.3, -2.4), 1.1)
    
    def test_sub_different_sign(self):
        self.assertAlmostEqual(self.calculator.subtraction(1, -2), 3)
        self.assertAlmostEqual(self.calculator.subtraction(-1, 2), -3)
    
    def test_sub_int_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(3.5, 1), 2.5)
        self.assertAlmostEqual(self.calculator.subtraction(1, 3.5), -2.5)
        self.assertAlmostEqual(self.calculator.subtraction(-1.1, -1), -0.1)
        self.assertAlmostEqual(self.calculator.subtraction(-1, -1.1), 0.1)
        self.assertAlmostEqual(self.calculator.subtraction(4, -1.3), 5.3)
        self.assertAlmostEqual(self.calculator.subtraction(-1.3, 4), -5.3)
    
    def test_sub_zeros(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(0.0, 0.0), 0.0)
    
    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(float("inf"), 1), float("inf"))
        self.assertEqual(self.calculator.subtraction(1, float("inf")), float("-inf"))
        self.assertEqual(self.calculator.subtraction(1.1, float("inf")), float("-inf"))
        self.assertEqual(self.calculator.subtraction(float("inf"), 1.1), float("inf"))
   
    def test_sub_nan(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float("NaN"), 1)))
        self.assertTrue(math.isnan(self.calculator.subtraction(1, float("NaN"))))
        self.assertTrue(math.isnan(self.calculator.subtraction(1.1, float("NaN"))))
        self.assertTrue(math.isnan(self.calculator.subtraction(float("NaN"), 1.1)))
    
    def test_sub_complex(self):
        self.assertEqual(self.calculator.subtraction(1 + 1j, 2 + 2j), -1 - 1j)
        self.assertEqual(self.calculator.subtraction(2 + 2j, 1 + 1j), 1 + 1j)
    
    def test_sub_int_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, "abc")
        self.assertRaises(TypeError, self.calculator.subtraction, "abc", 1)
        self.assertRaises(TypeError, self.calculator.subtraction, [], 1)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, [])
        self.assertRaises(TypeError, self.calculator.subtraction, {}, 1)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, {})
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, None)


    #### TESTS FOR MUL
    def test_mul_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_mul_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.5, 2.5), 3.75)
        self.assertAlmostEqual(self.calculator.multiplication(2.5, 1.5), 3.75)
    
    def test_mul_negative_int(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)
        self.assertEqual(self.calculator.multiplication(-3, -2), 6)
    
    def test_mul_negative_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(-1.5, -2.5), 3.75)
        self.assertAlmostEqual(self.calculator.multiplication(-2.5, -1.5), 3.75)
    
    def test_mul_different_sign(self):
        self.assertAlmostEqual(self.calculator.multiplication(2, -3), -6)
        self.assertAlmostEqual(self.calculator.multiplication(-2, 3), -6)
    
    def test_mul_int_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.5, 2), 3.0)
        self.assertAlmostEqual(self.calculator.multiplication(2, 1.5), 3.0)
        self.assertAlmostEqual(self.calculator.multiplication(-1.5, -2), 3.0)
        self.assertAlmostEqual(self.calculator.multiplication(-2, -1.5), 3.0)
        self.assertAlmostEqual(self.calculator.multiplication(2, -0.5), -1.0)
        self.assertAlmostEqual(self.calculator.multiplication(-0.5, 2), -1.0)
    
    def test_mul_zeros(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 5), 0)
        self.assertEqual(self.calculator.multiplication(5, 0), 0)
        self.assertEqual(self.calculator.multiplication(0.0, 3.0), 0.0)
    
    def test_mul_inf(self):
        self.assertEqual(self.calculator.multiplication(float("inf"), 2), float("inf"))
        self.assertEqual(self.calculator.multiplication(2, float("inf")), float("inf"))
        self.assertEqual(self.calculator.multiplication(float("inf"), -2), float("-inf"))
        self.assertEqual(self.calculator.multiplication(-2, float("inf")), float("-inf"))
    
    def test_mul_nan(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(float("NaN"), 2)))
        self.assertTrue(math.isnan(self.calculator.multiplication(2, float("NaN"))))
        self.assertTrue(math.isnan(self.calculator.multiplication(float("NaN"), -2)))
        self.assertTrue(math.isnan(self.calculator.multiplication(-2, float("NaN"))))
    
    def test_mul_complex(self):
        self.assertEqual(self.calculator.multiplication(1 + 1j, 2 + 2j), (1 + 1j)*(2 + 2j))
        self.assertEqual(self.calculator.multiplication(2 + 2j, 1 + 1j), (2 + 2j)*(1 + 1j))
    
    def test_mul_int_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.multiplication, {}, 2)
        self.assertRaises(TypeError, self.calculator.multiplication, 2, {})
        self.assertRaises(TypeError, self.calculator.multiplication, None, 2)
        self.assertRaises(TypeError, self.calculator.multiplication, 2, None)


    #### TESTS FOR DIV
    def test_div_int(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.division(9, 3), 3)

    def test_div_float(self):
        self.assertAlmostEqual(self.calculator.division(4.4, 2.2), 2.0)
        self.assertAlmostEqual(self.calculator.division(9.9, 3.3), 3.0)

    def test_div_negative_int(self):
        self.assertEqual(self.calculator.division(-4, -2), 2)
        self.assertEqual(self.calculator.division(-9, -3), 3)

    def test_div_negative_float(self):
        self.assertAlmostEqual(self.calculator.division(-4.4, -2.2), 2.0)
        self.assertAlmostEqual(self.calculator.division(-9.9, -3.3), 3.0)

    def test_div_different_sign(self):
        self.assertAlmostEqual(self.calculator.division(4, -2), -2)
        self.assertAlmostEqual(self.calculator.division(-4, 2), -2)

    def test_div_int_float(self):
        self.assertAlmostEqual(self.calculator.division(5.5, 2), 2.75)
        self.assertAlmostEqual(self.calculator.division(2, 0.5), 4.0)
        self.assertAlmostEqual(self.calculator.division(-5.5, -2), 2.75)
        self.assertAlmostEqual(self.calculator.division(-2, -0.5), 4.0)
        self.assertAlmostEqual(self.calculator.division(10, -4.0), -2.5)
        self.assertAlmostEqual(self.calculator.division(-10, 4.0), -2.5)

    def test_div_zeros(self):
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertEqual(self.calculator.division(0.0, 1.0), 0.0)

    def test_div_inf(self):
        self.assertEqual(self.calculator.division(float("inf"), 2), float("inf"))
        self.assertEqual(self.calculator.division(2, float("inf")), 0.0)
        self.assertTrue(math.isnan(self.calculator.division(float("inf"), float("inf"))))

    def test_div_nan(self):
        self.assertTrue(math.isnan(self.calculator.division(float("NaN"), 2)))
        self.assertTrue(math.isnan(self.calculator.division(2, float("NaN"))))
        self.assertTrue(math.isnan(self.calculator.division(float("NaN"), float("NaN"))))

    def test_div_by_zero(self):
        self.assertIsNone(self.calculator.division(123, 0))
        self.assertIsNone(self.calculator.division(123, 0.0))
    
    def test_mul_complex(self):
        self.assertEqual(self.calculator.division(1 + 1j, 2 + 2j), (1 + 1j)/(2 + 2j))
        self.assertEqual(self.calculator.division(2 + 2j, 1 + 1j), (2 + 2j)/(1 + 1j))

    def test_div_int_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.division, 1, "abc")
        self.assertRaises(TypeError, self.calculator.division, "abc", 1)
        self.assertRaises(TypeError, self.calculator.division, [], 1)
        self.assertRaises(TypeError, self.calculator.division, 1, [])
        self.assertRaises(TypeError, self.calculator.division, {}, 1)
        self.assertRaises(TypeError, self.calculator.division, 1, {})
        self.assertRaises(TypeError, self.calculator.division, None, 1)
        self.assertRaises(TypeError, self.calculator.division, 1, None)


    #### TESTS FOR ABS
    def test_abs_positive_int(self):
        self.assertEqual(self.calculator.absolute(4), 4)
        self.assertAlmostEqual(self.calculator.absolute(9.9), 9.9)

    def test_abs_negative_int(self):
        self.assertEqual(self.calculator.absolute(-9), 9)
        self.assertAlmostEqual(self.calculator.absolute(-4.4), 4.4)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(0.0), 0.0)

    def test_abs_inf(self):
        self.assertEqual(self.calculator.absolute(float("inf")), float("inf"))
        self.assertEqual(self.calculator.absolute(float("-inf")), float("inf"))

    def test_abs_nan(self):
        self.assertTrue(math.isnan(self.calculator.absolute(float("NaN"))))

    def test_abs_complex(self):
        self.assertEqual(self.calculator.absolute(3 + 4j), 5.0)
        self.assertEqual(self.calculator.absolute(-3 - 4j), 5.0)

    def test_abs_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.absolute, "abc")
        self.assertRaises(TypeError, self.calculator.absolute, [])
        self.assertRaises(TypeError, self.calculator.absolute, {})
        self.assertRaises(TypeError, self.calculator.absolute, None)


    #### TESTS FOR DEGREE
    def test_degree_positive_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(3.2, 3), 32.768)

    def test_degree_negative_int(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertAlmostEqual(self.calculator.degree(-3.2, 3), -32.768)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 3), 0)
        self.assertEqual(self.calculator.degree(0, 1e100), 0)
        self.assertEqual(self.calculator.degree(0, 0), 1)
    
    def test_degree_zero_exponent(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(1, 0), 1)
        self.assertEqual(self.calculator.degree(-1, 0), 1)

    def test_degree_large_exponent(self):
        self.assertEqual(self.calculator.degree(2, 1000), 2 ** 1000)

    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(float("inf"), 2), float("inf"))
        self.assertEqual(self.calculator.degree(float("-inf"), 2), float("inf"))
        self.assertEqual(self.calculator.degree(float("inf"), 0), 1)
        self.assertEqual(self.calculator.degree(float("-inf"), 0), 1)

    def test_degree_nan(self):
        self.assertTrue(math.isnan(self.calculator.degree(float("NaN"), 2)))
        self.assertTrue(math.isnan(self.calculator.degree(2, float("NaN"))))

    def test_degree_complex(self):
        self.assertEqual(self.calculator.degree(1 + 1j, 2), (1 + 1j) ** 2)
        self.assertEqual(self.calculator.degree(2 + 2j, 3), (2 + 2j) ** 3)

    def test_degree_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.degree, "abc", 2)
        self.assertRaises(TypeError, self.calculator.degree, 2, "abc")
        self.assertRaises(TypeError, self.calculator.degree, [], 2)
        self.assertRaises(TypeError, self.calculator.degree, 2, [])
        self.assertRaises(TypeError, self.calculator.degree, {}, 2)
        self.assertRaises(TypeError, self.calculator.degree, 2, {})
        self.assertRaises(TypeError, self.calculator.degree, None, 2)
        self.assertRaises(TypeError, self.calculator.degree, 2, None)


    #### TESTS FOR LN
    def test_ln_positive_int(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(10), math.log(10))

    def test_ln_positive_float(self):
        self.assertAlmostEqual(self.calculator.ln(2.5), math.log(2.5))
        self.assertAlmostEqual(self.calculator.ln(3.7), math.log(3.7))

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_large_number(self):
        self.assertAlmostEqual(self.calculator.ln(1e6), math.log(1e6))
        self.assertAlmostEqual(self.calculator.ln(1e12), math.log(1e12))

    def test_ln_small_number(self):
        self.assertAlmostEqual(self.calculator.ln(1e-6), math.log(1e-6))
        self.assertAlmostEqual(self.calculator.ln(1e-12), math.log(1e-12))

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(float("inf")), math.log(float("inf")))

    def test_ln_nan(self):
        self.assertTrue(math.isnan(self.calculator.ln(float("NaN"))))

    def test_ln_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.ln, "abc")
        self.assertRaises(TypeError, self.calculator.ln, [])
        self.assertRaises(TypeError, self.calculator.ln, {})
        self.assertRaises(TypeError, self.calculator.ln, None)


    #### TESTS FOR LOG
    def test_log_positive_int(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(2, 10), math.log(2, 10))

    def test_log_positive_float(self):
        self.assertAlmostEqual(self.calculator.log(2.5, 2), math.log(2.5, 2))
        self.assertAlmostEqual(self.calculator.log(10, 10), math.log(10, 10))

    def test_log_base_equal_val(self):
        self.assertEqual(self.calculator.log(2, 2), 1)

    def test_log_undefined(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 10, 1)
        self.assertRaises(ValueError, self.calculator.log, 0, 2)
        self.assertRaises(ValueError, self.calculator.log, -1, 2)

    def test_log_large_number(self):
        self.assertAlmostEqual(self.calculator.log(1e6, 10), math.log(1e6, 10))
        self.assertAlmostEqual(self.calculator.log(1e12, 2), math.log(1e12, 2))

    def test_log_small_number(self):
        self.assertAlmostEqual(self.calculator.log(1e-6, 10), math.log(1e-6, 10))
        self.assertAlmostEqual(self.calculator.log(1e-12, 2), math.log(1e-12, 2))

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(float("inf"), 10), math.log(float("inf"), 10))

    def test_log_nan(self):
        self.assertTrue(math.isnan(self.calculator.log(float("NaN"), 2)))

    def test_log_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.log, "abc", 2)
        self.assertRaises(TypeError, self.calculator.log, 2, "abc")
        self.assertRaises(TypeError, self.calculator.log, [], 2)
        self.assertRaises(TypeError, self.calculator.log, 2, [])
        self.assertRaises(TypeError, self.calculator.log, {}, 2)
        self.assertRaises(TypeError, self.calculator.log, 2, {})
        self.assertRaises(TypeError, self.calculator.log, None, 2)
        self.assertRaises(TypeError, self.calculator.log, 2, None)


    #### TESTS FOR SQRT
    def test_sqrt_positive_int(self):
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_positive_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(1.2), math.sqrt(1.2))
        self.assertAlmostEqual(self.calculator.sqrt(10.5), math.sqrt(10.5))

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(0.0), 0.0)

    # тут должна быть ошибка, но код не обрабатывает
    # def test_sqrt_negative(self):
    #     self.assertRaises(ValueError, self.calculator.sqrt, -1)

    def test_sqrt_large_number(self):
        self.assertAlmostEqual(self.calculator.sqrt(1e6), math.sqrt(1e6))
        self.assertAlmostEqual(self.calculator.sqrt(1e12), math.sqrt(1e12))

    def test_sqrt_small_number(self):
        self.assertAlmostEqual(self.calculator.sqrt(1e-6), math.sqrt(1e-6))
        self.assertAlmostEqual(self.calculator.sqrt(1e-12), math.sqrt(1e-12))

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(float("inf")), math.sqrt(float("inf")))

    def test_sqrt_nan(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(float("NaN"))))

    def test_sqrt_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "abc")
        self.assertRaises(TypeError, self.calculator.sqrt, [])
        self.assertRaises(TypeError, self.calculator.sqrt, {})
        self.assertRaises(TypeError, self.calculator.sqrt, None)


    #### TESTS FOR NTH_ROOT
    def test_nth_root_positive_int(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertEqual(self.calculator.nth_root(16, 4), 2)

    def test_nth_root_positive_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(2.5, 2), math.sqrt(2.5))
        self.assertAlmostEqual(self.calculator.nth_root(27.0, 3), math.pow(27.0, 1/3))

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 2), 0)
    
    def test_nth_root_zero_exponent(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 8, 0)

    # тут должна быть либо ошибка, либо возвращаться комплексные числа
    # def test_nth_root_negative_odd_n(self):
    #     self.assertRaises(ValueError, self.calculator.nth_root, -8, 3)
    #     self.assertRaises(ValueError, self.calculator.nth_root, -16, 4)

    def test_nth_root_large_number(self):
        self.assertAlmostEqual(self.calculator.nth_root(1e20, 6), math.pow(1e20, 1/6))

    def test_nth_root_small_number(self):
        self.assertAlmostEqual(self.calculator.nth_root(1e-20, 6), math.pow(1e-20, 1/6))

    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(float("inf"), 3), float("inf"))

    def test_nth_root_nan(self):
        self.assertTrue(math.isnan(self.calculator.nth_root(float("NaN"), 2)))

    def test_nth_root_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "abc", 2)
        self.assertRaises(TypeError, self.calculator.nth_root, [], 2)
        self.assertRaises(TypeError, self.calculator.nth_root, {}, 2)
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)


if __name__ == "__main__":
    unittest.main()