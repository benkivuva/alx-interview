#!/usr/bin/python3
'''
Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

- Prototype: def rotate_2d_matrix(matrix):
- This function modifies the input matrix in-place without returning anything
- The matrix must have 2 dimensions, and it is assumed not to be empty.
'''


def rotate_2d_matrix(matrix):
    '''
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: The n x n 2D matrix to be rotated.

    Returns:
    - None: The function modifies the input matrix in-place.
    '''
    n = len(matrix)

    # Create a copy of the matrix as a reference
    copy = [[x for x in row] for row in matrix]

    # Perform the rotation in-place
    for i in range(0, n):
        for j in range(0, n):
            matrix[j][n-1-i] = copy[i][j]
