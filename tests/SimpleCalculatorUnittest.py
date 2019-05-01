import unittest

from src.Calculators.SimpleCalculator import SimpleCalculator


class SimpleCalculatorUnittest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.calc_add(5, 6), 11)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.calc_subtract(5, 6), -1)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.calc_multiply(5, 6), 30)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.calc_divide(15, 3), 5)

    def test_divide_exception(self):
        with self.assertRaises(Exception):
            SimpleCalculator.calc_divide(5, 0)


if __name__ == '__main__':
    unittest.main()
