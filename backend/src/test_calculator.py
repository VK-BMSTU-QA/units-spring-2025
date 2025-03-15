import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calculator.addition('hello', 'world'), 'helloworld')

    def test_add3(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_substract(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_substract2(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'asafas', 'None')

    def test_substract3(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_multiply2(self):
        self.assertEqual(self.calculator.multiplication(-3.5, 2), -7)

    def test_multiply3(self):
        self.assertEqual(self.calculator.multiplication(3, 'asd'), 'asdasdasd')

    def test_multiply4(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)

    def test_multiply5(self):
        self.assertRaises(TypeError, self.calculator.multiplication, '12123', 'fsdfds')

    def test_divide(self):
        self.assertEqual(self.calculator.division(3, 2), 1.5)

    def test_divide2(self):
        self.assertEqual(self.calculator.division(3, 0), None)

    def test_divide3(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    def test_divide4(self):
        self.assertRaises(TypeError, self.calculator.division, 'None', 'None')

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-3), 3)

    def test_absolute2(self):
        self.assertEqual(self.calculator.absolute(-3.5), 3.5)

    def test_absolute3(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_absolute4(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'None')

    def test_degree(self):
        self.assertEqual(self.calculator.degree(-3, 4), 81)

    def test_degree2(self):
        self.assertRaises(TypeError, self.calculator.degree, 'None', 2)

    def test_degree3(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 2)

    def test_degree4(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, None)

    def test_degree5(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln2(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln2(self):
        self.assertRaises(TypeError, self.calculator.ln, 'asd')

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e**2), 2)

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_log2(self):
        self.assertRaises(TypeError, self.calculator.log, None, 2)

    def test_log3(self):
        self.assertRaises(TypeError, self.calculator.log, 2, None)

    def test_log4(self):
        self.assertRaises(TypeError, self.calculator.log, 'None', 2)

    def test_log5(self):
        self.assertRaises(TypeError, self.calculator.log, 2, 'None')

    def test_log6(self):
        self.assertEqual(self.calculator.log(0.5, 2), -1)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt2(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt3(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'None')

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)

    def test_nth_root2(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)

    def test_nth_root3(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, None)

    def test_nth_root4(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'None', 2)

    def test_nth_root5(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, 'None')

    def test_nth_root6(self):
        self.assertEqual(self.calculator.nth_root(16, -4), 0.5)

    def test_nth_root7(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)



if __name__ == "__main__":
    unittest.main()
