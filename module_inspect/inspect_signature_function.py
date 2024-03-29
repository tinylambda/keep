import inspect

import module_inspect.example as example


sig = inspect.signature(example.module_level_function)
print("module_leve_function{}".format(sig))

print("\nParameter details:")
for name, param in sig.parameters.items():
    if param.kind == inspect.Parameter.POSITIONAL_ONLY:
        print("{} (positional-only)".format(name))
    elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
        if param.default != inspect.Parameter.empty:
            print("{}={!r}".format(name, param.default))
        else:
            print("{}".format(name))
    elif param.kind == inspect.Parameter.VAR_POSITIONAL:
        print("*{}".format(name))
    elif param.kind == inspect.Parameter.KEYWORD_ONLY:
        if param.default != inspect.Parameter.empty:
            print("{}={!r} (keyword-only)".format(name, param.default))
        else:
            print("{} (keyword-only)".format(name))
    elif param.kind == inspect.Parameter.VAR_KEYWORD:
        print("**{}".format(name))
