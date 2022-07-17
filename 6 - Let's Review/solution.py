number_of_words = int(input())

for _ in range(number_of_words):
    word = input()
    print(word[0::2] + ' ' + word[1::2])
