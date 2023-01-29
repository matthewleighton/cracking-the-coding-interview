# Instead of actually deleting the node, we just set its values such that
# they match those of its next node, essentially "becoming" the next node.
def delete_middle_node(node):
	if node.next is None:
		raise ValueError('This node is the last node, so cannot be deleted.')
	
	next_node = node.next

	node.data = next_node.data
	node.next = next_node.next