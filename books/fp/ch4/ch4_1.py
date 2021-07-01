if __name__ == '__main__':
    s = '特朗普的最终结局会怎么样'
    print(len(s))
    b = s.encode('utf-8')
    print(b)
    print(len(b))
    print(b.decode('utf-8'))

