import unittest
from LinkedList import LinkedList, Node

class TestLinkedList(unittest.TestCase):

	def test_str_works_correctly(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		expected = 'abcd'
		result = str(linked_list)

		self.assertEqual(result, expected)

	# def test_delete_node(self):
	# 	linked_list = LinkedList()
	# 	linked_list.append('a')
	# 	linked_list.append('b')
	# 	linked_list.append('c')
	# 	linked_list.append('d')

	# 	current = linked_list.head.next
	# 	linked_list.delete(current)

	# 	expected = 'acd'
	# 	result = str(linked_list)

	# 	self.assertEqual(result, expected)

	def test_length(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		result = linked_list.length
		self.assertEqual(result, 4)

	def text_length_on_empty(self):
		linked_list = LinkedList()
		result = linked_list.length
		self.assertEqual(result, 0)

	def test_get_valid(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		result = linked_list.get(2)
		self.assertEqual(result, 'c')

	def test_get_invalid(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		self.assertRaises(ValueError, linked_list.get, 4)

	def test_delete_first_element(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')

		linked_list.delete(0)

		first_element = linked_list.get(0)
		second_element = linked_list.get(1)

		self.assertEqual(first_element, 'b')
		self.assertEqual(second_element, 'c')

		length = linked_list.length
		self.assertEqual(length, 2)

	def test_delete_middle_element(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')

		linked_list.delete(1)

		first_element = linked_list.get(0)
		second_element = linked_list.get(1)

		self.assertEqual(first_element, 'a')
		self.assertEqual(second_element, 'c')

		length = linked_list.length
		self.assertEqual(length, 2)

	def test_delete_last_element(self):
		linked_list = LinkedList()
		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')

		linked_list.delete(2)

		first_element = linked_list.get(0)
		second_element = linked_list.get(1)

		self.assertEqual(first_element, 'a')
		self.assertEqual(second_element, 'b')

		length = linked_list.length
		self.assertEqual(length, 2)

	def test_initialize_list_with_values(self):
		linked_list = LinkedList([1, 2, 'a', 'b'])

		self.assertEqual(str(linked_list), '12ab')




if __name__ == '__main__':
	unittest.main()