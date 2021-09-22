targets_as_str = input().split()
targets = [int(target) for target in targets_as_str]
command = input()

while not command == 'End':
    name, index, value = command.split()
    index = int(index)
    value = int(value)
    if name == 'Shoot':
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif name == 'Add':
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif name == 'Strike':
        start_index = index - value
        end_index = index + value
        if index in range(len(targets)) and start_index in range(len(targets))\
            and end_index in range(len(targets)):
            del targets[start_index: end_index + 1]
        else:
            print('Strike missed!')
    command = input()

result = [str(target) for target in targets]

print('|'.join(result))