from inspect import signature


def clip(text, max_len=80):
    """doc here"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


if __name__ == "__main__":
    print(clip.__defaults__)

    print(clip.__code__)  # doctest: +ELLIPSIS

    print(clip.__code__.co_varnames)

    print(clip.__code__.co_argcount)

    sig = signature(clip)
    print(sig)

    for name, param in sig.parameters.items():
        print(param.kind, ":", name, "=", param.default)
