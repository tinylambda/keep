from typing import List


class Table:
    def __init__(self, table: List[List[int]]):
        self._table = table
        self._n = len(table[0])
        self._min_index = 0
        self._max_index = self._n - 1

    def left_of(self, x, y):
        if y <= self._min_index:
            return None, None
        return x, y - 1

    def right_of(self, x, y):
        if y >= self._max_index:
            return None, None
        return x, y + 1

    def top_of(self, x, y):
        if x <= self._min_index:
            return None, None
        return x - 1, y

    def bottom_of(self, x, y):
        if x >= self._max_index:
            return None, None
        return x + 1, y

    def value_of(self, x, y):
        if x is None or y is None:
            return None
        return self._table[x][y]

    def still_alive(self, x, y):
        values = [
            self.value_of(*self.left_of(x, y)) == 0,
            self.value_of(*self.top_of(x, y)) == 0,
            self.value_of(*self.right_of(x, y)) == 0,
            self.value_of(*self.bottom_of(x, y)) == 0,
        ]
        return any(values)

    def is_alive(self, x, y) -> bool:
        check_v = self.value_of(x, y)
        if check_v == 0:
            return None

        alive = self.still_alive(x, y)
        if alive:
            return alive

        # search the left
        left_x, left_y = self.left_of(x, y)
        value = self.value_of(left_x, left_y)

        if value == check_v:
            alive = self.is_alive(left_x, left_y)
            if alive:
                return True

        # search the top
        top_x, top_y = self.top_of(x, y)
        value = self.value_of(top_x, top_y)
        if value == check_v:
            alive = self.is_alive(top_x, top_y)
            if alive:
                return True

        # search the right
        right_x, right_y = self.right_of(x, y)
        value = self.value_of(right_x, right_y)
        if value == check_v:
            alive = self.is_alive(right_x, right_y)
            if alive:
                return True

        # search the bottom
        bottom_x, bottom_y = self.bottom_of(x, y)
        value = self.value_of(bottom_x, bottom_y)
        if value == check_v:
            alive = self.is_alive(bottom_x, bottom_y)
            if alive:
                return True
        return False


if __name__ == '__main__':
    example_input_1 = [[0, 1, 0], [1, 2, 1], [0, 1, 0]]  # x=1, y=1 False
    example_input_2 = [[0, 1, 0], [1, 2, 1], [0, 0, 0]]  # x=1, y=1 True

    test_table = Table(example_input_2)
    assert test_table.value_of(1, 1) == 2
    assert test_table.top_of(1, 1) == (0, 1)
    assert test_table.top_of(0, 1) == (None, None)
    assert test_table.still_alive(1, 1) is True
    assert test_table.still_alive(1, 0) is True

    assert test_table.is_alive(1, 1) is True

    test_table2 = Table(example_input_1)
    assert test_table2.is_alive(1, 1) is False

    # not fully tested
