# def say_hi(greeting, *names):
#     for names in names:
#         print(f'{greeting}, {names.capitalize()}!')
#
# say_hi('Hello', 'mike', 'john', 'zeo')

#为函数的某些参数设定默认值
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hello', 'mike', 'john', 'zeo')
say_hi('Hello', 'mike', 'john', 'zeo', capitalized=True)

# 设计可以接受一系列值的关键字参数
