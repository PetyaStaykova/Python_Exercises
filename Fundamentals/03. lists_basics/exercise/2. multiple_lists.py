factor = int(input())
count = int(input())
multiplies_list = []

for num in range(1, count + 1):
    new_number = num * factor
    multiplies_list.append(new_number)

print(multiplies_list)