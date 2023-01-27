def zero_matrix(matrix):
	zero_columns, zero_rows = [], []

	for col in range(len(matrix[0])):
		for row in range(len(matrix)):
			if matrix[row][col] == 0:
				zero_columns.append(col)
				zero_rows.append(row)

	for col in zero_columns:
		nullify_column(matrix, col)
	
	for row in zero_rows:
		nullify_row(matrix, row)

	return matrix

def nullify_column(matrix, col):
	for row in range(len(matrix)):
		matrix[row][col] = 0

def nullify_row(matrix, row):
	for col in range(len(matrix[0])):
		matrix[row][col] = 0