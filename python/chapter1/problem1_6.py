def compress_string(string):
	if string == '':
		return string

	compressed_string = [string[0]]
	count = 1

	for character in string[1:]:
		if character == compressed_string[-1]:
			count += 1
			continue
		
		compressed_string.append(str(count))
		compressed_string.append(character)
		count = 1

	# Append the final count, since this isn't handled in the loop.
	compressed_string.append(str(count))

	# Only return the compressed string if it's shorter than the original.
	if len(compressed_string) >= len(string):
		return string

	return ''.join(compressed_string)