if __name__ == '__main__':
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1.append(100)

    print(l1, '\n', l2)
    print(
        l1[1] is l2[1]
    )
    print(l1[2] is l2[2])

    l1[1].remove(55)
    print(l1, '\n', l2)

    l2[1] += [33, 22]
    l2[2] += (10, 11)

    print(l1[2] is l2[2])
    print(l1, '\n', l2)

