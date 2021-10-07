n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    element = input()
    first_set.add(element)
for _ in range(m):
    element = input()
    second_set.add(element)
result = first_set.intersection(second_set)
[print(element) for element in result]