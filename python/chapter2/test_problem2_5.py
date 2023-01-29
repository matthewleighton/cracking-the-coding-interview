import unittest
from LinkedList import LinkedList
from problem2_5 import sum_lists_v1, sum_lists_v2, split_number_to_digits

def initialize_lists(list1_values, list2_values):
	list1 = LinkedList(list1_values)
	list2 = LinkedList(list2_values)

	return list1, list2

def list_to_int(linked_list, reverse_order=True):
	n = -1 if reverse_order else 1

	return int(str(linked_list)[::n])


class TestSumListsV1(unittest.TestCase):

	# Check that the data type returned is a linked list.
	def test_returns_linked_list(self):
		list1, list2 = initialize_lists([1], [2])
		
		summed_list = sum_lists_v1(list1, list2)
		
		self.assertEqual(type(summed_list), LinkedList)

	# Check we can sum single digits. (The digits do not rollover to a double digit result)
	def test_sums_single_digit_no_rollover(self):
		list1, list2 = initialize_lists([1], [2])
		
		summed_list = sum_lists_v1(list1, list2)
		int_result = list_to_int(summed_list)
		excepted = 1 + 2

		self.assertEqual(int_result, excepted)

	# Check we can sum single digits. (The digits DO rollover to a double digit result)
	def test_sums_single_digit_with_rollover(self):
		list1, list2 = initialize_lists([6], [8])
		
		summed_list = sum_lists_v1(list1, list2)
		int_result = list_to_int(summed_list)
		expected = 6 + 8

		self.assertEqual(int_result, expected)

	# Check we can sum numbers made up of two digits.
	def test_sums_two_digits(self):
		list1, list2 = initialize_lists([1, 7], [5, 4])

		summed_list = sum_lists_v1(list1, list2)
		int_result = list_to_int(summed_list)

		expected = 71 + 45

		self.assertEqual(int_result, expected)

	# Check we can sum two numbers which contain different numbers of digits.
	def test_sums_different_length_numbers(self):
		list1, list2 = initialize_lists(
			[7, 5, 8],
			[6, 2]
		)

		summed_list = sum_lists_v1(list1, list2)
		int_result = list_to_int(summed_list)

		expected = 857 + 26

		self.assertEqual(int_result, expected)
	
	# Check we can also add numbers where the elements are not in reverse order, if we use reverse_order=False.
	def test_non_reverse_order(self):
		list1, list2 = initialize_lists(
			[7, 5, 8],
			[6, 2]
		)

		summed_list = sum_lists_v1(list1, list2, reverse_order=False)
		int_result = list_to_int(summed_list, reverse_order=False)

		expected = 758 + 62

		self.assertEqual(int_result, expected)

class TestSumListsV2(unittest.TestCase):

	# Check single digits can be added.
	def test_v2_sums_single_digits(self):
		list1, list2 = initialize_lists([1], [2])

		summed_list = sum_lists_v2(list1, list2)
		int_result = list_to_int(summed_list)

		expected = 1 + 2

		self.assertEqual(int_result, expected)

	# Check single digits can be added (when the result is greater than 10).
	def test_v2_sums_single_digits_with_carry(self):	
		list1, list2 = initialize_lists([3], [9])

		summed_list = sum_lists_v2(list1, list2)
		int_result = list_to_int(summed_list)

		expected = 3 + 9

		self.assertEqual(int_result, expected)

	# Check double digit numbers can be summed (no carry needed).
	def test_v2_sums_double_digits_without_carry(self):
		list1, list2 = initialize_lists([3, 1], [4, 3])

		summed_list = sum_lists_v2(list1, list2)
		int_result = list_to_int(summed_list)

		expected = 13 + 34

		self.assertEqual(int_result, expected)

class TestSplitNumbertoDigits(unittest.TestCase):

	def test_works_with_double_digit_number(self):
		carry, unit = split_number_to_digits(42)

		self.assertEqual(carry, 4)
		self.assertEqual(unit, 2)
	
	def test_works_with_single_digit_number(self):
		carry, unit = split_number_to_digits(2)

		self.assertEqual(carry, 0)
		self.assertEqual(unit, 2)


	

if __name__ == '__main__':
	unittest.main()