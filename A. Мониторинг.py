from typing import List, Tuple


def transpose(matrix: List[List[int]], row: int, col: int) -> List[List[int]]:
    matrix_transposed = []
    for j in range(col):
        transposed_row = []
        for i in range(row):
            transposed_row.append(matrix[i][j])
        matrix_transposed.append(transposed_row)
    return matrix_transposed


def read_input() -> Tuple[List[List[int]], int, int]:
    row = int(input())
    col = int(input())
    matrix = []
    for _ in range(row):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, row, col


matrix, row, col = read_input()
transposed_matrix = transpose(matrix, row, col)
for transposed_row in transposed_matrix:
    print(" ".join(map(str, transposed_row)))
# коммент
