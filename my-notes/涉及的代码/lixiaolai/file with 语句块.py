import os

with open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthird line\n')

with open('C:/Users/22502/Desktop/python/lixiaolai/test-file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist.')

#删除了，但是为什么没有命令行反馈呢