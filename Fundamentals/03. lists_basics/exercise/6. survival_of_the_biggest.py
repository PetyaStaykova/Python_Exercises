numbers = input().split()
n = int(input())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for j in range(n):
    min_number = min(numbers)
    numbers.remove(min_number)
for k in range(len(numbers)):
    numbers[k] = str(numbers[k])

print(', '.join(numbers))
