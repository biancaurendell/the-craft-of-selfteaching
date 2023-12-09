import sys
print(sys.path)

#指定检索目录在何处
# sys.path.append("")
# import my_module

#系统内建的模块

print(sys.builtin_module_names)
print("_sre" in sys.builtin_module_names) # True
print("math" in sys.builtin_module_names) # False （根据自己电脑库的安装情况，结果会有不同）


from mycode import is_prime
print(is_prime(3))

#引入使用化名
import this
import __hello__
