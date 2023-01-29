def partition(linked_list, partition_value):
	current = linked_list.head
	runner = linked_list.head

	length = 0

	while runner.next is not None:
		runner = runner.next
		length += 1

	i = 0
	# while current.next is not None:
	while True:
		if current.next.data >= partition_value:
			linked_list.append(current.next.data)
			current.next = current.next.next
		else:
			current = current.next

		i += 1

		if i >= length:
			break