def is_one_away(input_string, target):
	if input_string == target:
		return True

	length_difference = len(target) - len(input_string)

	# If the lengths differ by more than 1, then they are more than 1 step away.
	if abs(length_difference) > 1:
		return False
	
	# If the lengths are equal, then we need to check if a replacement is possible.
	if length_difference == 0:
		return check_character_replacement(input_string, target)

	# If the target is longer, then check if we can insert a character.
	if length_difference == 1:
		return check_character_insertion(input_string, target)

	# Otherwise, the input_string must be longer.
	# In this case, removing a character is the same as performing an insertion on the target string.
	return check_character_insertion(target, input_string)

def check_character_replacement(input_string, target):
	found_difference = False

	for i, character in enumerate(input_string):
		if character != target[i]:
			if found_difference:
				return False
			
			found_difference = True

	return True

# Return True if short_string can be turned into long_string by inserting a character.
def check_character_insertion(short_string, long_string):
	long_index = -1
	for short_index, short_character in enumerate(short_string):
		long_index += 1
		long_character = long_string[long_index]

		if short_character == long_character:
			continue
		
		# If the characters are not equal, we increase the long_index.
		# If this happens more than once, then it means multiple characters are different,
		# and an insertion fix is not possible.
		long_index += 1
		if long_index - short_index > 1:
			return False
	
	return True
		
