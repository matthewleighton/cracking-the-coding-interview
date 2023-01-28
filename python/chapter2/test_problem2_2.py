import unittest
from problem2_2 import get_kth_last_element_v1, get_kth_last_element_v2
from LinkedList import LinkedList

class TestProblem2(unittest.TestCase):

	def initialize_linked_list(self):
		linked_list = LinkedList()

		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		return linked_list

	# ---- Version 1 ----

	def test_v1_returns_last_element_if_k_is_0(self):
		linked_list = self.initialize_linked_list()
		k = 0

		target_element = get_kth_last_element_v1(linked_list, k)
		
		self.assertEqual(target_element.data, 'd')

	def test_v1_returns_second_last_element_if_k_is_1(self):
		linked_list = self.initialize_linked_list()
		k = 1

		target_element = get_kth_last_element_v1(linked_list, k)
		
		self.assertEqual(target_element.data, 'c')

	def test_v1_returns_first_element_if_k_is_length_minus_1(self):
		linked_list = self.initialize_linked_list()
		k = 3

		target_element = get_kth_last_element_v1(linked_list, k)
		
		self.assertEqual(target_element.data, 'a')

	def test_v1_raises_value_error_if_k_is_length_or_greater(self):
		linked_list = self.initialize_linked_list()
		k = 4

		self.assertRaises(ValueError, get_kth_last_element_v1, linked_list, k)

	def test_v1_raises_value_error_if_k_is_less_than_zero(self):
		linked_list = self.initialize_linked_list()
		k = -1

		self.assertRaises(ValueError, get_kth_last_element_v1, linked_list, k)


	# ---- Version 2 ----

	def test_v2_returns_last_element_if_k_is_0(self):
		linked_list = self.initialize_linked_list()
		k = 0

		target_element = get_kth_last_element_v2(linked_list, k)
		
		self.assertEqual(target_element.data, 'd')

	def test_v2_returns_second_last_element_if_k_is_1(self):
		linked_list = self.initialize_linked_list()
		k = 1

		target_element = get_kth_last_element_v2(linked_list, k)
		
		self.assertEqual(target_element.data, 'c')

	def test_v2_returns_first_element_if_k_is_length_minus_1(self):
		linked_list = self.initialize_linked_list()
		k = 3

		target_element = get_kth_last_element_v2(linked_list, k)
		
		self.assertEqual(target_element.data, 'a')

	def test_v2_raises_value_error_if_k_is_length_or_greater(self):
		linked_list = self.initialize_linked_list()
		k = 4

		self.assertRaises(ValueError, get_kth_last_element_v2, linked_list, k)

	def test_v2_raises_value_error_if_k_is_less_than_zero(self):
		linked_list = self.initialize_linked_list()
		k = -1

		self.assertRaises(ValueError, get_kth_last_element_v2, linked_list, k)




if __name__ == '__main__':
	unittest.main()