import unittest
from problem2_4 import partition
from LinkedList import LinkedList

class TestProblem4(unittest.TestCase):

	# Create a LinkedList, with the values given by a standard Python List.
	def initialize_linked_list(self, value_list):
		linked_list = LinkedList()

		for value in value_list:
			linked_list.append(value)

		return linked_list

	# Returns True if a linked list is correctly partitioned, else False
	def check_list_is_partitioned_correctly(self, linked_list, partition_value):
		
		# This boolean will switch to False, once values are larger than the partiton_value.
		# After this, we should encounter no values less than the partition_value.
		less_than_value = True

		current = linked_list.head

		while current.next is not None:
			current = current.next
			if current.data >= partition_value:
				less_than_value = False

			if (current.data >= partition_value and less_than_value) or (current.data < partition_value and not less_than_value):
				return False

		return True

	# Checking that our test correctly recognises a non-partitioned list.
	def test_fails_if_non_partitoned_list_is_not_partitioned(self):
		linked_list = self.initialize_linked_list([3, 4, 8, 5, 10, 2, 1])
		partition_value = 5

		partitioned_correctly = self.check_list_is_partitioned_correctly(linked_list, partition_value)

		self.assertFalse(partitioned_correctly, 'This list is not partitioned, but our test thinks it is.')

	# Checking that a pre-partitioned list remains partitioned after running the function.
	def test_pre_partitioned_list_remains_correct(self):
		linked_list = self.initialize_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		partition_value = 5

		partition(linked_list, partition_value)
		partitioned_correctly = self.check_list_is_partitioned_correctly(linked_list, partition_value)

		self.assertTrue(partitioned_correctly, 'All values less than the partition value are not on the left side.')

	# Checking that the function correctly partitions a list which was not pre-partitioned.
	def test_non_partitoned_list_becomes_partitioned(self):
		linked_list = self.initialize_linked_list([3, 5, 8, 5, 10, 2, 1])
		partition_value = 5

		partition(linked_list, partition_value)
		partitioned_correctly = self.check_list_is_partitioned_correctly(linked_list, partition_value)

		self.assertTrue(partitioned_correctly, 'This list should become partitioned, but it is not.')

	# Checking that the list does not change length while we're partitioning it.
	def test_list_length_does_not_change(self):
		linked_list = self.initialize_linked_list([3, 5, 8, 5, 10, 2, 1])
		partition_value = 5

		original_length = len(str(linked_list))
		partition(linked_list, partition_value)
		new_length = len(str(linked_list))

		self.assertEqual(new_length, original_length, 'The list changed length during the partition process.')

	# Checking it works correctly when the partition_value is smaller than any list element.
	def test_partition_value_smaller_than_list_values(self):
		linked_list = self.initialize_linked_list([3, 5, 8, 5, 10, 2, 7])
		partition_value = 1

		partition(linked_list, partition_value)
		partitioned_correctly = self.check_list_is_partitioned_correctly(linked_list, partition_value)

		self.assertTrue(partitioned_correctly, 'This list should become partitioned, but it is not.')

	# Checking it works correctly when the partition_value is larger than any list element.
	def test_partition_value_larger_than_list_values(self):
		linked_list = self.initialize_linked_list([3, 5, 8, 5, 10, 2, 7])
		partition_value = 30

		partition(linked_list, partition_value)
		partitioned_correctly = self.check_list_is_partitioned_correctly(linked_list, partition_value)

		self.assertTrue(partitioned_correctly, 'This list should become partitioned, but it is not.')

	# Checking that it works correctly when each element is initially on the wrong side.
	def test_backwards_list(self):
		linked_list = self.initialize_linked_list([9,9,9,1,1,1])
		partition_value = 5

		partition(linked_list, partition_value)
		partitioned_correctly = self.check_list_is_partitioned_correctly(linked_list, partition_value)

		self.assertTrue(partitioned_correctly, 'This list should become partitioned, but it is not.')


if __name__ == '__main__':
	unittest.main()