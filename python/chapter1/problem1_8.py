def zero_matrix(matrix):
	# Record whether the first row/column contains a zero.
	zero_in_first_column = check_zero_in_first_column(matrix)
	zero_in_first_row = check_zero_in_first_row(matrix)

	# We now use the first row and column to record which rows/columns contain a zero.
	for col in range(1, len(matrix[0])):
		for row in range(1, len(matrix)):
			if matrix[row][col] == 0:
				matrix[0][col] = 0
				matrix[row][0] = 0

	# Then use those values in the first rows/columns to zero the rest of the matrix.
	for row in range(1, len(matrix)):
		if matrix[row][0] == 0:
			nullify_row(matrix, row)

	for col in range(1, len(matrix[0])):
		if matrix[0][col] == 0:
			nullify_column(matrix, col)

	# Finally, we use the booleans we recorded at the start to zero the first row/column if necessary.
	if zero_in_first_column:
		nullify_column(matrix, 0)

	if zero_in_first_row:
		nullify_row(matrix, 0)
	
	return matrix

def check_zero_in_first_column(matrix):
	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			return True
	return False

def check_zero_in_first_row(matrix):
	for i in range(len(matrix[0])):
		if matrix[0][i] == 0:
			return True
	return False

def nullify_column(matrix, col):
	for row in range(len(matrix)):
		matrix[row][col] = 0

def nullify_row(matrix, row):
	for col in range(len(matrix[0])):
		matrix[row][col] = 0