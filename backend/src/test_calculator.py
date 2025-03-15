import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    # Тесты для addition
    def test_addition_positive(self):
        """Проверка сложения двух положительных чисел."""
        self.assertEqual(self.calculator.addition(3, 5), 8)

    def test_addition_negative(self):
        """Проверка сложения двух отрицательных чисел."""
        self.assertEqual(self.calculator.addition(-3, -5), -8)

    def test_addition_mixed(self):
        """Проверка сложения положительного и отрицательного числа."""
        self.assertEqual(self.calculator.addition(3, -5), -2)

    def test_addition_zero(self):
        """Проверка сложения с нулем."""
        self.assertEqual(self.calculator.addition(0, 5), 5)
        self.assertEqual(self.calculator.addition(3, 0), 3)

    def test_addition_positive_floats(self):
        """Проверка сложения двух положительных дробных чисел."""
        self.assertEqual(self.calculator.addition(3.5, 2.7), 6.2)

    def test_addition_negative_floats(self):
        """Проверка сложения двух отрицательных дробных чисел."""
        self.assertEqual(self.calculator.addition(-1.2, -3.4), -4.6)

    def test_addition_mixed_floats(self):
        """Проверка сложения положительного и отрицательного дробного числа."""
        self.assertEqual(self.calculator.addition(2.5, -1.5), 1.0)

    def test_addition_int_and_float(self):
        """Проверка сложения целого числа и дробного."""
        self.assertEqual(self.calculator.addition(3, 2.5), 5.5)
        self.assertEqual(self.calculator.addition(2.5, 3), 5.5)

    def test_addition_large_integers(self):
        """Проверка сложения больших целых чисел."""
        self.assertEqual(self.calculator.addition(10 ** 10, 10 ** 10), 2 * 10 ** 10)

    def test_addition_large_floats(self):
        """Проверка сложения больших дробных чисел."""
        self.assertEqual(self.calculator.addition(1.5e10, 2.5e10), 4.0e10)

    def test_addition_with_string(self):
        """Проверка сложения с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.addition("3", 5)
        with self.assertRaises(TypeError):
            self.calculator.addition(3, "5")

    def test_addition_with_none(self):
        """Проверка сложения с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.addition(None, 5)
        with self.assertRaises(TypeError):
            self.calculator.addition(3, None)

    def test_addition_with_list(self):
        """Проверка сложения с передачей списка."""
        with self.assertRaises(TypeError):
            self.calculator.addition([1, 2], 3)
        with self.assertRaises(TypeError):
            self.calculator.addition(3, [1, 2])

    def test_addition_with_infinity(self):
        """Проверка сложения с бесконечностью."""
        self.assertEqual(self.calculator.addition(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, -5), -math.inf)

    def test_addition_with_nan(self):
        """Проверка сложения с NaN."""
        result = self.calculator.addition(math.nan, 5)
        self.assertTrue(math.isnan(result))

    def test_addition_small_floats(self):
        """Проверка сложения очень малых чисел."""
        self.assertAlmostEqual(self.calculator.addition(1e-10, 2e-10), 3e-10)

    # Тесты для multiplication
    def test_multiplication_positive(self):
        """Проверка умножения двух положительных чисел."""
        self.assertEqual(self.calculator.multiplication(3, 5), 15)

    def test_multiplication_negative(self):
        """Проверка умножения двух отрицательных чисел."""
        self.assertEqual(self.calculator.multiplication(-3, -5), 15)

    def test_multiplication_mixed(self):
        """Проверка умножения положительного на отрицательное."""
        self.assertEqual(self.calculator.multiplication(3, -5), -15)

    def test_multiplication_zero(self):
        """Проверка умножения на ноль."""
        self.assertEqual(self.calculator.multiplication(0, 5), 0)
        self.assertEqual(self.calculator.multiplication(3, 0), 0)

    def test_multiplication_positive_floats(self):
        """Проверка умножения двух положительных дробных чисел."""
        self.assertEqual(self.calculator.multiplication(2.5, 4.0), 10.0)

    def test_multiplication_negative_floats(self):
        """Проверка умножения двух отрицательных дробных чисел."""
        self.assertEqual(self.calculator.multiplication(-2.5, -4.0), 10.0)

    def test_multiplication_mixed_floats(self):
        """Проверка умножения положительного и отрицательного дробного числа."""
        self.assertEqual(self.calculator.multiplication(2.5, -4.0), -10.0)

    def test_multiplication_int_and_float(self):
        """Проверка умножения целого числа и дробного."""
        self.assertEqual(self.calculator.multiplication(3, 2.5), 7.5)
        self.assertEqual(self.calculator.multiplication(2.5, 3), 7.5)

    def test_multiplication_large_integers(self):
        """Проверка умножения больших целых чисел."""
        self.assertEqual(self.calculator.multiplication(10 ** 10, 10 ** 10), 10 ** 20)

    def test_multiplication_large_floats(self):
        """Проверка умножения больших дробных чисел."""
        self.assertEqual(self.calculator.multiplication(1.5e10, 2.0e10), 3.0e20)

    def test_multiplication_with_string(self):
        """Проверка умножения с передачей строки."""
        self.assertEqual(self.calculator.multiplication("3", 5), "33333")

    def test_multiplication_with_none(self):
        """Проверка умножения с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, 5)
        with self.assertRaises(TypeError):
            self.calculator.multiplication(3, None)

    def test_multiplication_with_list(self):
        """Проверка умножения с передачей списка."""
        self.assertEqual(self.calculator.multiplication([1, 2], 3), [1, 2, 1, 2, 1, 2])

    def test_multiplication_with_infinity(self):
        """Проверка умножения на бесконечность."""
        self.assertEqual(self.calculator.multiplication(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, 5), -math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -5), -math.inf)

    def test_multiplication_with_nan(self):
        """Проверка умножения на NaN."""
        result = self.calculator.multiplication(math.nan, 5)
        self.assertTrue(math.isnan(result))

    def test_multiplication_zero_and_infinity(self):
        """Проверка умножения нуля на бесконечность."""
        result = self.calculator.multiplication(0, math.inf)
        self.assertTrue(math.isnan(result))

    def test_multiplication_small_floats(self):
        """Проверка умножения очень малых чисел."""
        self.assertAlmostEqual(self.calculator.multiplication(1e-10, 2e-10), 2e-20)

    def test_multiplication_by_one(self):
        """Проверка умножения на единицу."""
        self.assertEqual(self.calculator.multiplication(5, 1), 5)
        self.assertEqual(self.calculator.multiplication(-5, 1), -5)
        self.assertEqual(self.calculator.multiplication(0, 1), 0)

    # Тесты для subtraction
    def test_subtraction_positive(self):
        """Проверка вычитания положительных чисел."""
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtraction_negative(self):
        """Проверка вычитания отрицательных чисел."""
        self.assertEqual(self.calculator.subtraction(-5, -3), -2)

    def test_subtraction_mixed(self):
        """Проверка вычитания с разными знаками."""
        self.assertEqual(self.calculator.subtraction(5, -3), 8)

    def test_subtraction_zero(self):
        """Проверка вычитания с нулем."""
        self.assertEqual(self.calculator.subtraction(0, 5), -5)
        self.assertEqual(self.calculator.subtraction(3, 0), 3)

    def test_subtraction_positive_floats(self):
        """Проверка вычитания двух положительных дробных чисел."""
        self.assertEqual(self.calculator.subtraction(4.5, 2.3), 2.2)

    def test_subtraction_negative_floats(self):
        """Проверка вычитания двух отрицательных дробных чисел."""
        self.assertEqual(self.calculator.subtraction(-4.5, -2.3), -2.2)

    def test_subtraction_mixed_floats(self):
        """Проверка вычитания положительного и отрицательного дробного числа."""
        self.assertEqual(self.calculator.subtraction(4.5, -2.3), 6.8)

    def test_subtraction_int_and_float(self):
        """Проверка вычитания целого числа и дробного."""
        self.assertEqual(self.calculator.subtraction(5, 2.5), 2.5)
        self.assertEqual(self.calculator.subtraction(2.5, 3), -0.5)

    def test_subtraction_large_integers(self):
        """Проверка вычитания больших целых чисел."""
        self.assertEqual(self.calculator.subtraction(10 ** 10, 10 ** 9), 9 * 10 ** 9)

    def test_subtraction_large_floats(self):
        """Проверка вычитания больших дробных чисел."""
        self.assertEqual(self.calculator.subtraction(1.5e10, 0.5e10), 1.0e10)

    def test_subtraction_with_string(self):
        """Проверка вычитания с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.subtraction("5", 3)
        with self.assertRaises(TypeError):
            self.calculator.subtraction(5, "3")

    def test_subtraction_with_none(self):
        """Проверка вычитания с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, 5)
        with self.assertRaises(TypeError):
            self.calculator.subtraction(3, None)

    def test_subtraction_with_list(self):
        """Проверка вычитания с передачей списка."""
        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2], 3)
        with self.assertRaises(TypeError):
            self.calculator.subtraction(3, [1, 2])

    def test_subtraction_with_infinity(self):
        """Проверка вычитания с бесконечностью."""
        self.assertEqual(self.calculator.subtraction(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.subtraction(5, math.inf), -math.inf)
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

    def test_subtraction_with_nan(self):
        """Проверка вычитания с NaN."""
        result = self.calculator.subtraction(math.nan, 5)
        self.assertTrue(math.isnan(result))
        result = self.calculator.subtraction(5, math.nan)
        self.assertTrue(math.isnan(result))

    def test_subtraction_small_floats(self):
        """Проверка вычитания очень малых чисел."""
        self.assertAlmostEqual(self.calculator.subtraction(1e-10, 2e-10), -1e-10)

    def test_subtraction_self(self):
        """Проверка вычитания числа из самого себя."""
        self.assertEqual(self.calculator.subtraction(5, 5), 0)
        self.assertEqual(self.calculator.subtraction(-5, -5), 0)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    # Тесты для division
    def test_division_positive(self):
        """Проверка деления положительных чисел."""
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_division_negative(self):
        """Проверка деления отрицательных чисел."""
        self.assertEqual(self.calculator.division(-10, -2), 5)

    def test_division_mixed(self):
        """Проверка деления с разными знаками."""
        self.assertEqual(self.calculator.division(10, -2), -5)

    def test_division_by_zero(self):
        """Проверка деления на ноль (должен вернуть None)."""
        self.assertIsNone(self.calculator.division(10, 0))

    def test_division_zero_by_number(self):
        """Проверка деления нуля на число."""
        self.assertEqual(self.calculator.division(0, 5), 0)

    def test_division_positive_floats(self):
        """Проверка деления двух положительных дробных чисел."""
        self.assertEqual(self.calculator.division(4.5, 1.5), 3.0)

    def test_division_negative_floats(self):
        """Проверка деления двух отрицательных дробных чисел."""
        self.assertEqual(self.calculator.division(-4.5, -1.5), 3.0)

    def test_division_mixed_floats(self):
        """Проверка деления положительного и отрицательного дробного числа."""
        self.assertEqual(self.calculator.division(4.5, -1.5), -3.0)

    def test_division_int_and_float(self):
        """Проверка деления целого числа и дробного."""
        self.assertEqual(self.calculator.division(5, 2.0), 2.5)
        self.assertEqual(self.calculator.division(5.0, 2), 2.5)

    def test_division_large_integers(self):
        """Проверка деления больших целых чисел."""
        self.assertEqual(self.calculator.division(10 ** 10, 10 ** 5), 10 ** 5)

    def test_division_large_floats(self):
        """Проверка деления больших дробных чисел."""
        self.assertEqual(self.calculator.division(1.5e10, 5.0e5), 3.0e4)

    def test_division_small_floats(self):
        """Проверка деления очень малых чисел."""
        self.assertAlmostEqual(self.calculator.division(1e-10, 2e-10), 0.5)

    def test_division_by_small_number(self):
        """Проверка деления на очень малое число."""
        self.assertAlmostEqual(self.calculator.division(1, 1e-10), 1e10)

    def test_division_with_string(self):
        """Проверка деления с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.division("5", 2)
        with self.assertRaises(TypeError):
            self.calculator.division(5, "2")

    def test_division_with_none(self):
        """Проверка деления с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.division(None, 5)
        with self.assertRaises(TypeError):
            self.calculator.division(5, None)

    def test_division_with_list(self):
        """Проверка деления с передачей списка."""
        with self.assertRaises(TypeError):
            self.calculator.division([1, 2], 3)
        with self.assertRaises(TypeError):
            self.calculator.division(3, [1, 2])

    def test_division_with_infinity(self):
        """Проверка деления с бесконечностью."""
        self.assertEqual(self.calculator.division(5, math.inf), 0.0)
        self.assertEqual(self.calculator.division(5, -math.inf), -0.0)
        self.assertEqual(self.calculator.division(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 5), -math.inf)

    def test_division_infinity_by_infinity(self):
        """Проверка деления бесконечности на бесконечность."""
        result = self.calculator.division(math.inf, math.inf)
        self.assertTrue(math.isnan(result))

    def test_division_with_nan(self):
        """Проверка деления с NaN."""
        result = self.calculator.division(math.nan, 5)
        self.assertTrue(math.isnan(result))
        result = self.calculator.division(5, math.nan)
        self.assertTrue(math.isnan(result))

    def test_division_zero_by_zero(self):
        """Проверка деления нуля на ноль."""
        self.assertIsNone(self.calculator.division(0, 0))

    # Тесты для absolute
    def test_absolute_positive(self):
        """Проверка модуля положительного числа."""
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_negative(self):
        """Проверка модуля отрицательного числа."""
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_absolute_zero(self):
        """Проверка модуля нуля."""
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_positive_float(self):
        """Проверка модуля положительного дробного числа."""
        self.assertEqual(self.calculator.absolute(3.14), 3.14)

    def test_absolute_negative_float(self):
        """Проверка модуля отрицательного дробного числа."""
        self.assertEqual(self.calculator.absolute(-3.14), 3.14)

    def test_absolute_large_integer(self):
        """Проверка модуля большого целого числа."""
        self.assertEqual(self.calculator.absolute(10 ** 10), 10 ** 10)

    def test_absolute_large_float(self):
        """Проверка модуля большого дробного числа."""
        self.assertEqual(self.calculator.absolute(-1.5e10), 1.5e10)

    def test_absolute_small_float(self):
        """Проверка модуля очень малого числа."""
        self.assertEqual(self.calculator.absolute(1e-10), 1e-10)
        self.assertEqual(self.calculator.absolute(-1e-10), 1e-10)

    def test_absolute_with_string(self):
        """Проверка модуля с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.absolute("5")

    def test_absolute_with_none(self):
        """Проверка модуля с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.absolute(None)

    def test_absolute_with_list(self):
        """Проверка модуля с передачей списка."""
        with self.assertRaises(TypeError):
            self.calculator.absolute([1, 2, 3])

    def test_absolute_infinity(self):
        """Проверка модуля бесконечности."""
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    def test_absolute_nan(self):
        """Проверка модуля NaN."""
        result = self.calculator.absolute(math.nan)
        self.assertTrue(math.isnan(result))

    # Тесты для degree
    def test_degree_positive(self):
        """Проверка возведения в степень с положительными числами."""
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_negative_base(self):
        """Проверка возведения отрицательного числа в степень."""
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_zero_base(self):
        """Проверка возведения нуля в степень."""
        self.assertEqual(self.calculator.degree(0, 3), 0)

    def test_degree_zero_exponent(self):
        """Проверка возведения в нулевую степень."""
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree_fractional_exponent(self):
        """Проверка возведения в дробную степень."""
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_negative_exponent(self):
        """Проверка возведения в отрицательную степень."""
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.degree(2, -2), 0.25)

    def test_degree_negative_base_fractional_exponent(self):
        """Проверка возведения отрицательного числа в дробную степень."""
        result = self.calculator.degree(-4, 0.5)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result, 2j)

    def test_degree_float_exponent(self):
        """Проверка возведения в степень с плавающей запятой."""
        self.assertAlmostEqual(self.calculator.degree(2, 1.5), 2 ** 1.5)

    def test_degree_large_values(self):
        """Проверка возведения больших чисел в степень."""
        self.assertEqual(self.calculator.degree(10, 10), 10 ** 10)
        self.assertAlmostEqual(self.calculator.degree(1.5, 10), 1.5 ** 10)

    def test_degree_small_base(self):
        """Проверка возведения малых оснований в степень."""
        self.assertAlmostEqual(self.calculator.degree(0.1, 2), 0.01)
        self.assertAlmostEqual(self.calculator.degree(0.1, -2), 100.0)

    def test_degree_with_string(self):
        """Проверка возведения с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.degree("2", 3)
        with self.assertRaises(TypeError):
            self.calculator.degree(2, "3")

    def test_degree_with_none(self):
        """Проверка возведения с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.degree(None, 3)
        with self.assertRaises(TypeError):
            self.calculator.degree(2, None)

    def test_degree_infinity(self):
        """Проверка возведения с бесконечностью."""
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, 3), -math.inf)
        self.assertEqual(self.calculator.degree(2, math.inf), math.inf)
        self.assertEqual(self.calculator.degree(0.5, math.inf), 0.0)

    def test_degree_nan(self):
        """Проверка возведения с NaN."""
        result = self.calculator.degree(math.nan, 2)
        self.assertTrue(math.isnan(result))
        result = self.calculator.degree(2, math.nan)
        self.assertTrue(math.isnan(result))

    def test_degree_zero_to_negative_exponent(self):
        """Проверка возведения нуля в отрицательную степень."""
        with self.assertRaises(ZeroDivisionError):
            self.calculator.degree(0, -1)

    # Тесты для ln
    def test_ln_positive(self):
        """Проверка натурального логарифма положительного числа."""
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(2), math.log(2))

    def test_ln_one(self):
        """Проверка ln(1), должен быть 0."""
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_negative(self):
        """Проверка ln отрицательного числа (должен выбросить исключение)."""
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)
        with self.assertRaises(ValueError):
            self.calculator.ln(-math.e)

    def test_ln_zero(self):
        """Проверка ln(0) (должен выбросить исключение)."""
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_ln_small_positive(self):
        """Проверка ln очень малого положительного числа."""
        self.assertAlmostEqual(self.calculator.ln(0.001), math.log(0.001))
        self.assertTrue(self.calculator.ln(1e-10) < 0)

    def test_ln_large_positive(self):
        """Проверка ln очень большого положительного числа."""
        self.assertAlmostEqual(self.calculator.ln(1e10), math.log(1e10))
        self.assertTrue(self.calculator.ln(1e100) > 0)

    def test_ln_fraction(self):
        """Проверка ln дробного числа между 0 и 1."""
        self.assertAlmostEqual(self.calculator.ln(0.5), math.log(0.5))
        self.assertTrue(self.calculator.ln(0.5) < 0)

    def test_ln_with_string(self):
        """Проверка ln с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.ln("2")

    def test_ln_with_none(self):
        """Проверка ln с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.ln(None)

    def test_ln_infinity(self):
        """Проверка ln с бесконечностью."""
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        with self.assertRaises(ValueError):
            self.calculator.ln(-math.inf)

    def test_ln_nan(self):
        """Проверка ln с NaN."""
        result = self.calculator.ln(math.nan)
        self.assertTrue(math.isnan(result))

    # Тесты для log
    def test_log_positive(self):
        """Проверка логарифма с положительными x и основанием."""
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_one(self):
        """Проверка log(1) по любому основанию (должен быть 0)."""
        self.assertEqual(self.calculator.log(1, 2), 0)

    def test_log_negative_x(self):
        """Проверка log с отрицательным x (должен выбросить исключение)."""
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_log_negative_n(self):
        """Проверка log с отрицательным основанием (должен выбросить исключение)."""
        with self.assertRaises(ValueError):
            self.calculator.log(2, -1)

    def test_log_n_one(self):
        """Проверка log с основанием 1 (должен выбросить исключение)."""
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(2, 1)

    def test_log_x_zero(self):
        """Проверка log(0) по любому основанию (должен выбросить исключение)."""
        with self.assertRaises(ValueError):
            self.calculator.log(0, 2)
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)

    def test_log_n_zero(self):
        """Проверка log с основанием 0 (должен выбросить исключение)."""
        with self.assertRaises(ValueError):
            self.calculator.log(2, 0)
        with self.assertRaises(ValueError):
            self.calculator.log(10, 0)

    def test_log_fractional(self):
        """Проверка log с дробными x и n."""
        self.assertAlmostEqual(self.calculator.log(0.5, 2), math.log(0.5, 2))
        self.assertAlmostEqual(self.calculator.log(4, 0.5), math.log(4, 0.5))

    def test_log_large_values(self):
        """Проверка log с большими x и n."""
        self.assertAlmostEqual(self.calculator.log(1e10, 10), 10)
        self.assertAlmostEqual(self.calculator.log(1e100, 10), 100)

    def test_log_small_values(self):
        """Проверка log с малыми x и n."""
        self.assertAlmostEqual(self.calculator.log(1e-10, 10), -10)
        self.assertAlmostEqual(self.calculator.log(0.1, 10), -1)

    def test_log_with_string(self):
        """Проверка log с передачей строк."""
        with self.assertRaises(TypeError):
            self.calculator.log("2", 3)
        with self.assertRaises(TypeError):
            self.calculator.log(2, "3")

    def test_log_with_none(self):
        """Проверка log с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.log(None, 3)
        with self.assertRaises(TypeError):
            self.calculator.log(2, None)

    def test_log_infinity(self):
        """Проверка log с бесконечностью."""
        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)
        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, 2)
        self.assertEqual(self.calculator.log(2, math.inf), 0.0)
        with self.assertRaises(ValueError):
            self.calculator.log(2, -math.inf)

    def test_log_nan(self):
        """Проверка log с NaN."""
        result = self.calculator.log(math.nan, 2)
        self.assertTrue(math.isnan(result))
        result = self.calculator.log(2, math.nan)
        self.assertTrue(math.isnan(result))

    # Тесты для sqrt
    def test_sqrt_positive(self):
        """Проверка квадратного корня из положительного числа."""
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_zero(self):
        """Проверка квадратного корня из нуля."""
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative(self):
        """Проверка квадратного корня из отрицательного числа (должен вернуть NaN)."""
        self.assertEqual(self.calculator.sqrt(-1), 6.123233995736766e-17+1j)

    def test_sqrt_one(self):
        """Проверка квадратного корня из 1."""
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_fractional(self):
        """Проверка квадратного корня из дробного числа."""
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5)
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2))

    def test_sqrt_large_value(self):
        """Проверка квадратного корня из большого числа."""
        self.assertAlmostEqual(self.calculator.sqrt(1e10), 1e5)

    def test_sqrt_small_value(self):
        """Проверка квадратного корня из малого положительного числа."""
        self.assertAlmostEqual(self.calculator.sqrt(1e-10), 1e-5)

    def test_sqrt_with_string(self):
        """Проверка sqrt с передачей строки."""
        with self.assertRaises(TypeError):
            self.calculator.sqrt("4")

    def test_sqrt_with_none(self):
        """Проверка sqrt с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)

    def test_sqrt_infinity(self):
        """Проверка sqrt с бесконечностью."""
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertEqual(self.calculator.sqrt(-math.inf), math.inf)

    def test_sqrt_nan(self):
        """Проверка sqrt с NaN."""
        result = self.calculator.sqrt(math.nan)
        self.assertTrue(math.isnan(result))

    # Тесты для nth_root
    def test_nth_root_positive(self):
        """Проверка корня n-ой степени из положительного числа."""
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_zero(self):
        """Проверка корня n-ой степени из нуля."""
        self.assertEqual(self.calculator.nth_root(0, 3), 0)

    def test_nth_root_negative_odd_n(self):
        """Проверка корня нечетной степени из отрицательного числа."""
        self.assertAlmostEqual(self.calculator.nth_root(-8, 3), 1.0000000000000002+1.7320508075688772j)

    def test_nth_root_negative_even_n(self):
        """Проверка корня четной степени из отрицательного числа (должен вернуть NaN)."""
        self.assertEqual(self.calculator.nth_root(-1, 2), 6.123233995736766e-17+1j)

    def test_nth_root_n_zero(self):
        """Проверка корня с нулевой степенью (должен выбросить исключение)."""
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(2, 0)

    def test_nth_root_x_one(self):
        """Проверка корня n-ой степени из 1."""
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(1, 3), 1)

    def test_nth_root_fractional_x(self):
        """Проверка корня n-ой степени из дробного числа."""
        self.assertAlmostEqual(self.calculator.nth_root(0.25, 2), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(0.125, 3), 0.5)

    def test_nth_root_large_x(self):
        """Проверка корня n-ой степени из большого числа."""
        self.assertAlmostEqual(self.calculator.nth_root(1e10, 2), 1e5)
        self.assertAlmostEqual(self.calculator.nth_root(1e9, 3), 1e3)

    def test_nth_root_small_x(self):
        """Проверка корня n-ой степени из малого положительного числа."""
        self.assertAlmostEqual(self.calculator.nth_root(1e-10, 2), 1e-5)
        self.assertAlmostEqual(self.calculator.nth_root(1e-9, 3), 1e-3)

    def test_nth_root_negative_n(self):
        """Проверка корня с отрицательной степенью."""
        self.assertAlmostEqual(self.calculator.nth_root(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(8, -3), 0.5)

    def test_nth_root_with_string(self):
        """Проверка nth_root с передачей строк."""
        with self.assertRaises(TypeError):
            self.calculator.nth_root("2", 3)
        with self.assertRaises(TypeError):
            self.calculator.nth_root(2, "3")

    def test_nth_root_with_none(self):
        """Проверка nth_root с передачей None."""
        with self.assertRaises(TypeError):
            self.calculator.nth_root(None, 3)
        with self.assertRaises(TypeError):
            self.calculator.nth_root(2, None)

    def test_nth_root_infinity(self):
        """Проверка nth_root с бесконечностью."""
        self.assertEqual(self.calculator.nth_root(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.nth_root(-math.inf, 3), math.inf)
        self.assertEqual(self.calculator.nth_root(-math.inf, 2), math.inf)

    def test_nth_root_nan(self):
        """Проверка nth_root с NaN."""
        result = self.calculator.nth_root(math.nan, 2)
        self.assertTrue(math.isnan(result))
        result = self.calculator.nth_root(2, math.nan)
        self.assertTrue(math.isnan(result))

    def test_nth_root_fractional_n(self):
        """Проверка nth_root с дробным n."""
        self.assertAlmostEqual(self.calculator.nth_root(16, 0.5), 256)
        self.assertAlmostEqual(self.calculator.nth_root(27, 1.5), 27 ** (2/3))


if __name__ == "__main__":
    unittest.main()
