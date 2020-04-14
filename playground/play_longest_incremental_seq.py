#coding=utf-8
# 给出一个数组序列，找出其中最长的递增子序列
# 比如给出[2, 5, 7, 6, 4, 7, 9]   ->  2, 5, 6, 7, 9
from collections import defaultdict


def find_max_continuous_list(original_list, current_index, cont_cache=defaultdict(list)):
    assert cont_cache[current_index] == []
    if current_index > (len(original_list) - 1):
        return cont_cache
    else:
        before_list = original_list[:current_index]
        current_number = original_list[current_index]

        max_before_index = None
        for before_index in range(len(before_list)):
            before_number = before_list[before_index]
            if current_number > before_number:
                if len(cont_cache[before_index]) > len(cont_cache[max_before_index]):
                    max_before_index = before_index

        if max_before_index is not None:
            cont_cache[current_index].extend(cont_cache[max_before_index])
        cont_cache[current_index].append(current_number)

        return find_max_continuous_list(original_list, current_index+1, cont_cache)


l = [2, 5, 7, 6, 4, 7, 9]
l = [3, 2, 5, 3, 4, 7]
l = [1, 2, 6, 3, 4, 5, 6]
result = find_max_continuous_list(l, 0)
print(l)
print(result)
max_key = None
for key in result:
    if max_key is None:
        max_key = key
    else:
        max_key_list = result[max_key]
        key_list = result[key]
        if len(key_list) > len(max_key_list):
            max_key = key
print(result[max_key])





