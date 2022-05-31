import inspect


def func(self, request, a, b, c, d, *args, **kwargs):
    pass


if __name__ == "__main__":
    skip_parameters = ["self", "request"]
    sig_inspect = inspect.signature(func)
    sig_parameter = []
    for parameter in sig_inspect.parameters.values():
        if parameter.name not in skip_parameters:
            sig_parameter.append(parameter)

    print(sig_inspect)
    sig_replaced = sig_inspect.replace(parameters=sig_parameter)
    print(sig_replaced)
