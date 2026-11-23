import unittest

from calc import add, mul


class AddTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


class MulTests(unittest.TestCase):
    def test_mul(self):
        for a, b, expected in [(2, 3, 6), (-2, 3, -6), (0, 3, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(mul(a, b), expected)


if __name__ == "__main__":
    unittest.main()
