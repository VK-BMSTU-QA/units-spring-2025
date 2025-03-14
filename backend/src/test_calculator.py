import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        test_cases = [
            [1.1, 2, 3.1, "ok"],
            [-1, 2, 1, "ok"],
            ["1", 2, TypeError, "err"],
                      ]
        func = self.calculator.addition
        test_all(self, test_cases, func)
    
    def test_multiplication(self):
        test_cases = [
            [1.1, 2, 2.2, "ok"],
            [-1, 2, -2, "ok"],
            ["1", "2", TypeError, "err"],
                      ]
        func = self.calculator.multiplication
        test_all(self, test_cases, func)

    def test_subtraction(self):
        test_cases = [
            [4.1, 2, 2.1, "ok"],
            [-1, 2, -3, "ok"],
            ["1", 2, TypeError, "err"],
                      ]
        func = self.calculator.subtraction
        test_all(self, test_cases, func)
    
    def test_division(self):
        test_cases = [
            [2, 2, 1, "ok"],
            [-1, 2, -0.5, "ok"],
            ["1", 2, TypeError, "err"],
            [1, 0, None, "ok"],
                      ]
        func = self.calculator.division
        test_all(self, test_cases, func)

    def test_absolute(self):
        test_cases = [
            [2.1, 2.1, "ok"],
            [-1, 1, "ok"],
            ["1", TypeError, "err"],
                      ]
        func = self.calculator.absolute
        test_all(self, test_cases, func)

    def test_degree(self):
        test_cases = [
            [2.1, 2, 4.41, "ok"],
            [-1, 2, 1, "ok"],
            [2, -1, 0.5, "ok"],
            ["1", 2, TypeError, "err"],
                      ]
        func = self.calculator.degree
        test_all(self, test_cases, func)

    def test_ln(self):
        test_cases = [
            [1.5, 0.405465, "ok"],
            ["1", TypeError, "err"],
            [-1, ValueError, "err"],
                      ]
        func = self.calculator.ln
        test_all(self, test_cases, func)
    
    def test_log(self):
        test_cases = [
            [5.1, 2, 2.3505, "ok"],
            ["1", 2, TypeError, "err"],
            [-2, 1, ValueError, "err"],
            [2, -1, ValueError, "err"],
                      ]
        func = self.calculator.log
        test_all(self, test_cases, func)

    def test_sqrt(self):
        test_cases = [
            [2.25, 1.5, "ok"],
            ["1", TypeError, "err"],
            #[-1, ValueError, "err"],
                      ]
        func = self.calculator.sqrt
        test_all(self, test_cases, func)
    
    
    def test_nth_root(self):
        test_cases = [
            [2.25, 2, 1.5, "ok"],
            ["1", 2, TypeError, "err"],
            [2.25, 0, ZeroDivisionError, "err"],
            #[-2, 1, ValueError, "err"],
            #[2, -1, ValueError, "err"],
                      ]
        func = self.calculator.nth_root
        test_all(self, test_cases, func)
    

def test_all(self, test_cases, func):
    for i in test_cases:
        if i[-1]=="ok":
            if len(i)==4:
                self.assertAlmostEqual(func(i[0], i[1]), i[2], 4)
            else:
                self.assertAlmostEqual(func(i[0]), i[1], 4)
        elif i[-1]=="err":
            if len(i)==4:
                self.assertRaises(i[2], func, i[0], i[1])
            else:
                self.assertRaises(i[1], func, i[0])


if name == "main":
    unittest.main()