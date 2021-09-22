n_people = int(input())
capacity = int(input())
result = 0
if n_people % capacity == 0:
    result = n_people / capacity
else:
    result = (n_people // capacity) + 1

print(int(result))