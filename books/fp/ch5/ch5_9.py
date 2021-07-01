from inspect import signature
from books.fp.ch5.ch5_6 import tag

if __name__ == '__main__':
    my_tag = {
        'name': 'img',
        'title': 'Sunset boulevard',
        'src': 'sunset.jpg', 'cls': 'framed',
    }
    sig = signature(tag)
    bound_args = sig.bind(**my_tag)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)

    del my_tag['name']
    bound_args = sig.bind(**my_tag)

