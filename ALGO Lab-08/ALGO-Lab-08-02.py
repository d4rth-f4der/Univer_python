def get_el_sum_col(matrix: list, col: int) -> int:
    els_sum = 0
    for row_i in range(len(matrix)):
        els_sum += matrix[row_i][col]
    return els_sum

def swap_cols(matrix: list, col1: int, col2: int):
    for row_i in range(0, len(matrix)):
        matrix[row_i][col1], matrix[row_i][col2] = matrix[row_i][col2], matrix[row_i][col1]


def matrix_cols_insert_sort(matrix: list):
    cols_qty = len(matrix[0])
    for col_i in range(1, cols_qty):
        focus_i = col_i
        col_cur_sum = get_el_sum_col(matrix, col_i)

        while focus_i > 0:
            col_prev_sum = get_el_sum_col(matrix, focus_i - 1)
            if col_cur_sum < col_prev_sum:
                swap_cols(matrix, focus_i, focus_i - 1)
                focus_i -= 1
            else:
                break

matrix1 = [
    [5, 4, 5, 11, 1, 12, 6],
    [2, 12, 0, 0, 7, 5, 18],
    [8, 8, 13, 8, 0, 3, 5],
    [3, 5, 6, 3, 5, 8, 14],
    [0, 7, 2, 6, 2, 6, 15],
    [5, 8, 0, 6, 11, 12, 13],
    [12, 5, 4, 1, 7, 6, 9],
    [6, 8, 11, 3, 7, 10, 0]
]

for row in matrix1:
    print(row)
for i in range(len(matrix1[0])):
    print(get_el_sum_col(matrix1, i), end='  ')
print("(sums)\n")

matrix_cols_insert_sort(matrix1)
for row in matrix1:
    print(row)
for i in range(len(matrix1[0])):
    print(get_el_sum_col(matrix1, i), end='  ')
print("(sums)\n")