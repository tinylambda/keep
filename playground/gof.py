from collections import namedtuple

ALIVE = "*"
EMPTY = "-"
TICK = object()


Query = namedtuple("Query", ("y", "x"))
Transition = namedtuple("Transition", ("y", "x", "state"))


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # North East
    e_ = yield Query(y + 0, x + 1)  # East
    se = yield Query(y - 1, x + 1)  # South East
    s_ = yield Query(y - 1, x + 0)  # South
    sw = yield Query(y - 1, x - 1)  # South West
    w_ = yield Query(y - 0, x - 1)  # West
    nw = yield Query(y + 1, x - 1)  # North West

    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        line_fmt = "{}" * self.width
        lines = [line_fmt.format(*item) for item in self.rows]
        return "\n".join(lines)


def simulate(height: int, width: int):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


def live_a_generation(grid: Grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny


if __name__ == "__main__":
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    grid.assign(0, 4, ALIVE)
    grid.assign(1, 4, ALIVE)
    grid.assign(1, 5, ALIVE)
    sim = simulate(grid.height, grid.width)
    for i in range(50):
        print(grid)
        grid = live_a_generation(grid, sim)
        print("O" * grid.width)
