"""
INPUT:

[
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]

OUTPUT in spiral order
1 2 3 4 8 12 11 10 9 5 6 7
"""


def spiral_order(matrix, rows, columns, start_pos=("left", "top")):
    if not matrix:
        raise ValueError("empty matrix")

    output_in_spiral_order = []

    if start_pos == ("left", "top"):
        # row fixed, iterate over columns
        row = 0
        column = 0
        while True:
            output_in_spiral_order.append(matrix[row][column])
            column += 1
            if column == columns:
                break
        # drop the first row to get a smaller matrix
        smaller_matrix = matrix[1:]
        new_rows = rows - 1
        new_columns = columns

        if new_rows == 0 or new_columns == 0:
            return output_in_spiral_order

        output_in_spiral_order.extend(
            spiral_order(
                smaller_matrix, new_rows, new_columns, start_pos=("right", "top")
            )
        )
    elif start_pos == ("right", "top"):
        # column fixed, iterate over rows
        row = 0
        column = columns - 1
        while True:
            output_in_spiral_order.append(matrix[row][column])
            row += 1
            if row == rows:
                break

        # drop the right column
        smaller_matrix = [item[:-1] for item in matrix]
        new_rows = rows
        new_columns = columns - 1

        if new_rows == 0 or new_columns == 0:
            return output_in_spiral_order

        output_in_spiral_order.extend(
            spiral_order(
                smaller_matrix, new_rows, new_columns, start_pos=("right", "bottom")
            )
        )

    elif start_pos == ("right", "bottom"):
        # row fixed, iterate over columns (reversed)
        row = rows - 1
        column = columns - 1
        while True:
            output_in_spiral_order.append(matrix[row][column])
            column -= 1
            if column == -1:
                break
        # drop the bottom row
        smaller_matrix = matrix[:-1]
        new_rows = rows - 1
        new_columns = columns

        if new_rows == 0 or new_columns == 0:
            return output_in_spiral_order

        output_in_spiral_order.extend(
            spiral_order(
                smaller_matrix, new_rows, new_columns, start_pos=("left", "bottom")
            )
        )

    elif start_pos == ("left", "bottom"):
        # column fixed, iterate over rows (reversed)
        row = rows - 1
        column = 0
        while True:
            output_in_spiral_order.append(matrix[row][column])
            row -= 1
            if row == -1:
                break
        # drop the left column
        smaller_matrix = [item[1:] for item in matrix]
        new_rows = rows
        new_columns = columns - 1

        if new_rows == 0 or new_columns == 0:
            return output_in_spiral_order

        output_in_spiral_order.extend(
            spiral_order(
                smaller_matrix, new_rows, new_columns, start_pos=("left", "top")
            )
        )
    return output_in_spiral_order


if __name__ == "__main__":
    _matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    _m = len(_matrix)
    _n = len(_matrix[0])

    print(spiral_order(_matrix, _m, _n))
    # should be 1 2 3 4 8 12 11 10 9 5 6 7

    _matrix = [
        [5, 6, 7],
    ]
    _m = len(_matrix)
    _n = len(_matrix[0])
    print(
        spiral_order(
            _matrix,
            _m,
            _n,
        )
    )
    # should be 5, 6, 7

    print(spiral_order(_matrix, _m, _n, start_pos=("right", "top")))
    # should be 7, 6, 5
