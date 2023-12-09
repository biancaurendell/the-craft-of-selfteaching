a_list = ['first line\n', 'second line\n', 'third line\n']
f = open('C:/Users/22502/Desktop/python/lixiaolai/test-file2.txt', 'w')
f.writelines(a_list)
f.close()

f = open('C:/Users/22502/Desktop/python/lixiaolai/test-file2.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
#将列表写入文件然后迭代输出该列表
