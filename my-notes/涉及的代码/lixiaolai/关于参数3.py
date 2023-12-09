#设计可以接受一系列值的关键字参数
# def say_hi(**names_greetings):
#     for name, greeting in names_greetings.items():
#         print(f'{greeting}, {name}!')
#
# say_hi(mike='Hello', ann='Oh, my darling', john='Hi')

#调用函数直接使用字典形式
# def say_hi(**names_greetings):
#     for name, greeting in names_greetings.items():
#         print(f'{greeting}, {name}!')
# a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
# say_hi(**a_dictionary)
# say_hi(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})

#函数定义时各种参数的排列顺序

def say_hi(*names, greeting='Hello' , capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
say_hi('mike', 'john', 'zeo', greeting='Hi')
#这是因为函数被调用时，面对许多参数，python需要按照既定的规则，顺序，判断每个参数究竟是哪一类参数


