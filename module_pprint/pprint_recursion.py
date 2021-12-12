from pprint import pprint

if __name__ == '__main__':
    local_data = ['a', 'b', 1, 2]
    local_data.append(local_data)

    print('id(local_data) =>', id(local_data))
    pprint(local_data)
