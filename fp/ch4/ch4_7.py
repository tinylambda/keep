if __name__ == '__main__':
    s = '特朗普的最终结局会怎么样'
    r = s.encode('utf-8')
    print(r)

    r = s.encode('utf-16')
    print(r)

    # s.encode('iso8859-1')
    #
    r = s.encode('cp437', errors='ignore')
    print(r)
    r = s.encode('cp437', errors='replace')
    print(r)
    r = s.encode('cp437', errors='xmlcharrefreplace')
    print(r)

