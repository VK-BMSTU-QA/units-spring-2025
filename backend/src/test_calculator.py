import unittest
from src.calculator import Calculator 
from typing import Tuple, List, Callable, Any

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_ok(self):
        tests = [
            ([1, 2], 3),
            ([1, -1], 0),
            ([0, 1], 1),
            ([5.5, 10.75], 16.25),
        ]

        run_table_test(self, self.calculator.addition, tests)

    def test_add_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.addition, tests)

    def test_mul(self):
        tests = [
            ([1, 1], 1),
            ([1, -1], -1),
            ([1, 0], 0),
            ([1.5, 2], 3),
        ]

        run_table_test(self, self.calculator.multiplication, tests)

    def test_mul_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.multiplication, tests)


    def test_sub(self):
        tests = [
            ([1, 1], 0),
            ([1, -1], 2),
            ([1, 0], 1),
            ([20.654, 18.153], 2.501)
        ]

        run_table_test(self, self.calculator.subtraction, tests)

    def test_sub_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.subtraction, tests)

    def test_div(self):
        tests = [
            ([1, -1], -1),
            ([5.55, 5], 1.11),
            ([5, 0.5], 10),
            ([1.44, 1.2], 1.2),
        ]

        run_table_test(self, self.calculator.division, tests)

    def test_div_by_zero(self):
        tests = [
            ([1, 0], ZeroDivisionError),
            ([-1, 0], ZeroDivisionError),
            ([123123, 0], ZeroDivisionError),
            ([-2231.0034, 0], ZeroDivisionError),
            ([0.001, 0], ZeroDivisionError),
            ([0, 0], ZeroDivisionError),
        ]

        run_table_test_raises(self, self.calculator.division, tests)

    def test_div_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.division, tests)


    def test_abs(self):
        tests = [
            ([-1], 1),
            ([-0], 0),
            ([1.2313], 1.2313),
            ([100020202], 100020202)
        ]

        run_table_test(self, self.calculator.absolute, tests)

    def test_abs_only_numbers_allowed(self):
        tests = [
            (["hello"], TypeError),
            ([(1, 2)], TypeError),
            ([[]], TypeError),
        ]

        run_table_test_raises(self, self.calculator.absolute, tests)

    def test_degree(self):
        tests = [
            ([1, 1], 1),
            ([0, 3883], 0),
            ([11, 2], 121),
            ([5.56, 5], 5313.417697178),
            ([-1, 3], -1),
        ]

        run_table_test(self, self.calculator.degree, tests)

    def test_degree_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_degree_only_positive_base_if_exponent_is_frac(self):
        tests = [
            ([-1, 1.23], ValueError),
            ([-5, 4.23], ValueError),
            ([-9, 9.34], ValueError),
            ([-1.3123, 1.23], ValueError),
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_degree_zero_to_zero(self):
        tests = [
            ([0, 0], ValueError)
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_degree_div_by_zero(self):
        tests = [
            ([0, -1], ZeroDivisionError),
            ([0, -4], ZeroDivisionError),
            ([0, -5], ZeroDivisionError),
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_ln(self):
        tests = [
            ([1], 0),
            ([2], 0.693147181),
            ([200.543], 5.301028688),
            ([401235], 12.90230257),
            ([0.231233], -1.46432919),
        ]

        run_table_test(self, self.calculator.ln, tests)

    def test_ln_only_numbers_allowed(self):
        tests = [
            (["hello"], TypeError),
            ([(1, 2)], TypeError),
            ([[]], TypeError),
        ]

        run_table_test_raises(self, self.calculator.ln, tests)

    def test_ln_only_positive_numbers_allowed(self):
        tests = [
            ([-1], ValueError),
            ([-123.32], ValueError),
            ([-858.158], ValueError),
        ]

        run_table_test_raises(self, self.calculator.ln, tests)

    def test_log(self):
        tests = [
            ([1, 3], 0),
            ([1, 4], 0),
            ([1, 8], 0),
            ([2.33, 1.55], 1.930082716),
            ([1.334345, 300055], 0.02287083),
            ([2, 0.4], -0.756470797)
        ]

        run_table_test(self, self.calculator.log, tests)

    def test_log_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.log, tests)

    def test_log_only_positive_numbers_allowed(self):
        tests = [
            ([-2, 2], ValueError),
            ([2, -2], ValueError),
            ([2.090132, -12332], ValueError),
            ([-5743.231100, 1102332], ValueError),
            ([-5743.231100, -12332], ValueError),
        ]

        run_table_test_raises(self, self.calculator.log, tests)

    def test_log_one_in_base_not_allowed(self):
        tests = [
            ([2, 1], ValueError),
            ([9, 1], ValueError),
            ([1.32, 1], ValueError),
            ([2.00504, 1], ValueError),
        ]

        run_table_test_raises(self, self.calculator.log, tests)

    def test_sqrt(self):
        tests = [
            ([2], 1.414213562),
            ([1], 1),
            ([4], 2),
            ([9], 3),
            ([12344433212344], 3513464.559710828),
            ([0], 0)
        ]

        run_table_test(self, self.calculator.sqrt, tests)

    def test_sqrt_only_numbers_allowed(self):
        tests = [
            (["hello"], TypeError),
            ([(1, 2)], TypeError),
            ([[]], TypeError),
        ]

        run_table_test_raises(self, self.calculator.sqrt, tests)

    def test_sqrt_only_positive_numbers_allower(self):
        tests = [
            ([-1], ValueError),
            ([-1.300], ValueError),
            ([-3348348], ValueError)
        ]

        run_table_test_raises(self, self.calculator.sqrt, tests)

    def test_nth_root(self):
        tests = [
            ([1, 2], 1),
            ([1, 4], 1),
            ([1, 6], 1),
            ([2, 2], 1.414213562),
            ([27, 3], 3),
            ([128, 7], 2),
            ([12341234, 984.303], 1.0167272108),
        ]

        run_table_test(self, self.calculator.nth_root, tests)

    def test_nth_root_only_positive_arg_if_base_is_frac(self):
        tests = [
            ([-1, 2.33], ValueError),
            ([-4.22, 8454.24], ValueError),
            ([-2, 0.2344], ValueError)
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)

    def test_nth_root_zero_base_is_not_allowed(self):
        tests = [
            ([-1, 0], ValueError),
            ([1, 0], ValueError),
            ([0, 0], ValueError),
            ([1.320392, 0], ValueError),
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)

    def test_nth_root_only_positive_numbers_if_base_even(self):
        tests = [
            ([-1, 2], ValueError),
            ([-10345, 4], ValueError),
            ([-1.383, 6], ValueError),
            ([-2, 8], ValueError),
            ([-4, 10], ValueError),
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)

    def test_nth_root_only_numbers_allowed(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)




def run_table_test(test_class: unittest.TestCase, test_func: Callable, test_cases: List[Tuple[List, Any]], delta=1e-6):
    for (args, expected) in test_cases:
        got = test_func(*args)
        test_class.assertAlmostEqual(got,
                                     expected,
                                     msg=f"failed when called with {args.__str__()}, expected {expected}, got {got}",
                                     delta=delta
                                     )

def run_table_test_raises(test_class: unittest.TestCase, test_func: Callable, test_cases: List[Tuple[List, Any]]):
    for (args, expected) in test_cases:
        with test_class.assertRaises(expected):
            test_func(*args)

if __name__ == "__main__":
    unittest.main()
