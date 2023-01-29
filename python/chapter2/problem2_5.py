from LinkedList import LinkedList, Node

# By default the digits are given in reverse order.
def sum_lists_v1(list1, list2, reverse_order=True):
	n = -1 if reverse_order else 1
	
	num1 = int(str(list1)[::n])
	num2 = int(str(list2)[::n])

	summed_int = num1 + num2

	summed_list = LinkedList(list(str(summed_int)[::n]))

	return summed_list


# This version does not convert the entire lists to integers,
# but instead sums item by item.
def sum_lists_v2(list1, list2):
	current1, current2 = list1.head, list2.head

	while current1.next is not None or current2.next is not None:
		
		if current1.next is None:
			current1.next = Node(0)
		elif current2.next is None:
			current2.next = Node(0)
		
		current1, current2 = current1.next, current2.next

		value = current1.data

		sum_digits(value, current2)

	return list2

# Add the specified value to the specified node.
# If the resulting value is greater than 10, then the function
# is called recursively to update the next digit position.
def sum_digits(value, node):
	carry, unit = split_number_to_digits(value + node.data)

	node.data = unit

	if carry > 0:
		if node.next is None:
			node.next = Node(0)
		sum_digits(carry, node.next)



# This splits a two digit number into two values:
# - A "carry" (tens position)
# - A "unit" (ones position)
def split_number_to_digits(number):
	number_string = str(number)
	if len(number_string) == 1:
		number_string = '0' + number_string
	
	return list(map(int, number_string))