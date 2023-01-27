def is_rotation(base_string, rotated_string):
	if len(rotated_string) != len(base_string):
		return False
	
	long_string = base_string * 2

	return rotated_string in long_string