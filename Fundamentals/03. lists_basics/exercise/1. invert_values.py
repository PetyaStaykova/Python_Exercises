list_of_strings = input().split(' ')
list_of_opposite = []

for i in range(0, len(list_of_strings)):
    list_of_strings[i] = int(list_of_strings[i]) * (-1)
    list_of_opposite.append(list_of_strings[i])

print(list_of_opposite)