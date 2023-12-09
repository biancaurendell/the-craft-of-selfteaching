my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# 使用Counter类统计元素出现次数
from collections import Counter
element_counts = Counter(my_list)
print(element_counts)