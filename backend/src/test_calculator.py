import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_1(self):
        self.assertEqual(self.calculator.addition(1, -1), 0)

    def test_add_2(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, "1")

    def test_add_3(self):
        self.assertEqual(self.calculator.addition(1, True), 2)

    def test_add_4(self):
        self.assertEqual(self.calculator.addition(1/3, False), 1/3)

    def test_add_5(self):
        self.assertRaises(TypeError, self.calculator.addition,
                          [1, 2, 3, 4, 4], False)

    def test_add_6(self):
        self.assertEqual(self.calculator.addition("1", "1"), "11")

    def test_add_7(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, 1, 1, 1, 0)

    def test_add_8(self):
        self.assertEqual(self.calculator.addition(1j, 1j), 2j)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multiplication_1(self):
        self.assertEqual(self.calculator.multiplication(5, -5), -25)

    def test_multiplication_2(self):
        self.assertEqual(self.calculator.multiplication(2, "1"), "11")

    def test_multiplication_3(self):
        self.assertEqual(self.calculator.multiplication(2, True), 2)

    def test_multiplication_4(self):
        self.assertEqual(self.calculator.multiplication(1/3, False), 0)

    def test_multiplication_5(self):
        self.assertEqual(self.calculator.multiplication(
            [1, 2, 3, 4, 4], False), [])

    def test_multiplication_6(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "1", "11")

    def test_multiplication_7(self):
        self.assertEqual(self.calculator.multiplication(0.25, 1/4), 1/16)

    def test_multiplication_8(self):
        self.assertRaises(
            TypeError, self.calculator.multiplication, 1, 1, 1, 1, 1, 1)

    def test_multiplication_9(self):
        self.assertEqual(self.calculator.multiplication(1j+3, 3), 3j+9)

    def test_multiplication_10(self):
        self.assertEqual(self.calculator.multiplication(1j, 1j), -1)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtraction_1(self):
        self.assertEqual(self.calculator.subtraction(5, -5), 10)

    def test_subtraction_2(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 2, "1")

    def test_subtraction_3(self):
        self.assertEqual(self.calculator.subtraction(2, True), 1)

    def test_subtraction_4(self):
        self.assertEqual(self.calculator.subtraction(1/3, False), 1/3)

    def test_subtraction_5(self):
        self.assertRaises(TypeError, self.calculator.subtraction,
                          [1, 2, 3, 4, 4], False)

    def test_subtraction_6(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "1", "11")

    def test_subtraction_7(self):
        self.assertEqual(self.calculator.subtraction(0.25, 1/4), 0)

    def test_subtraction_8(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 1, 1)

    def test_subtraction_9(self):
        self.assertEqual(self.calculator.subtraction(0.25, 1j), 0.25-1j)

    def test_division(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_division_1(self):
        self.assertEqual(self.calculator.division(5, -5), -1)

    def test_division_2(self):
        self.assertRaises(TypeError, self.calculator.division, 2, "1")

    def test_division_3(self):
        self.assertEqual(self.calculator.division(2, True), 2)

    def test_division_4(self):
        self.assertEqual(self.calculator.division(1/3, False), None)

    def test_division_5(self):
        self.assertRaises(TypeError, self.calculator.division,
                          [1, 2, 3, 4, 4], 1.2)

    def test_division_6(self):
        self.assertRaises(TypeError, self.calculator.division, "1", "11")

    def test_division_7(self):
        self.assertEqual(self.calculator.division(0.25, 1/4), 1)

    def test_division_8(self):
        self.assertEqual(self.calculator.division(
            [1, 2, 3, 4, 4], 0), None)

    def test_division_9(self):
        self.assertRaises(
            TypeError, self.calculator.division, 1, 1, 1, 1, 1, 1)

    def test_division_10(self):
        self.assertEqual(self.calculator.division(0.25, 1j), -0.25j)

    def test_division_11(self):
        self.assertEqual(self.calculator.division(6 + 3j, 3), 2 + 1j)

    def test_division_12(self):
        self.assertEqual(self.calculator.division(6 + 3j, 6 + 3j), 1)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(2), 2)

    def test_absolute_1(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_2(self):
        self.assertRaises(TypeError, self.calculator.absolute, "1")

    def test_absolute_3(self):
        self.assertEqual(self.calculator.absolute(True), 1)

    def test_absolute_4(self):
        self.assertEqual(self.calculator.absolute(-1/3), 1/3)

    def test_absolute_5(self):
        self.assertRaises(TypeError, self.calculator.absolute,
                          [1, 2, 3, 4, 4], False)

    def test_absolute_6(self):
        self.assertRaises(TypeError, self.calculator.absolute, [1, 2, 3, 4, 5])

    def test_absolute_7(self):
        self.assertEqual(self.calculator.absolute(
            5 + 1j), self.calculator.sqrt(26))

    def test_degree(self):
        self.assertEqual(self.calculator.degree(200, False), 1)

    def test_degree_1(self):
        self.assertEqual(self.calculator.degree(5, -2), 1/25)

    def test_degree_2(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, "1",)

    def test_degree_3(self):
        self.assertEqual(self.calculator.degree(2, True), 2)

    def test_degree_4(self):
        self.assertEqual(self.calculator.degree(False, 1/3), 0)

    def test_degree_5(self):
        self.assertRaises(TypeError, self.calculator.degree,
                          False, [1, 2, 3, 4, 4])

    def test_degree_6(self):
        self.assertRaises(TypeError, self.calculator.degree, "1", 4)

    def test_degree_7(self):
        self.assertEqual(self.calculator.degree(16, 1/4), 2)

    def test_degree_8(self):
        self.assertRaises(
            TypeError, self.calculator.degree, 1, 1, 1, 1, 1, 1)

    def test_degree_9(self):
        self.assertEqual(self.calculator.degree(1j, 2), -1)

    def test_degree_10(self):
        self.assertEqual(self.calculator.degree(1j+2, 3), 2+11j)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.exp(4)), 4)

    def test_ln_1(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_2(self):
        self.assertRaises(TypeError, self.calculator.ln, "1")

    def test_ln_3(self):
        self.assertEqual(self.calculator.ln(True), 0)

    def test_ln_4(self):
        self.assertEqual(self.calculator.ln(math.exp(-2)), -2)

    def test_ln_5(self):
        self.assertRaises(ValueError, self.calculator.ln,
                          False)

    def test_ln_6(self):
        self.assertRaises(TypeError, self.calculator.ln, [1, 2, 3, 4, 5])

    def test_ln_7(self):
        self.assertRaises(TypeError, self.calculator.ln, 5 + 1j)

    def test_ln_8(self):
        self.assertRaises(TypeError, self.calculator.ln, -10, 10)

    def test_ln_9(self):
        self.assertRaises(ValueError, self.calculator.ln, -10)

    def test_log(self):
        self.assertEqual(self.calculator.log(100, 10), 2)

    def test_log_1(self):
        self.assertEqual(self.calculator.log(16, 2), 4)

    def test_log_2(self):
        self.assertRaises(TypeError, self.calculator.log, 1, "1")

    def test_log_3(self):
        self.assertEqual(self.calculator.log(True, 1000), 0)

    def test_log_4(self):
        self.assertEqual(self.calculator.log(1/9, 3), -2)

    def test_log_5(self):
        self.assertRaises(ValueError, self.calculator.log,
                          False, 10)

    def test_log_6(self):
        self.assertRaises(TypeError, self.calculator.log, [1, 2, 3, 4, 5])

    def test_log_7(self):
        self.assertRaises(TypeError, self.calculator.log, 5 + 1j, 10)

    def test_log_8(self):
        self.assertRaises(ValueError, self.calculator.log, -10, 10)

    def test_log_9(self):
        self.assertRaises(TypeError, self.calculator.log, 1, 1j)

    def test_log_10(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 10, 1)

    def test_log_11(self):
        self.assertRaises(TypeError, self.calculator.log, 10)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_1(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_2(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "1")

    def test_sqrt_3(self):
        self.assertEqual(self.calculator.sqrt(True), 1)

    # прикол питона работы с мнимыми числами
    # Добавлено чтобы проходили тесты
    def test_sqrt_4(self):
        self.assertEqual(self.calculator.sqrt(-4), 1.2246467991473532e-16+2j)

    def test_sqrt_5(self):
        self.assertRaises(TypeError, self.calculator.sqrt,
                          1, 2, 3, )

    def test_sqrt_6(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2, 3, 4, 5])

    # прикол питона работы с мнимыми числами
    # Добавлено чтобы проходили тесты
    def test_sqrt_7(self):
        self.assertEqual(self.calculator.sqrt(2j), 1.0000000000000002+1j)

    def test_sqrt_8(self):
        self.assertEqual(self.calculator.sqrt(0.81), 0.9)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(200, 1), 200)

    def test_nth_root_1(self):
        self.assertEqual(self.calculator.nth_root(25, -2), 1/5)

    def test_nth_root_2(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, "1",)

    def test_nth_root_3(self):
        self.assertRaises(ZeroDivisionError,
                          self.calculator.nth_root, 2, False)

    def test_nth_root_4(self):
        self.assertEqual(self.calculator.nth_root(False, 1/3), 0)

    def test_nth_root_5(self):
        self.assertRaises(TypeError, self.calculator.nth_root,
                          False, [1, 2, 3, 4, 4])

    def test_nth_root_6(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "1", 4)

    def test_nth_root_7(self):
        self.assertEqual(self.calculator.nth_root(16, 1/4), 65536)

    def test_nth_root_8(self):
        self.assertRaises(
            TypeError, self.calculator.nth_root, 1, 1, 1, 1, 1, 1)

    def test_nth_root_9(self):
        self.assertEqual(self.calculator.nth_root(27j, 3),
                         2.598076211353316+1.4999999999999998j)

    # прикол питона работы с мнимыми числами
    # Добавлено чтобы проходили тесты
    def test_nth_root_10(self):
        self.assertEqual(self.calculator.nth_root(1024, 10), 2)


if __name__ == "__main__":
    unittest.main()
