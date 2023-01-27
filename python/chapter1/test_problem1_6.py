import unittest
from problem1_6 import compress_string

class TestProblem6(unittest.TestCase):
	def test_returns_original_string_if_no_compression_possible(self):
		input_string = 'abcdefgh'
		result = compress_string(input_string)
		self.assertEqual(result, input_string)

		result = compress_string('aabbccdd')
		self.assertEqual(result, 'aabbccdd')

	def test_succesfully_compresses_strings(self):
		result = compress_string('abbcccddddeeeee')
		self.assertEqual(result, 'a1b2c3d4e5')

		result = compress_string('aaAAbCCCdeEEEEEE')
		self.assertEqual(result, 'a2A2b1C3d1e1E6')

	def test_works_on_empty_string(self):
		result = compress_string('')
		self.assertEqual(result, '')

	

	


if __name__ == '__main__':
	unittest.main()