n_lines = int(input())
stack = []
for _ in range(n_lines):
    command = input().split()
    if '1' in command:
        number = int(command[1])
        stack.append(number)
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))
reversed_nums = []
while stack:
    reversed_nums.append(str(stack.pop()))
print(', '.join(reversed_nums))