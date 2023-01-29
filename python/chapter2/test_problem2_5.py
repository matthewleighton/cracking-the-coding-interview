import unittest
from LinkedList import LinkedList
from problem2_5 import sum_lists

class TestProblem5(unittest.TestCase):

	def initialize_lists(self, list1_values, list2_values):
		list1 = LinkedList(list1_values)
		list2 = LinkedList(list2_values)

		return list1, list2

	def list_to_int(self, linked_list, reverse_order=True):
		n = -1 if reverse_order else 1

		return int(str(linked_list)[::n])

	# Check that the data type returned is a linked list.
	def test_returns_linked_list(self):
		list1, list2 = self.initialize_lists([1], [2])
		
		summed_list = sum_lists(list1, list2)
		
		self.assertEqual(type(summed_list), LinkedList)

	# Check we can sum single digits. (The digits do not rollover to a double digit result)
	def test_sums_single_digit_no_rollover(self):
		list1, list2 = self.initialize_lists([1], [2])
		
		summed_list = sum_lists(list1, list2)
		int_result = self.list_to_int(summed_list)
		excepted = 1 + 2

		self.assertEqual(int_result, excepted)

	# Check we can sum single digits. (The digits DO rollover to a double digit result)
	def test_sums_single_digit_with_rollover(self):
		list1, list2 = self.initialize_lists([6], [8])
		
		summed_list = sum_lists(list1, list2)
		int_result = self.list_to_int(summed_list)
		expected = 6 + 8

		self.assertEqual(int_result, expected)

	# Check we can sum numbers made up of two digits.
	def test_sums_two_digits(self):
		list1, list2 = self.initialize_lists([1, 7], [5, 4])

		summed_list = sum_lists(list1, list2)
		int_result = self.list_to_int(summed_list)

		expected = 71 + 45

		self.assertEqual(int_result, expected)

	# Check we can sum two numbers which contain different numbers of digits.
	def test_sums_different_length_numbers(self):
		list1, list2 = self.initialize_lists(
			[7, 5, 8],
			[6, 2]
		)

		summed_list = sum_lists(list1, list2)
		int_result = self.list_to_int(summed_list)

		expected = 857 + 26

		self.assertEqual(int_result, expected)
	
	# Check we can also add numbers where the elements are not in reverse order, if we use reverse_order=False.
	def test_non_reverse_order(self):
		list1, list2 = self.initialize_lists(
			[7, 5, 8],
			[6, 2]
		)

		summed_list = sum_lists(list1, list2, reverse_order=False)
		int_result = self.list_to_int(summed_list, reverse_order=False)

		expected = 758 + 62

		self.assertEqual(int_result, expected)


if __name__ == '__main__':
	unittest.main()