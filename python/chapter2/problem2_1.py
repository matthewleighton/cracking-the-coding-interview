# This version uses a separate list to keep track of values we've encountered.
def remove_dups_v1(linked_list):
	found_values = []
	current = linked_list.head
	index = -1

	while current.next is not None:
		current = current.next
		index += 1

		if current.data in found_values:
			linked_list.delete(index)
		else:		
			found_values.append(current.data)

	return linked_list

# This version instead uses a runner technique.
def remove_dups_v2(linked_list):	
	current = linked_list.head
	current_index = -1

	while current.next is not None:
		current = current.next
		current_index +=1
		runner_index = current_index

		runner = current

		# The runner checks each element until the end of the linked list.
		# If any element is a duplicate of the current element, it is deleted.
		while runner.next is not None:
			runner = runner.next
			runner_index += 1

			if runner.data == current.data:
				linked_list.delete(runner_index)

	return linked_list