def sum_of_100(words):
    sum = 0
    for char in words:
        sum += ord(char) - 96
        #if sum == 100:
    return sum #居然在这里被卡了这么久，就是因为一个缩进问题，what the fuck

with open('the end.txt', 'w') as end:
    with open('words_alpha.txt', 'r') as file:
        for words in file:
            if sum_of_100(words.strip()) == 100:
                print(words, end.write(words))
                #print(words)


