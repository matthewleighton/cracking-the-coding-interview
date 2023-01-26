import unittest
from problem1_1 import has_unique_characters

class TestProblem1(unittest.TestCase):

	def test_correctly_returns_true(self):
		result = has_unique_characters('abcdefghijklmnopqrstuvwxyz1234567890')
		self.assertTrue(result)

	def test_correctly_returns_false(self):
		result = has_unique_characters('abcdefghijklmnopqrstuvwxyz1234567890a')
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()