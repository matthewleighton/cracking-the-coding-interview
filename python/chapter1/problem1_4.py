from collections import defaultdict

def is_palindrome_permutation(string):
	string = string.replace(' ', '').lower()

	character_counts = defaultdict(int)

	for character in string:
		character_counts[character] += 1
	
	# We're only allowed one character which appears an odd number of times.
	already_found_odd_count = False

	for count in character_counts.values():
		if count % 2 == 1:
			if already_found_odd_count:
				return False
			already_found_odd_count = True
	
	return True
