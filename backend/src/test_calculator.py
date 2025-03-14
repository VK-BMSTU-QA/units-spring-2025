import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.division(10, 0))

    def test_addition_positive(self):
        self.assertEqual(self.calculator.addition(1, -5), -4)

    def test_multiplication_positive(self):
        self.assertEqual(self.calculator.multiplication(4, 5), 20)

    def test_subtraction_positive(self):
        self.assertEqual(self.calculator.subtraction(20, 15), 5)

    def test_division_positive_numbers(self):
        # Проверка деления двух положительных чисел
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_division_negative_numbers(self):
        # Проверка деления отрицательных чисел
        self.assertEqual(self.calculator.division(-10, -2), 5)

    def test_division_mixed_signs(self):
        # Проверка деления чисел с разными знаками
        self.assertEqual(self.calculator.division(-10, 2), -5)
        self.assertEqual(self.calculator.division(10, -2), -5)

    def test_division_by_zero(self):
        # Проверка деления на ноль (должно вернуть None)
        self.assertIsNone(self.calculator.division(10, 0))

    def test_division_zero_dividend(self):
        self.assertAlmostEqual(self.calculator.division(5.5, 2.2), 2.5)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(4), 4)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-4), 4)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_degree_positive(self):
        self.assertEqual(self.calculator.degree(2, 16), 65536) #x ** n

    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(1), 0) #math.log(x)

    def test_log_positive(self):
        self.assertEqual(self.calculator.log(8, 2), 3) #math.log(x, n)

    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(64), 8) #x ** 0.5

    def test_nth_root_positive(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3) #x ** (1. / n)




if __name__ == "__main__":
    unittest.main()
