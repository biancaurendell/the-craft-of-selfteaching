#如何写函数
#定义一个啥都不干的函数
def do_nothing():
    pass
do_nothing()

# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('if'))

#不接受任何参数的函数
def do_something():
    print('This is a hello message from do_something().')
do_something()

#没有return 语句的函数
def do_something():
    print('This is a hello message from do_something().')
if not do_something():
    print("The return value of 'do_something()'is None")

#接受外部传递进来的值

