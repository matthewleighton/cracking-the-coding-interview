import unittest
from problem1_5 import is_one_away

class TestProblem5(unittest.TestCase):

	def test_true_if_strings_are_same(self):
		result = is_one_away('abcd', 'abcd')
		self.assertTrue(result)

	def test_true_by_single_character_replacement(self):
		result = is_one_away('pale', 'pame')
		self.assertTrue(result)

	def test_false_by_multiple_character_replacement(self):
		result = is_one_away('pale', 'bame')
		self.assertFalse(result)

	def test_false_if_string_length_greater_than_one(self):
		input_value, target = 'pale', 'pe'
		result = is_one_away(input_value, target)
		self.assertFalse(result)

	def test_false_if_more_than_one_character_replacement_needed(self):
		result = is_one_away('pale', 'bole')
		self.assertFalse(result)

	def test_true_by_removing_character(self):
		input_value, target = 'pale', 'ple'
		result = is_one_away(input_value, target)
		self.assertTrue(result)

	def test_true_by_inserting_character(self):
		result = is_one_away('aple', 'apple')
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()