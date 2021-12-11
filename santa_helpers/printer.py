from typing import List


def print_matrix(matrix: List[List[any]]):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))
