import unittest
from problem2_1 import remove_dups_v1, remove_dups_v2

from LinkedList import LinkedList

class TestProblem1(unittest.TestCase):

	def test_v1_returns_original_list_if_no_dups(self):
		linked_list = LinkedList()

		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		expected = 'abcd'
		result = str(remove_dups_v1(linked_list))

		self.assertEqual(result, expected)

	def test_v1_removes_single_separated_duplicate(self):
		linked_list = LinkedList()

		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')
		linked_list.append('c')

		expected = 'abcd'
		result = str(remove_dups_v1(linked_list))

		self.assertEqual(result, expected)

	def test_v2_returns_original_list_if_no_dups(self):
		linked_list = LinkedList()

		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		expected = 'abcd'
		result = str(remove_dups_v2(linked_list))

		self.assertEqual(result, expected)

	def test_v2_removes_single_separated_duplicate(self):
		linked_list = LinkedList()

		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')
		linked_list.append('c')

		expected = 'abcd'
		result = str(remove_dups_v2(linked_list))

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()