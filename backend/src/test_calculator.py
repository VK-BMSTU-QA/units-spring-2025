import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

   def setUp(self):
      self.calculator = Calculator()

   def test_add_input_types(self):
      self.assertRaises(TypeError, self.calculator.addition, 1, "2")
      self.assertRaises(TypeError, self.calculator.addition, [], 2)
      self.assertRaises(TypeError, self.calculator.addition, 1, {})
      self.assertRaises(TypeError, self.calculator.addition, 1, None)
      self.assertEqual(TypeError, self.calculator.addition(1, True), 2)

   def test_add(self):
      self.assertEqual(self.calculator.addition(1, 2), 3)
      self.assertEqual(self.calculator.addition(-1, -2), -3)
      self.assertEqual(self.calculator.addition(1, 0), 1)
      self.assertEqual(self.calculator.addition(1.5, 2.5), 4.0)
      self.assertEqual(self.calculator.addition(1e10, 1e10), 2e10)

   def test_mult_input_types(self):
      self.assertRaises(TypeError, self.calculator.multiplication, "2", 2)
      self.assertRaises(TypeError, self.calculator.multiplication, [], 2)
      self.assertRaises(TypeError, self.calculator.multiplication, 1, {})
      self.assertRaises(TypeError, self.calculator.multiplication, 1, None)
      self.assertRaises(TypeError, self.calculator.multiplication, 1, True)

   def test_mult(self):
      self.assertEqual(self.calculator.multiplication(2, 3), 6)
      self.assertEqual(self.calculator.multiplication(2, 0), 0)
      self.assertEqual(self.calculator.multiplication(-2, -3), 6)
      self.assertEqual(self.calculator.multiplication(2.5, 3.5), 8.75)
      self.assertEqual(self.calculator.multiplication(1e10, 1e10), 1e20)

   def test_subt_input_types(self):
      self.assertRaises(TypeError, self.calculator.subtraction, "2", 2)
      self.assertRaises(TypeError, self.calculator.subtraction, [], 2)
      self.assertRaises(TypeError, self.calculator.subtraction, 1, {})
      self.assertRaises(TypeError, self.calculator.subtraction, 1, None)
      self.assertRaises(TypeError, self.calculator.subtraction, 1, True)

   def test_subt(self):
      self.assertEqual(self.calculator.subtraction(3, 1), 2)
      self.assertEqual(self.calculator.subtraction(3, 0), 3)
      self.assertEqual(self.calculator.subtraction(-3, -1), -2)
      self.assertEqual(self.calculator.subtraction(3.5, 1.5), 2.0)
      self.assertEqual(self.calculator.subtraction(1e10, 1e10), 0)

   def test_div_input_types(self):
      self.assertRaises(TypeError, self.calculator.division, "2", 2)
      self.assertRaises(TypeError, self.calculator.division, [], 2)
      self.assertRaises(TypeError, self.calculator.division, 1, {})
      self.assertRaises(TypeError, self.calculator.division, 1, None)
      self.assertRaises(TypeError, self.calculator.division, 1, True)

   def test_div(self):
      self.assertEqual(self.calculator.division(6, 3), 2)
      self.assertEqual(self.calculator.division(6, -3), -2)
      self.assertRaises(ZeroDivisionError, self.calculator.division, 6, 0)
      self.assertEqual(self.calculator.division(6.5, 0.5), 13.0)
      self.assertEqual(self.calculator.division(1e10, 1e10), 1)

   def test_abs_input_types(self):
      self.assertRaises(TypeError, self.calculator.absolute, "2")
      self.assertRaises(TypeError, self.calculator.absolute, [])
      self.assertRaises(TypeError, self.calculator.absolute, {})
      self.assertRaises(TypeError, self.calculator.absolute, None)
      self.assertRaises(TypeError, self.calculator.absolute, True)

   def test_abs(self):
      self.assertEqual(self.calculator.absolute(6), 6)
      self.assertEqual(self.calculator.absolute(-6), 6)
      self.assertEqual(self.calculator.absolute(-0), 0)
      self.assertEqual(self.calculator.absolute(-6.5), 6.5)
      self.assertEqual(self.calculator.absolute(1e10), 1e10)

   def test_deg_input_types(self):
      self.assertRaises(TypeError, self.calculator.degree, "2", 2)
      self.assertRaises(TypeError, self.calculator.degree, [], 2)
      self.assertRaises(TypeError, self.calculator.degree, {}, 1)
      self.assertRaises(TypeError, self.calculator.degree, None, 1)
      self.assertRaises(TypeError, self.calculator.degree, True, 1)
    
   def test_deg(self):
      self.assertEqual(self.calculator.degree(2, 3), 8)
      self.assertEqual(self.calculator.degree(2, 0), 1)
      self.assertEqual(self.calculator.degree(2, -2), 0.25)
      self.assertEqual(self.calculator.degree(16, -0.5), 0.25)
      self.assertAlmostEqual(self.calculator.degree(1e5, 2), 1e10)
      self.assertRaises(ValueError, self.calculator.degree, 0, 0)
      self.assertRaises(ValueError, self.calculator.degree, -2, 0.5)

   def test_ln_input_types(self):
      self.assertRaises(TypeError, self.calculator.ln, "2", 2)
      self.assertRaises(TypeError, self.calculator.ln, [], 2)
      self.assertRaises(TypeError, self.calculator.ln, {}, 1)
      self.assertRaises(TypeError, self.calculator.ln, None, 1)
      self.assertRaises(TypeError, self.calculator.ln, True, 1)

   def test_ln(self):
      self.assertEqual(self.calculator.ln(1), 0)
      self.assertAlmostEqual(self.calculator.ln(0.5), -0.693147, places=6)
      self.assertAlmostEqual(self.calculator.ln(1e10), 23.0258509, places=6)
      self.assertRaises(ValueError, self.calculator.ln, 0)
      self.assertRaises(ValueError, self.calculator.ln, -1)

   def test_log_input_types(self):
      self.assertRaises(TypeError, self.calculator.log, "2", 2)
      self.assertRaises(TypeError, self.calculator.log, [], 2)
      self.assertRaises(TypeError, self.calculator.log, {}, 1)
      self.assertRaises(TypeError, self.calculator.log, None, 1)
      self.assertRaises(TypeError, self.calculator.log, True, 2)

   def test_log(self):
      self.assertEqual(self.calculator.log(8, 2), 3)
      self.assertEqual(self.calculator.log(0.25, 2), -2.0)
      self.assertEqual(self.calculator.log(1e10, 10), 10.0)
      self.assertRaises(ValueError, self.calculator.log, -8, 2)
      self.assertRaises(ValueError, self.calculator.log, 8, -2)
      self.assertRaises(ValueError, self.calculator.log, 8, 0)
      self.assertRaises(ValueError, self.calculator.log, 0, 8)

   def test_sqrt_input_types(self):
      self.assertRaises(TypeError, self.calculator.sqrt, "2", 2)
      self.assertRaises(TypeError, self.calculator.sqrt, [], 2)
      self.assertRaises(TypeError, self.calculator.sqrt, {}, 1)
      self.assertRaises(TypeError, self.calculator.sqrt, None, 1)
      self.assertRaises(TypeError, self.calculator.sqrt, True, 1)

   def test_sqrt(self):
      self.assertEqual(self.calculator.sqrt(4), 2)
      self.assertEqual(self.calculator.sqrt(0), 0)
      self.assertEqual(self.calculator.sqrt(0.25), 0.5)
      self.assertEqual(self.calculator.sqrt(1e10), 1e5)
      self.assertEqual(self.calculator.sqrt(1e-10), 1e-5)
      self.assertRaises(ValueError, self.calculator.sqrt, -4)

   def test_nth_root_input_types(self):
      self.assertRaises(TypeError, self.calculator.nth_root, "2", 2)
      self.assertRaises(TypeError, self.calculator.nth_root, [], 2)
      self.assertRaises(TypeError, self.calculator.nth_root, {}, 1)
      self.assertRaises(TypeError, self.calculator.nth_root, None, 1)
      self.assertRaises(TypeError, self.calculator.nth_root, True, 1)   

   def test_nth_root(self):
      self.assertEqual(self.calculator.nth_root(4, 2), 2)
      self.assertEqual(self.calculator.nth_root(0, 2), 0)
      self.assertEqual(self.calculator.nth_root(-8, 3), -2)
      self.assertEqual(self.calculator.nth_root(0.125, 3), 0.5)
      self.assertEqual(self.calculator.nth_root(1e10, 10), 10.0)
      self.assertRaises(ValueError, self.calculator.nth_root, -4, 2)


if __name__ == "__main__":
    unittest.main()
