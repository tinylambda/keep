class RestrictKeysMixins:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self._restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self._restrict_key_type):
            raise TypeError('keys must be ' + str(self._restrict_key_type))
        super().__setitem__(key, value)


if __name__ == '__main__':
    class RDict(RestrictKeysMixins, dict):
        pass

    d = RDict(_restrict_key_type=str)
    e = RDict([('name', 'Dave'), ('n', 37)], _restrict_key_type=str)
    f = RDict(name='Dave', n=37, _restrict_key_type=str)

    print(f)
    f[42] = 10

