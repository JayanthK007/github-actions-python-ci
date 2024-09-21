import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
   def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-1, -1), -2)


def test_subtract(self):
  self.assertEqual(subtract(10, 3), 7)
  self.assertEqual(subtract(-3, 1), -4)
  self.assertEqual(subtract(-3, -3), 0)


def test_divide(self):
  self.assertEqual(divide(4,2),2)
  self.assertEqual(divide(6,2),3)
  self.assertEqual(divide(20,10),2)


if __name__ == '__main__':
   unittest.main()