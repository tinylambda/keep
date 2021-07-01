def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<clsss {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))


if __name__ == '__main__':
    obj = Managed()
    obj.over

    Managed.over

    obj.over = 7
    obj.over

    obj.__dict__['over'] = 8
    print(
        vars(obj)
    )
    obj.over

    print('-' * 64)
    print(
        obj.over_no_get
    )
    print(
        Managed.over_no_get
    )
    obj.over_no_get = 7
    print(
        obj.over_no_get
    )
    obj.__dict__['over_no_get'] = 9
    print(
        obj.over_no_get
    )
    obj.over_no_get = 7
    print(
        obj.over_no_get
    )
    print('-' * 64)

    obj.non_over
    obj.non_over = 7
    print(obj.non_over)
    print(
        Managed.non_over
    )
    del obj.non_over
    print(
        obj.non_over
    )
    print('-' * 64)

    obj = Managed()
    Managed.over = 1
    Managed.over_no_get = 2
    Managed.non_over = 3
    print(
        obj.over, obj.over_no_get, obj.non_over
    )
    print('-' * 64)

    obj = Managed()
    print(
        obj.spam
    )
    print(
        Managed.spam
    )
    obj.spam = 7
    print(
        obj.spam
    )

    