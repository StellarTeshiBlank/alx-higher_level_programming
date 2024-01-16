#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Create a copy of the input matrix to avoid modifying the original matrix
    new_matrix = matrix.copy()

    # Iterate through each row of the matrix
    for i in range(len(matrix)):

        # Use the map function to square each element in the current row
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    # Return the new matrix with squared elements
    return (new_matrix)
