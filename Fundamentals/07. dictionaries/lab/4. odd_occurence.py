words = input().split()
dictionary = {}

for i in words:
    lower_word = i.lower()
    if lower_word not in dictionary:
        dictionary[lower_word] = 0
    dictionary[lower_word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')