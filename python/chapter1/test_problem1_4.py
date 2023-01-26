import unittest
from problem1_4 import is_palindrome_permutation

class TestProblem4(unittest.TestCase):
    
	def test_actual_palindrome_with_center_letter(self):
		result = is_palindrome_permutation('taco cat')
		self.assertTrue(result)

	def test_actual_palindrome_without_center_letter(self):
		result = is_palindrome_permutation('tac cat')
		self.assertTrue(result)

	def test_palindrome_permutation_with_center_letter(self):
		result = is_palindrome_permutation('Tact Coa')
		self.assertTrue(result)
	
	def test_palindrome_permutation_without_center_letter(self):
		result = is_palindrome_permutation('Tact Ca')
		self.assertTrue(result)

	def test_non_palindrome_permutation(self):
		result = is_palindrome_permutation('abc defg')
		self.assertFalse(result)

	def test_non_palindrome_permutation_with_repeats(self):
		result = is_palindrome_permutation('abcdefgab')
		self.assertFalse(result)

	def test_single_character_string(self):
		result = is_palindrome_permutation('a')
		self.assertTrue(result)

	def test_two_character_non_palindrome(self):
		result = is_palindrome_permutation('ab')
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()