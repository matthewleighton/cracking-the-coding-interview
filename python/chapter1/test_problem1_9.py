import unittest
from problem1_9 import is_rotation

class TestProblem9(unittest.TestCase):

	def test_returns_true_for_waterbottle_example(self):
		result = is_rotation('waterbottle', 'erbottlewat')
		self.assertTrue(result)

	def test_returns_false_for_obvious_wrong(self):
		result = is_rotation('waterbottle', 'qwerty')
		self.assertFalse(result)

	def test_returns_false_for_missing_end_letter(self):
		result = is_rotation('waterbottle', 'erbottlewa')
		self.assertFalse(result)

	def test_returns_false_for_extended_string(self):
		result = is_rotation('waterbottle', 'waterbottlewa')
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()