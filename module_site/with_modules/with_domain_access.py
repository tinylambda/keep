# import sys
#
#
# class T:
#     def __init__(self, name):
#         self.name = name
#         self.original_stdout = sys.stdout
#
#     def __enter__(self):
#         print(f'Entering {self.name}')
#         sys.stdout = sys.stderr
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'Exiting {self.name}')
#         sys.stdout = self.original_stdout
#
#
# class M:
#     def __init__(self, c, keys):
#         self.c = c
#         self.keys = keys
#
#     def __enter__(self):
#         self.watch(*self.keys)
#         with self.c as ci:
#             print('yyyy')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('xxxx')
#
#
# with M(T('1')):
#     print('GOGOGOG')
#

# import contextlib
#
#
# class T:
#     def __enter__(self):
#         print('Enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exit')
#
#
# @contextlib.contextmanager
# def mycm(keys):
#     try:
#         with T() as t:
#             old_data = {}
#             new_data = yield old_data
#             print('save ', new_data)
#     except RuntimeError:
#         pass
#     finally:
#         pass
#
#
# with mycm(['a', 'b', 'c']) as old_data:
#     print(old_data)
#     print(type(old_data))


class A:
    def __init__(self):
        self._x = None
