import unittest
from square_function import square_num

# test comment

class TestFunction(unittest.TestCase):

    def test_square(self):
        result = square_num(2)
        self.assertEqual(result, 4)

    def test_negative_square(self):
        result = square_num(-2)
        self.assertEqual(result, 4)

    def test_float_square(self):
        result = square_num(1.5)
        self.assertAlmostEqual(result, 2.25, places=2)
    
    def test_float_negative_square(self):
        result = square_num(-1.5)
        self.assertAlmostEqual(result, 2.25, places=2)

    def test_zero_square(self):
        result = square_num(0)
        self.assertEqual(result, 0)

    def test_string_square(self):
        with self.assertRaises(ValueError) as context:
            square_num("two")
        self.assertEqual(str(context.exception), "Input must be a number (integer or float).")

if __name__ == '__main__':
    unittest.main()