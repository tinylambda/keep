if __name__ == "__main__":
    s = bytes("特朗普的最终结局会怎么样", encoding="utf-8")
    print(s, len(s))

    print(s[0])
    print(s[:1])

    s_arr = bytearray(s)
    print(s_arr)

    print(s_arr[-1:])
