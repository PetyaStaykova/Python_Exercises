n = int(input())

for i in range(n):
    line = ' ' * (n - i - 1) + '* ' * (i + 1)
    print(line)
for i in range(n - 2, -1, -1):
    line = ' ' * (n - i - 1) + '* ' * (i + 1)
    print(line)
