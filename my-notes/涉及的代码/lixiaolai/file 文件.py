# open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'w')
#
# #我们会把这个函数的返回值，一个所谓的file object保存到变量中，以仿版后面调用这个file object的各种Methods
# f = open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'w')
# print(f.name)
# f.close()

#删除文件,调用os模块
# import os
#
# if os.path.exists(f.name):
#     os.remove(f.name)
#     print(f'{f.name} deleted.')
# else:
#     print(f'{f.name} does not exist.')

#读写文件
f = open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'r')
# s = f.read()
# print(s)
# #f.close()

#文件有很多行的时候，我们可以用file.readline()操作，这个Method每次调用，都会返回文件中的新一行
# b = f.readline()
# print(b)
# b = f.readline()
# print(b)


#如何操作str.strip()
b = f.readline().strip()
print(b)
b = f.readline().strip()
print(b)


#使用file.readlines()这个Method将文件作为一个列表返回
b = f.readlines()#将文件内容返回成列表
print(b)

for line in f.readlines():
    print(line)


#使用file.writelines()将一个列表写入一个文件中，按索引顺序，逐行写入列表的对应元素
a_list = ['first line\n', 'second line\n', 'third line\n']
f.writelines(a_list)
f.close()  # 一定要带上这个操作的啊
f = open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()

#python 学习的最关键就是去官方网站学习

