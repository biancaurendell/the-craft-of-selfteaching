# import re
#
# # 定义邮政编码的正则表达式模式
# zip_code_pattern = r'^\d{5}(?:-\d{4})?$'  # 例如：12345 或 12345-6789
#
# # 用户输入
# user_input = input("请输入邮政编码：")
#
# # 使用正则表达式检查输入是否符合模式
# if re.match(zip_code_pattern, user_input):
#     print("输入的邮政编码格式正确！")
# else:
#     print("输入的邮政编码格式不正确，请重新输入。")
import re
phone_number_pattern = r'^(\+?0?86-?)?1[3-9]\d{9}$'
user_input = input("请输入你的手机号:")
if re.match(phone_number_pattern, user_input):
    print("You are right")
else:
    print("error")
