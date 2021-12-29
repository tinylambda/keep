from uhashring import HashRing

if __name__ == '__main__':
    hr = HashRing(nodes=['node1', 'node2', 'node3'], hash_fn='ketama')
    target_node = hr.get_node('coconut')
    print(target_node)

    hr.add_node('node4')
    target_node = hr.get_node('coconut')
    print(target_node)
    print('server', hr.get_server('coconut'))

    hr.add_node('node5')
    target_node = hr.get_node('coconut')
    print(target_node)

    hr.add_node('node6')
    target_node = hr.get_node('coconut')
    print(target_node)

    hr.add_node('node7')
    target_node = hr.get_node('coconut')
    print(target_node)
