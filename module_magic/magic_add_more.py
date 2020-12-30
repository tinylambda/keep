class A:
    def __init__(self, value, _min, _max):
        self.value = value
        self._min = _min
        self._max = _max

    def __add__(self, other):
        tmp_value = self.value + other.value
        if tmp_value > self._max:
            raise RuntimeError(f'Max value {self._max}')
        elif tmp_value < self._min:
            raise RuntimeError(f'Min value {self._min}')
        self.value = tmp_value


if __name__ == '__main__':
    a1 = A(1, 0, 10)
    a2 = A(1, 0, 20)
    a1 + a2
    print(a1.value)



