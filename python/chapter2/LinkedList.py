class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, value_list=[]):
		self.head = Node()
		self.length = 0

		for value in value_list:
			self.append(value)

	def __str__(self):
		current = self.head
		value_list = []

		while current.next != None:
			current = current.next
			value_list.append(str(current.data))

		return ''.join(value_list)

	def append(self, data):
		current = self.head

		while current.next is not None:
			current = current.next

		current.next = Node(data)
		self.length += 1

	def get(self, index):
		if index >= self.length:
			raise ValueError(f'The index {index} is invalid. The linked list contains {self.length} elements.')
		
		current = self.head
		i = -1

		while i != index:
			current = current.next
			i += 1

		return current.data

	def delete(self, index):
		if index >= self.length:
			raise ValueError(f'The index {index} is invalid. The linked list contains {self.length} elements.')

		current = self.head
		i = -1

		while i != index-1:
			current = current.next
			i+= 1

		current.next = current.next.next
		self.length -= 1

		