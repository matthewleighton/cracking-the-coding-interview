from LinkedList import Node

# Sort a list, such that all elements less than the partition_value are on the left,
# while all elements greater are on the right.
# Aside for this, we do not care about value ordering.
def partition(linked_list, partition_value):
	current = linked_list.head
	end_node = linked_list.head

	# We get the list's last node, and count the length at the same time.
	length = 0
	while end_node.next is not None:
		end_node = end_node.next
		length += 1

	i = 0
	while True:

		# The next element is greater than (or equal to) the partition_value, so we move it to the end.
		if current.next.data >= partition_value:
		
			# The function linked_list.append needs to walk through the whole list each time.
			# But we already have the end_node. So instead we just change that node's "next" value, without doing the walk.
			end_node.next = Node(current.next.data)
			end_node = end_node.next
			current.next = current.next.next
		
		else: # Otherwise, just continue walking to the end of the list.
			current = current.next

		i += 1

		# We'll never actually reach the end of the list, since we'll get stuck in a loop of moving elements back.
		# So instead we just stop once we've moved as many elements as are in the list.
		if i >= length:
			break