def list_manipulator(numbers: list, command: str, direction: str, *args):
    if command == 'add':
        if direction == 'beginning':
            i = 0
            for arg in args:
                numbers.insert(i, arg)
                i += 1
        else:
            for arg in args:
                numbers.append(arg)
    if command == 'remove':
        if direction == 'beginning':
            if len(args) == 0:
                numbers = numbers[1:]
            else:
                count = args[0]
                numbers = numbers[count:]
        else:
            if len(args) == 0:
               numbers = numbers[:-1]
            else:
                count = args[0]
                numbers = numbers[:-count]
    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))