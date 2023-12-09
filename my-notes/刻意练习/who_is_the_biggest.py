#找出最大/最小值： 编写一个函数，接收一个列表作为参数，并返回列表中的最大值或最小值
def the_biggest(list):
    return max(list)
def the_minest(list):
    return min(list)

my_list = [2, 4, 5, 8, 10]
print('最大值是', the_biggest(my_list))
print('最小值是', the_minest(my_list))


