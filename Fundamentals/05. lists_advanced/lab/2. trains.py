wagons = int(input())
train_length = [0] * wagons
command = input()

while not command == 'End':
    command_data = command.split()
    if command_data[0] == 'add':
        train_length[-1] += int(command_data[1])
    elif command_data[0] == 'insert':
        index = int(command_data[1])
        people = int(command_data[2])
        train_length[index] += people
    elif command_data[0] == 'leave':
        index = int(command_data[1])
        people = int(command_data[2])
        train_length[index] -= people
    command = input()

print(train_length)