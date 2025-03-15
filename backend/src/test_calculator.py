import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(5, 3), 8)
        self.assertEqual(
            self.calculator.addition(complex(2, -3), complex(-1, 1)),
            complex(1, -2)
        )
        with self.assertRaises(TypeError):
            self.calculator.addition("1", 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 3), 9)
        self.assertEqual(self.calculator.multiplication(3, -3), -9)
        self.assertEqual(self.calculator.multiplication(3, -3.0), -9.0)
        self.assertEqual(
            self.calculator.multiplication(complex(2, 2), complex(2, -1)),
            complex(6, 2)
        )

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertEqual(self.calculator.subtraction(5, -3), 8)
        self.assertEqual(self.calculator.subtraction(5, -3.0), 8.0)
        self.assertEqual(
            self.calculator.subtraction(complex(5, 5), complex(2, -3)),
            complex(3, 8)
        )
        with self.assertRaises(TypeError):
            self.calculator.subtraction("5", 2)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2.0)
        self.assertEqual(self.calculator.division(6, 0), None)
        self.assertEqual(self.calculator.division(6, -3.0), -2.0)
        self.assertEqual(
            self.calculator.division(complex(5, 5), complex(1, 2)),
            complex(3, -1)
        )
        with self.assertRaises(TypeError):
            self.calculator.division("6", 3)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(-5.0), 5.0)
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(
            self.calculator.absolute(complex(3, 4)),
            5
        )
        with self.assertRaises(TypeError):
            self.calculator.absolute("5")

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 2), 9)
        self.assertEqual(self.calculator.degree(3, 0), 1)
        self.assertEqual(self.calculator.degree(2, -2.0), 0.25)
        self.assertEqual(
            self.calculator.degree(complex(2, 1), 2),
            complex(3, 4)
        )
        with self.assertRaises(TypeError):
            self.calculator.degree("1", 1)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1.0)
        self.assertEqual(self.calculator.ln(1), 0.0)
        with self.assertRaises(TypeError):
            self.calculator.ln(complex(2, 3))
        with self.assertRaises(TypeError):
            self.calculator.ln("5")

    def test_log(self):
        self.assertEqual(self.calculator.log(100, 10), 2.0)
        self.assertEqual(self.calculator.log(1, 10), 0.0)
        with self.assertRaises(TypeError):
            self.calculator.log(complex(2, 3), 10)
        with self.assertRaises(TypeError):
            self.calculator.log("100", 10)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4.0)
        self.assertEqual(self.calculator.sqrt(0), 0.0)
        res = self.calculator.sqrt(complex(1, 1))
        self.assertAlmostEqual(res.real, 1.0987, places=4)
        self.assertAlmostEqual(res.imag, 0.4551, places=4)
        with self.assertRaises(TypeError):
            self.calculator.sqrt("16")

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2.0)
        self.assertEqual(self.calculator.nth_root(27, 3), 3.0)
        self.assertAlmostEqual(self.calculator.nth_root(2.25, 2.0), 1.5, places=4)
        res = self.calculator.nth_root(complex(2, 5), 2)
        self.assertAlmostEqual(res.real, 1.9216093264675973, places=4)
        self.assertAlmostEqual(res.imag, 1.3010, places=4)
        with self.assertRaises(TypeError):
            self.calculator.nth_root("16", 4)
        with self.assertRaises(TypeError):
            self.calculator.nth_root(16, "4")


if __name__ == "__main__":
    unittest.main()
