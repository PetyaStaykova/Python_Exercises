def sum_numbers(num_1, num_2, num_3):
    return (num_1 + num_2) - num_3


first_num = int(input())
second_num = int(input())
third_num = int(input())
total = sum_numbers(first_num, second_num, third_num)
print(total)