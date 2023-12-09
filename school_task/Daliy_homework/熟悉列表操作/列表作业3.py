my_list = [1, 2, 3, 4, 5]

# 列表增加：使用append()方法在末尾添加元素
my_list.append(6)
print(my_list)  # 输出: [1, 2, 3, 4, 5, 6]

# 列表删除：使用remove()方法删除指定元素
my_list.remove(3)
print(my_list)  # 输出: [1, 2, 4, 5, 6]

# 列表查找：使用index()方法查找元素索引
index = my_list.index(5)
print(f"Index of 5: {index}")  # 输出: Index of 5: 3
#列表的增加、删除、查找方法