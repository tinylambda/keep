from typing import Tuple, Callable, NamedTuple
from collections import namedtuple


example_rgb = (128, 152, 64)

RGB = Tuple[int, int, int]
red: Callable[[RGB], int] = lambda color: color[0]
print(example_rgb, red(example_rgb))


Color = namedtuple('Color', 'red green blue name')
example_color = Color(red=128, green=152, blue=64, name='name_1')
print(example_color, example_color.red)


class Color(NamedTuple):
    """RGB color"""
    red: int
    green: int
    blue: int
    name: str


example_color = Color(red=128, green=152, blue=64, name='name_2')
print(example_color, example_color.red)

