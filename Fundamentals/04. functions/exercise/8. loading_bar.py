def loading_bar(number):
    initial_bar = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    if number == 0:
        return initial_bar
    n = number // 10
    for index in range(n):
        initial_bar[index] = '%'
    return initial_bar


num_from_data = int(input())
bar = loading_bar(num_from_data)
result_bar = ''.join(bar)

if bar.count('%') == 10:
    print('100% Complete!')
    print(f'[{result_bar}]')
else:
    print(f'{num_from_data}% [{result_bar}]')
    print('Still loading...')
