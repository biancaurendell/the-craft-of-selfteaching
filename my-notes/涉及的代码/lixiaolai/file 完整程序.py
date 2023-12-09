# with open('words_alpha.txt') as file:
#     for word in file.readlines():
#         pass #先用pass占个位
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

#print(sum_of_word('attitude'))
with open('results.txt', 'w') as result:
    with open('words_alpha.txt', 'r') as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                result.write(word)
#改进一下呗 —— 倒也简单，在计算前把读入字符串前后的空白字符都给删掉就好了，用 str.strip() 就可以了：
#想要把符合条件的词保存到一个文件results.txt中，那么


