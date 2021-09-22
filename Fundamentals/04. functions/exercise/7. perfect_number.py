def perfect_number(num):
    proper_divisors = []
    for current_num in range(1, num):
        if num % current_num == 0:
            proper_divisors.append(current_num)
        if sum(proper_divisors) == num:
            return True
    return False


number_from_input = int(input())
if perfect_number(number_from_input):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
