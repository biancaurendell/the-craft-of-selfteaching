my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# 删除指定键的元素
del my_dict['age']
print(my_dict)

# 使用pop()方法删除并返回指定键的元素
city = my_dict.pop('city')
print(my_dict)
print(f"Removed city: {city}")
