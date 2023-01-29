import unittest
from problem2_3 import delete_middle_node
from LinkedList import LinkedList

class TestProblem3(unittest.TestCase):

	def initialize_linked_list(self):
		linked_list = LinkedList()

		linked_list.append('a')
		linked_list.append('b')
		linked_list.append('c')
		linked_list.append('d')

		return linked_list

	def test_delete_first_node(self):
		linked_list = self.initialize_linked_list()
		node = linked_list.head.next

		delete_middle_node(node)

		list_output = str(linked_list)

		self.assertEqual(list_output, 'bcd')

	def test_delete_second_node(self):
		linked_list = self.initialize_linked_list()
		node = linked_list.head.next.next

		delete_middle_node(node)

		list_output = str(linked_list)

		self.assertEqual(list_output, 'acd')

	def test_delete_third_node(self):
		linked_list = self.initialize_linked_list()
		node = linked_list.head.next.next.next

		delete_middle_node(node)

		list_output = str(linked_list)

		self.assertEqual(list_output, 'abd')

	def test_deleting_last_node_raises_value_error(self):
		linked_list = self.initialize_linked_list()
		node = linked_list.head.next.next.next.next

		self.assertRaises(ValueError, delete_middle_node, node)

if __name__ == '__main__':
	unittest.main()