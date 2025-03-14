import unittest
from calculator import Calculator
import math


class TestCalculatorAddition(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_addition_int_two_positives(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_addition_int_two_negatives(self):
        self.assertEqual(self.calculator.addition(-6, -3), -9)
    
    def test_addition_int_two_zeros(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)
    
    def test_addition_int_zero_and_positive(self):
        self.assertEqual(self.calculator.addition(0, 3), 3)
    
    def test_addition_int_negative_and_zero(self):
        self.assertEqual(self.calculator.addition(-5, 0), -5)
    
    def test_addition_int_and_float(self):
        self.assertAlmostEqual(self.calculator.addition(2.5, 2), 4.5)
        self.assertAlmostEqual(self.calculator.addition(5, 2.1), 7.1)
    
    def test_addition_int_position(self):
        self.assertEqual(self.calculator.addition(52, 12), 64)
        self.assertEqual(self.calculator.addition(12, 52), 64)
    
    # Float

    def test_addition_float_two_positives(self):
        self.assertAlmostEqual(self.calculator.addition(10.3, 54.09), 64.39)
    
    def test_addition_float_two_negatives(self):
        self.assertAlmostEqual(self.calculator.addition(-4.8, -3.1), -7.9)
    
    def test_addition_float_two_zeros(self):
        self.assertAlmostEqual(self.calculator.addition(0.0, 0.0), 0.0)
    
    def test_addition_float_zero_and_positive(self):
        self.assertAlmostEqual(self.calculator.addition(0.0, 9.2), 9.2)
    
    def test_addition_float_negative_and_zero(self):
        self.assertAlmostEqual(self.calculator.addition(-5.8, 0.0), -5.8)
    
    def test_addition_float_position(self):
        self.assertAlmostEqual(self.calculator.addition(52.05, 12.09), 64.14)
        self.assertAlmostEqual(self.calculator.addition(12.09, 52.05), 64.14)
    
    # Inf

    def test_addition_inf_int(self):
        self.assertEqual(self.calculator.addition(float("inf"), 5), float("inf"))

    def test_addition_inf_float(self):
        self.assertEqual(self.calculator.addition(float("inf"), 5), float("inf"))
    
    def test_addition_inf_position(self):
        self.assertEqual(self.calculator.addition(float("inf"), 5), float("inf"))
        self.assertEqual(self.calculator.addition(1, float("inf")), float("inf")) 
    
    # NaN

    def test_addition_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.addition(float("NaN"), 2)))
    
    def test_addition_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.addition(float("NaN"), 2.3)))
    
    def test_addition_nan_position(self):
        self.assertTrue(math.isnan(self.calculator.addition(float("NaN"), 67.01)))
        self.assertTrue(math.isnan(self.calculator.addition(23.14, float("NaN"))))
    
    # Complex

    def test_addition_complex_two_positives(self):
        self.assertEqual(self.calculator.addition(1 + 1j, 1 + 1j), 2 + 2j)

    # TypeError

    def test_addition_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.addition, "foo", 15)
        self.assertRaises(TypeError, self.calculator.addition, "bar", 7.3)
        self.assertRaises(TypeError, self.calculator.addition, "bar", 1 + 1j)


class TestCalculatorMultiplication(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_multiplication_int_two_positives(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
    
    def test_multiplication_int_two_negatives(self):
        self.assertEqual(self.calculator.multiplication(-6, -3), 18)
    
    def test_multiplication_int_two_zeros(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
    
    def test_multiplication_int_zero_and_positive(self):
        self.assertEqual(self.calculator.multiplication(0, 3), 0)
    
    def test_multiplication_int_negative_and_zero(self):
        self.assertEqual(self.calculator.multiplication(-5, 0), 0)
    
    def test_multiplication_int_and_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calculator.multiplication(3, 4.1), 12.3)

    def test_multiplication_int_position(self):
        self.assertEqual(self.calculator.multiplication(5, 4), 20)
        self.assertEqual(self.calculator.multiplication(4, 5), 20)
    
    # Float

    def test_multiplication_float_two_positives(self):
        self.assertAlmostEqual(self.calculator.multiplication(10.3, 54.09), 10.3 * 54.09)
    
    def test_multiplication_float_two_negatives(self):
        self.assertAlmostEqual(self.calculator.multiplication(-4.8, -3.1), -4.8 * -3.1)
    
    def test_multiplication_float_two_zeros(self):
        self.assertAlmostEqual(self.calculator.multiplication(0.0, 0.0), 0.0)
    
    def test_multiplication_float_zero_and_positive(self):
        self.assertAlmostEqual(self.calculator.multiplication(0.0, 9.2), 0.0)
    
    def test_multiplication_float_negative_and_zero(self):
        self.assertAlmostEqual(self.calculator.multiplication(-5.8, 0.0), 0.0)
    
    def test_multiplication_float_position(self):
        self.assertAlmostEqual(self.calculator.multiplication(52.05, 12.09), 52.05 * 12.09)
        self.assertAlmostEqual(self.calculator.multiplication(12.09, 52.05), 12.09 * 52.05)
    
    # Inf

    def test_multiplication_inf_int(self):
        self.assertEqual(self.calculator.multiplication(float("inf"), 5), float("inf"))

    def test_multiplication_inf_float(self):
        self.assertEqual(self.calculator.multiplication(float("inf"), 5), float("inf"))
    
    def test_multiplication_inf_position(self):
        self.assertEqual(self.calculator.multiplication(float("inf"), 5), float("inf"))
        self.assertEqual(self.calculator.multiplication(1, float("inf")), float("inf")) 
    
    # NaN

    def test_multiplication_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(float("NaN"), 2)))
    
    def test_multiplication_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(float("NaN"), 2.3)))
    
    def test_multiplication_nan_position(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(float("NaN"), 67.01)))
        self.assertTrue(math.isnan(self.calculator.multiplication(23.14, float("NaN"))))
    
    # Complex

    def test_multiplication_complex_two_positives(self):
        self.assertEqual(self.calculator.multiplication(1 + 1j, 1 + 1j), 2j)

    # TypeError

    def test_multiplication_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "bar", 7.3)
        self.assertRaises(TypeError, self.calculator.multiplication, "bar", 1 + 1j)


class TestCalculatorSubtraction(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_subtraction_int_two_positives(self):
        self.assertEqual(self.calculator.subtraction(5, 2), 3)
        self.assertEqual(self.calculator.subtraction(2, 7), -5)
    
    def test_subtraction_int_two_negatives(self):
        self.assertEqual(self.calculator.subtraction(-6, -3), -3)
    
    def test_subtraction_int_two_zeros(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
    
    def test_subtraction_int_zero_and_positive(self):
        self.assertEqual(self.calculator.subtraction(0, 3), -3)
    
    def test_subtraction_int_negative_and_zero(self):
        self.assertEqual(self.calculator.subtraction(-5, 0), -5)
    
    def test_subtraction_int_and_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(2.5, 2), 0.5)
        self.assertAlmostEqual(self.calculator.subtraction(2, 2.5), -0.5)
    
    # Float

    def test_subtraction_float_two_positives(self):
        self.assertAlmostEqual(self.calculator.subtraction(10.3, 54.09), 10.3 - 54.09)
    
    def test_subtraction_float_two_negatives(self):
        self.assertAlmostEqual(self.calculator.subtraction(-4.8, -3.1), -4.8 - -3.1)
    
    def test_subtraction_float_two_zeros(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.0, 0.0), 0.0)
    
    def test_subtraction_float_zero_and_positive(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.0, 9.2), -9.2)
    
    def test_subtraction_float_negative_and_zero(self):
        self.assertAlmostEqual(self.calculator.subtraction(-5.8, 0.0), -5.8)
    
    # Inf

    def test_subtraction_inf_int(self):
        self.assertEqual(self.calculator.subtraction(float("inf"), 5), float("inf"))

    def test_subtraction_inf_float(self):
        self.assertEqual(self.calculator.subtraction(float("inf"), 5), float("inf"))
    
    def test_subtraction_inf_position(self):
        self.assertEqual(self.calculator.subtraction(float("inf"), 5), float("inf"))
        self.assertEqual(self.calculator.subtraction(1, float("inf")), float("-inf")) 
    
    # NaN

    def test_subtraction_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float("NaN"), 2)))
    
    def test_subtraction_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float("NaN"), 2.3)))
    
    def test_subtraction_nan_position(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float("NaN"), 67.01)))
        self.assertTrue(math.isnan(self.calculator.subtraction(23.14, float("NaN"))))
    
    # Complex

    def test_subtraction_complex_two_positives(self):
        self.assertEqual(self.calculator.subtraction(1 + 1j, 1 + 2j), -1j)

    # TypeError

    def test_subtraction_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "foo", 15)
        self.assertRaises(TypeError, self.calculator.subtraction, "bar", 7.3)
        self.assertRaises(TypeError, self.calculator.subtraction, "bar", 1 + 1j)


class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_division_int_two_positives(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertAlmostEqual(self.calculator.division(3, 2), 1.5)
    
    def test_division_int_two_negatives(self):
        self.assertEqual(self.calculator.division(-6, -3), 2)
    
    def test_division_int_two_zeros(self):
        self.assertIsNone(self.calculator.division(0, 0))
    
    def test_division_int_zero_and_positive(self):
        self.assertEqual(self.calculator.division(0, 3), 0)
    
    def test_division_int_negative_and_zero(self):
        self.assertIsNone(self.calculator.division(-5, 0))
    
    def test_division_int_and_float(self):
        self.assertAlmostEqual(self.calculator.division(2.5, 2), 1.25)
        self.assertAlmostEqual(self.calculator.division(2, 2.5), 2 / 2.5)
    
    # Float

    def test_division_float_two_positives(self):
        self.assertAlmostEqual(self.calculator.division(10.3, 54.09), 10.3 / 54.09)
    
    def test_division_float_two_negatives(self):
        self.assertAlmostEqual(self.calculator.division(-4.8, -3.1), -4.8 / -3.1)
    
    def test_division_float_two_zeros(self):
        self.assertIsNone(self.calculator.division(0.0, 0.0))
    
    def test_division_float_zero_and_positive(self):
        self.assertAlmostEqual(self.calculator.division(0.0, 9.2), 0.0)
    
    def test_division_float_negative_and_zero(self):
        self.assertIsNone(self.calculator.division(-5.8, 0.0))
    
    # Inf

    def test_division_inf_int(self):
        self.assertEqual(self.calculator.division(float("inf"), 5), float("inf"))

    def test_division_inf_float(self):
        self.assertEqual(self.calculator.division(float("inf"), 5), float("inf"))
    
    def test_division_inf_position(self):
        self.assertEqual(self.calculator.division(float("inf"), 5), float("inf"))
        self.assertAlmostEqual(self.calculator.division(1, float("inf")), 0.0) 
    
    # NaN

    def test_division_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.division(float("NaN"), 2)))
    
    def test_division_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.division(float("NaN"), 2.3)))
    
    def test_division_nan_position(self):
        self.assertTrue(math.isnan(self.calculator.division(float("NaN"), 67.01)))
        self.assertTrue(math.isnan(self.calculator.division(23.14, float("NaN"))))
    
    # Complex

    def test_division_complex_two_positives(self):
        self.assertEqual(self.calculator.division(5 + 4j, 2 + 3j), (5 + 4j) / (2 + 3j))

    # TypeError

    def test_division_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.division, "foo", 15)
        self.assertRaises(TypeError, self.calculator.division, "bar", 7.3)
        self.assertRaises(TypeError, self.calculator.division, "bar", 1 + 1j)


class TestCalculatorAbsolute(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer
    
    def test_absolute_int_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)
    
    def test_absolute_int_negative(self):
        self.assertEqual(self.calculator.absolute(-16), 16)

    # Float

    def test_absolute_float_positive(self):
        self.assertAlmostEqual(self.calculator.absolute(51.401), 51.401)
    
    def test_absolute_float_negative(self):
        self.assertAlmostEqual(self.calculator.absolute(-3.52), 3.52)
    
    # Inf

    def test_absolute_inf(self):
        self.assertEqual(self.calculator.absolute(float("inf")), float("inf"))
    
    def test_absolute_inf_negative(self):
        self.assertEqual(self.calculator.absolute(float("-inf")), float("inf"))
    
    # NaN

    def test_absolute_nan(self):
        self.assertTrue(math.isnan(self.calculator.absolute(float("NaN"))))

    # Complex

    def test_absolute_complex_two(self):
        self.assertAlmostEqual(self.calculator.absolute(1 + 1j), abs(1 + 1j))

    # TypeError

    def test_absolute_typeerror_str(self):
        self.assertRaises(TypeError, self.calculator.absolute, "foo")
    
    def test_absolute_typeerror_list(self):
        self.assertRaises(TypeError, self.calculator.absolute, ["a", "b", "c"])

    def test_absolute_typeerror_tuple(self):
        self.assertRaises(TypeError, self.calculator.absolute, (1, 2, 3))


class TestCalculatorDegree(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_degree_int_two_positives(self):
        self.assertEqual(self.calculator.degree(3, 4), 81)
    
    def test_degree_int_two_negatives(self):
        self.assertAlmostEqual(self.calculator.degree(-6, -3), -6 ** -3)
    
    def test_degree_int_two_zeros(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)
    
    def test_degree_int_zero_and_positive(self):
        self.assertEqual(self.calculator.degree(0, 3), 0)
    
    def test_degree_int_negative_and_zero(self):
        self.assertEqual(self.calculator.degree(-5, 0), 1)
    
    def test_degree_int_and_float(self):
        self.assertAlmostEqual(self.calculator.degree(2.5, 2), 6.25)
        self.assertAlmostEqual(self.calculator.degree(5, 4.63), 5 ** 4.63)
    
    # Float

    def test_degree_float_two_positives(self):
        self.assertAlmostEqual(self.calculator.degree(10.3, 54.09), 10.3 ** 54.09)
    
    def test_degree_float_two_negatives(self):
        self.assertAlmostEqual(self.calculator.degree(-4.8, -3.1), (-4.8) ** (-3.1))
    
    def test_degree_float_two_zeros(self):
        self.assertAlmostEqual(self.calculator.degree(0.0, 0.0), 1.0)
    
    def test_degree_float_zero_and_positive(self):
        self.assertAlmostEqual(self.calculator.degree(0.0, 9.2), 0.0)
    
    def test_degree_float_negative_and_zero(self):
        self.assertAlmostEqual(self.calculator.degree(-5.8, 0.0), 1.0)
    
    # Inf

    def test_degree_inf_int(self):
        self.assertEqual(self.calculator.degree(float("inf"), 5), float("inf"))

    def test_degree_inf_float(self):
        self.assertEqual(self.calculator.degree(float("inf"), 5), float("inf"))
    
    # NaN

    def test_degree_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.degree(float("NaN"), 2)))
    
    def test_degree_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.degree(float("NaN"), 2.3)))
    
    def test_degree_nan_position(self):
        self.assertTrue(math.isnan(self.calculator.degree(float("NaN"), 67.01)))
        self.assertTrue(math.isnan(self.calculator.degree(23.14, float("NaN"))))
    
    # Complex

    def test_degree_complex_two_positives(self):
        self.assertEqual(self.calculator.degree(3 + 2j, 4 + 1j), (3 + 2j) ** (4 + 1j))

    # TypeError

    def test_degree_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.degree, "foo", 15)
        self.assertRaises(TypeError, self.calculator.degree, "bar", 7.3)
        self.assertRaises(TypeError, self.calculator.degree, "bar", 1 + 1j)


class TestCalculatorLn(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_ln_int_positive(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0.0)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1.0)
        self.assertAlmostEqual(self.calculator.ln(5), math.log(5))

    
    def test_ln_int_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -6)
    
    def test_ln_int_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)
    
    # Float
    
    def test_ln_float_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -4.3)

    # Inf

    def test_ln_inf_positive(self):
        self.assertEqual(self.calculator.ln(float("inf")), float("inf"))

    def test_ln_inf_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, float("-inf")) 
    
    # NaN

    def test_ln_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.ln(float("NaN"))))

    # TypeError

    def test_ln_typeerror_str(self):
        self.assertRaises(TypeError, self.calculator.ln, "foo")
    
    def test_ln_typeerror_list(self):
        self.assertRaises(TypeError, self.calculator.ln, ["a", "b", "c"])
    
    def test_ln_typeerror_tuple(self):
        self.assertRaises(TypeError, self.calculator.ln, (1, 2, 3))
    
    def test_ln_typeerror_complex(self):
        self.assertRaises(TypeError, self.calculator.ln, 2 + 3j)


class TestCalculatorLog(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    
    def test_log_int_low_base(self):
        self.assertAlmostEqual(self.calculator.log(2, 0.5), -1.0)
    
    def test_log_int_high_base(self):
        self.assertAlmostEqual(self.calculator.log(16, 2), 4.0)
        self.assertAlmostEqual(self.calculator.log(27, 3), 3.0)
    
    def test_log_int_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, -3, -10)
        self.assertRaises(ValueError, self.calculator.log, 5, -10)

    def test_log_int_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 5, 0)

    def test_log_int_single_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1, 1)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 4, 1)

    def test_log_int_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -30, 10)
        self.assertRaises(ValueError, self.calculator.log, -5, -5)

    # Float
    
    def test_log_float_low_base(self):
        self.assertAlmostEqual(self.calculator.log(2, 0.5), -1.0)
    
    def test_log_float_high_base(self):
        self.assertAlmostEqual(self.calculator.log(0.2, 5), -1.0)
        self.assertAlmostEqual(self.calculator.log(0.25, 4), -1.0)
    
    def test_log_float_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, -3.7, -10.4)
        self.assertRaises(ValueError, self.calculator.log, 5.3, -10.9)

    def test_log_float_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 5.2, 0.0)

    def test_log_float_single_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1.5, 1.0)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 4.32, 1.0)

    def test_log_float_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -30.1, 10.4)
        self.assertRaises(ValueError, self.calculator.log, -5.1, -5.4)

    # Inf

    def test_log_inf_positive(self):
        self.assertEqual(self.calculator.log(float("inf"), 3.14), float("inf"))
    
    # NaN

    def test_log_nan_int(self):
        self.assertTrue(math.isnan(self.calculator.log(float("NaN"), 4.15)))

    # TypeError

    def test_log_typeerror_str(self):
        self.assertRaises(TypeError, self.calculator.log, "foo", 6)
    
    def test_log_typeerror_list(self):
        self.assertRaises(TypeError, self.calculator.log, ["a", "b", "c"], 3)
    
    def test_log_typeerror_tuple(self):
        self.assertRaises(TypeError, self.calculator.log, (1, 2, 3), 8)
    
    def test_log_typeerror_complex(self):
        self.assertRaises(TypeError, self.calculator.log, 2 + 3j, 3)


class TestCalculatorSqrt(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_sqrt_int_positive(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(81), 9)
    
    def test_sqrt_int_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-6), (-6) ** 0.5)
        self.assertAlmostEqual(self.calculator.sqrt(-41), (-41) ** 0.5)
    
    def test_sqrt_int_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
    
    # Float

    def test_sqrt_float_positive(self):
        self.assertAlmostEqual(self.calculator.sqrt(6.25), 2.5)
        self.assertAlmostEqual(self.calculator.sqrt(42.25), 6.5)
    
    def test_sqrt_float_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-3.63), (-3.63) ** 0.5)
        self.assertAlmostEqual(self.calculator.sqrt(-41.25), (-41.25) ** 0.5)
    
    # Inf

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(float("inf")), float("inf"))

    # NaN

    def test_sqrt_nan(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(float("NaN"))))
    
    # Complex

    def test_sqrt_complex(self):
        self.assertAlmostEqual(self.calculator.sqrt(4 + 3j), (4 + 3j) ** 0.5)

    # TypeError

    def test_sqrt_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "foo")
        self.assertRaises(TypeError, self.calculator.sqrt, ["a", "b", "c"])
        self.assertRaises(TypeError, self.calculator.sqrt, (1, 2, 3))


class TestCalculatorNthRoot(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Integer

    def test_nthroot_int_positive(self):
        self.assertEqual(self.calculator.nth_root(16, 2), 4)
        self.assertEqual(self.calculator.nth_root(81, 4), 3)
    
    def test_nthroot_int_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 5), 0)
    
    # Inf

    def test_nthroot_inf(self):
        self.assertEqual(self.calculator.nth_root(float("inf"), 5), float("inf"))
        self.assertEqual(self.calculator.nth_root(54, float("inf")), 1.0)

    # NaN

    def test_nthroot_nan(self):
        self.assertTrue(math.isnan(self.calculator.nth_root(float("NaN"), 63)))
        self.assertTrue(math.isnan(self.calculator.nth_root(23, float("NaN"))))

    # TypeError

    def test_nthroot_typeerror_str_and_numeric(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "foo", 16)
        self.assertRaises(TypeError, self.calculator.nth_root, 5.32, ["a", "b", "c"])
        self.assertRaises(TypeError, self.calculator.nth_root, (1, 2, 3), 4)


if __name__ == "__main__":
    unittest.main()
