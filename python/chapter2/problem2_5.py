from LinkedList import LinkedList

# By default the digits are given in reverse order.
def sum_lists(list1, list2, reverse_order=True):
	n = -1 if reverse_order else 1
	
	num1 = int(str(list1)[::n])
	num2 = int(str(list2)[::n])

	summed_int = num1 + num2

	summed_list = LinkedList(list(str(summed_int)[::n]))

	return summed_list