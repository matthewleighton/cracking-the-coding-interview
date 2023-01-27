import unittest
from problem1_8 import zero_matrix, check_zero_in_first_column, check_zero_in_first_row

class TestProblem8(unittest.TestCase):

	def test_check_zero_in_first_row_correctly_true(self):
		matrix = [
			[1, 0, 3],
			[4, 5, 6],
			[7, 8, 9]
		]

		result = check_zero_in_first_row(matrix)
		self.assertTrue(result)

	def test_check_zero_in_first_row_correctly_false(self):
		matrix = [
			[1, 2, 3],
			[0, 5, 6],
			[7, 8, 9]
		]

		result = check_zero_in_first_row(matrix)
		self.assertFalse(result)

	
	def test_check_zero_in_first_column_correctly_true(self):
		matrix = [
			[1, 2, 3],
			[0, 5, 6],
			[7, 8, 9]
		]

		result = check_zero_in_first_column(matrix)
		self.assertTrue(result)

	def test_check_zero_in_first_column_correctly_false(self):
		matrix = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		]

		result = check_zero_in_first_column(matrix)
		self.assertFalse(result)

	

	def test_returns_original_matrix_if_no_elements_are_zero(self):
		input_matrix = [
			[1, 2],
			[3, 4],
			[5, 6]
		]

		expected_output = [
			[1, 2],
			[3, 4],
			[5, 6]
		]

		result = zero_matrix(input_matrix)
		
		self.assertEqual(result, input_matrix)

	def test_works_when_single_zero_element(self):
		input_matrix = [
			[1, 2],
			[3, 0],
			[5, 6]
		]

		expected_output = [
			[1, 0],
			[0, 0],
			[5, 0]
		]

		result = zero_matrix(input_matrix)

		self.assertEqual(result, expected_output)

	def test_works_when_multiple_zero_elements(self):
		input_matrix = [
			[0, 0, 3],
			[4, 5, 6],
			[7, 8, 9]
		]

		expected_output = [
			[0, 0, 0],
			[0, 0, 6],
			[0, 0, 9]
		]

		result = zero_matrix(input_matrix)

		self.assertEqual(result, expected_output)

	def test_works_with_rectangle_matrix_zero_in_first_column(self):
		input_matrix = [
			[1, 2],
			[0, 4],
			[5, 6]
		]

		excepted_output = [
			[0, 2],
			[0, 0],
			[0, 6]
		]

		result = zero_matrix(input_matrix)

		self.assertEqual(result, excepted_output)


if __name__ == '__main__':
	unittest.main()