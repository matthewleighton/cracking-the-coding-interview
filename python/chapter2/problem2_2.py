# This version simply uses the known length of the linked list.
def get_kth_last_element_v1(linked_list, k):
	if k < 0 or k >= linked_list.length:
		raise ValueError(f'{k} is not a valid index.')

	current = linked_list.head
	target_index = linked_list.length - k - 1
	current_index = -1

	while current_index != target_index:
		current = current.next
		current_index += 1

	return current

#############################################################################################################

# This version doesn't use the pre-known length.
# Instead we use a recursive function.
# This steps along to the end of the list,
# then passes back elements such that we end up with the desired node.
def get_kth_last_element_v2(linked_list, k):
	if k < 0:
		raise ValueError(f'{k} is not a valid index.')
	
	current = linked_list.head

	completed_backsteps, element = kth_last_recursive(current, k)

	if completed_backsteps < k:
		raise ValueError(f'{k} is not a valid index.')

	return element

def kth_last_recursive(current, k, backsteps=None):
	# Iterate through the list until we get to the end.
	if backsteps is None:
		if current.next is not None:
			current = current.next
			backsteps = None
			backsteps, passback_element = kth_last_recursive(current, k, backsteps)	
		else:
			return -1, current # Start passing back the number of backsteps we've done, and the current node.

	backsteps += 1

	# As we work our way back up the chain, we pass back whatever node the previous call returned.
	# Unless the backsteps number indicates we're at our target node. Then the current node becomes the value we pass back each time.
	if backsteps == k:
		return_element = current
	else:
		return_element = passback_element

	return backsteps, return_element

#############################################################################################################

# This version uses a runner which is positioned k elements ahead of the current node.
# The runner and current then both walk to the end.
# At this point, current will be positioned at our desired node, k steps from the end.
def get_kth_last_element_v3(linked_list, k):
	if k < 0:
		raise ValueError(f'{k} is not a valid index.')

	current, runner = linked_list.head.next, linked_list.head.next

	for i in range(k):
		if runner.next is None:
			raise ValueError(f'{k} is not a valid index.')
		runner = runner.next

	while runner.next is not None:
		current = current.next
		runner = runner.next

	return current