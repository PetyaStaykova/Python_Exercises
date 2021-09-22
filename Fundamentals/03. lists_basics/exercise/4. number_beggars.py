money_str = input().split(',')
beggars = int(input())
sum_of_each_beggar = []
start_index = 0

for beggar in range(1, beggars + 1):
    current_sum = 0
    for sum in range(start_index, len(money_str), beggars):
        current_sum += int(money_str[sum])
    sum_of_each_beggar.append(current_sum)
    start_index += 1


print(sum_of_each_beggar)