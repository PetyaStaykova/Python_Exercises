nums_as_str = input().split(', ')
numbers = [int(n)for n in nums_as_str]
step = 10
while numbers:
    new_nums_list = []
    for i in numbers:
        if i <= step:
            new_nums_list.append(i)
    for x in new_nums_list:
        numbers.remove(x)
    print(f'Group of {step}\'s: {new_nums_list}')
    step += 10
