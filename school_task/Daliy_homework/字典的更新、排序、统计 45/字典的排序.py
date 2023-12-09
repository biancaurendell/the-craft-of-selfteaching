my_dict = {'b': 3, 'a': 1, 'c': 2}

# 按键排序
sorted_dict_by_keys = sorted(my_dict.items(), key=lambda x: x[0])
print(sorted_dict_by_keys)

# 按值排序
sorted_dict_by_values = sorted(my_dict.items(), key=lambda x: x[1])
print(sorted_dict_by_values)
