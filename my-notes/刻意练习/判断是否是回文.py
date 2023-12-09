# # def if_same(n):
# #     pass
# n = str(input("请输入一个字符串:"))
# # for i in range(len(n), 0):
# n = list[n]
# s = [::-1]
#

def if_name(s):
    s = s.strip().lower()
    return s == s[: : -1]
string = input("请输入一个字符串:")
if if_name(string):
    print("是回文序列")
else:
    print('不是回文序列')
#我真是厉害啊卧槽