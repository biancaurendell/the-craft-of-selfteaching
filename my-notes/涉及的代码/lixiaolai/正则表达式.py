import string
print(string.ascii_letters)
print(string.digits)

#集合原子
#beg[iau]n能够代表begin began begun
import re

# str = 'begin began begun bigins begining'
# pttn = r'beg[iau]n'
# print(re.findall(pttn, str))

# str = 'defg,xyz,abcde,abcf,ghijkl'
# pttn = r'(?!.*abc).*$'
# print(re.findall(pttn,str) )

#类别原子
# import re
#
# str = str = '<dl>(843) 542-4256</dl> <dl>(431) 270-9664</dl>'
# pttn = r'\d\d\d\-'#这里指的是三个数字后面跟着一个- 的数字而已
# print(re.findall(pttn, str))

#边界原子
import re

# str = 'never ever verb however everest'
# pttn = r'er\b'
# print(re.findall(pttn, str))
# pttn = r'er\B'
# print(re.findall(pttn, str))

#组合原子
#数量操作符

with open('regex-target-text-sample.txt', 'r') as f:
    str = f.read()
pttn = r'go+gle'
print(re.findall(pttn, str))

pttn = r'go{2,5}gle'
print(re.findall(pttn, str))

pttn = r'colou?red'
print(re.findall(pttn, str))

pttn = r'520*'
print(re.findall(pttn, str))

#--------------------------
str = 'error wonderer severeness'

pttn = r'er'#er是两个整体,e在前，r在后
print(re.findall(pttn, str))

pttn = r'(er)'#er是一个整体原子
print(re.findall(pttn, str))

pttn = r'[er]'#e或者r
print(re.findall(pttn, str))

#那么接下来我要对数量进行操作了

pttn = r'er+'
print(re.findall(pttn, str))

pttn = r'[er]+'
print(re.findall(pttn, str))

pttn = r'(er)+'
print(re.findall(pttn, str))

#或操作符|
str = 'begin began begun begins beginn'
pttn = r'begin|began|begun'
print(re.findall(pttn, str))

str = 'achroiocythaemia achroiocythemia a|e'

pttn = r'[a|ae]'
print (re.findall(pttn, str))

pttn = r'[a|e]'
print(re.findall(pttn, str))

pttn = r'[ae]'
print(re.findall(pttn, str))

pttn = r'[(ae)]'
print(re.findall(pttn, str))

pttn = r'[a|ae|(ae)]'
print(re.findall(pttn, str))

#匹配并捕获
str = 'The white dog wears a black hat.'
pttn = r'The (white|black) dog wears a (white|black) hat'
print(re.findall(pttn, str))

rep1 = r'The \1 dog wears a \1 hat.'
print(re.sub(pttn, rep1, str)) #这里的意思很明显了，就是说证明替换是\1 \2这样替换的
rep1 = r'The \1 dog wears a \2 hat.'
print(re.sub(pttn, rep1, str))

#非捕获匹配
pttn = r'The (?:white|black) dog wears a (white|black) hat.'
print(re.findall(pttn, str))

#控制标记



