def sum_of_word(words):
    sum =0
    for char in words:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    with open('result.txt', 'w') as result:
        for words in file.readlines():
            if sum_of_word(words.strip()) == 204:
                print(result.write(words))
                print(words)

