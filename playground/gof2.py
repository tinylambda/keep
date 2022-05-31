import copy


class State:
    DEAD = "X"
    LIVE = "O"

    def __init__(self, row_num: int, column_num: int):
        self.row_num = row_num
        self.column_num = column_num

        self._state = []
        for _ in range(row_num):
            self._state.append([self.DEAD for _ in range(column_num)])

    def __str__(self):
        # print the overall state
        line_fmt = "{}" * self.column_num
        lines = [line_fmt.format(*line_state) for line_state in self._state]
        return "\n".join(lines)

    def _ensure_index(self, row_index, column_index):
        # handle index overflow including negative index
        _row_index = row_index % self.row_num
        _column_index = column_index % self.column_num
        return _row_index, _column_index

    def state_at(self, row_index, column_index):
        _row_index, _column_index = self._ensure_index(row_index, column_index)
        return self._state[_row_index][_column_index]

    def set_state_at(self, row_index, column_index, state):
        _row_index, _column_index = self._ensure_index(row_index, column_index)
        self._state[_row_index][_column_index] = state

    def forward_at(self, row_index, column_index):
        _row_index, _column_index = self._ensure_index(row_index, column_index)
        current_state = self.state_at(_row_index, _column_index)
        count_alive_neighbors = self.count_alive_neighbors_at(_row_index, _column_index)

        new_state = copy.deepcopy(self._state)
        # how to change state
        if current_state == self.LIVE:
            if count_alive_neighbors < 2 or count_alive_neighbors > 3:
                new_state[_row_index][_column_index] = self.DEAD
        else:
            if count_alive_neighbors == 3:
                new_state[_row_index][_column_index] = self.LIVE

        self._state = new_state

    def refresh(self):
        for row_index in range(self.row_num):
            for column_index in range(self.column_num):
                self.forward_at(row_index, column_index)

    def count_alive_neighbors_at(self, row_index, column_index):
        top_coord = (row_index - 1, column_index)
        top_right_coord = (row_index - 1, column_index + 1)
        right_coord = (row_index, column_index + 1)
        bottom_right_coord = (row_index + 1, column_index + 1)
        bottom_coord = (row_index + 1, column_index)
        bottom_left_coord = (row_index + 1, column_index - 1)
        left_coord = (row_index, column_index - 1)
        top_left_coord = (row_index + 1, column_index - 1)

        coord_list = [
            top_coord,
            top_right_coord,
            right_coord,
            bottom_right_coord,
            bottom_coord,
            bottom_left_coord,
            left_coord,
            top_left_coord,
        ]

        neighbor_states = [self.state_at(*arg) for arg in coord_list]
        return len([item for item in neighbor_states if item == self.LIVE])


if __name__ == "__main__":
    s = State(4, 4)
    s.set_state_at(1, 1, s.LIVE)
    s.set_state_at(0, 0, s.LIVE)
    s.set_state_at(0, 1, s.LIVE)
    s.set_state_at(0, 2, s.LIVE)
    s.set_state_at(2, 1, s.LIVE)
    print(s)

    print("*" * 64)
    s.refresh()
    print(s)

    print("*" * 64)
    s.refresh()
    print(s)

    print("*" * 64)
    s.refresh()
    print(s)

    print("*" * 64)
    s.refresh()
    print(s)
