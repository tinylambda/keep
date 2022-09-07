from typing import Any, Sequence

if __name__ == "__main__":
    comparison_ops = {"=", ">", ">=", "<", "<=", "!=", "<>", "between", "in"}
    logical_ops = {"and", "or", "not"}

    cond1 = ("and", (">", "UserProfile.vendor_type", 0))
    cond2 = (
        "and",
        (">", "UserProfile.vendor_type", 0),
        ("<=", "UserProfile.vendor_type", 2),
        ("<>", "UserProfile.vendor_type", 1),
        ("between", "UserProfile.age", [16, 20]),
        ("between", "UserProfile.age", ["a", "x"]),
        ("=", "UserProfile.name", "felix"),
        ("not", ("=", "UserProfile.name", "tom"), ("!=", "UserProfile.name", 1)),
        ("not", ("and", ("=", "a", "x"), ("=", "b", "y"))),
        ("in", "UserProfile.age", [18, 19, 20, 21]),
    )

    def parse(condition: Sequence[Any]) -> str:
        if not condition:
            return ""
        head, *tail = condition

        if head in logical_ops:
            # now head be one of: and/or/not
            if head == "not":
                # not is unary op
                return f" not ({' and '.join([parse(item) for item in tail])})"
            else:
                # or/and can combine many conditions
                return f" {head} ".join([parse(item) for item in tail])
        elif head in comparison_ops:
            col, arg = tail
            if head == "between":
                arg = " and ".join([repr(item) for item in arg])
            elif head == "in":
                arg = ", ".join([repr(item) for item in arg]).join(["(", ")"])
            else:
                arg = repr(arg)
            return f"{col} {head} {arg}"

    r = parse(cond2)
    print(r)
