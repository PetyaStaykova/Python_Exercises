gifts_list = input().split()
command = input()

while not command == 'No Money':
    command_list = command.split()
    command_type = command_list[0]
    gift = command_list[1]

    if command_type == 'OutOfStock':
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = 'None'
    elif command_type == 'Required':
        index_to_replace = int(command_list[2])
        for i in range(len(gifts_list)):
            if i == index_to_replace and len(gifts_list) >= index_to_replace:
                gifts_list[i] = gift
    elif command_type == 'JustInCase':
        for i in gifts_list:
            gifts_list[-1] = gift

    command = input()

while 'None' in gifts_list:
    gifts_list.remove('None')
print(' '.join(gifts_list))
