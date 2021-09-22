# numbers = list(map(lambda n: int(n), input().split(', ')))

numbers_as_str = input().split(', ')
numbers = [int(num) for num in numbers_as_str]

positive_numbers = [str(num)for num in numbers if num >= 0]
negative_numbers = [str(num)for num in numbers if num < 0]
even_numbers = [str(num)for num in numbers if num % 2 == 0]
odd_numbers = [str(num)for num in numbers if num % 2 != 0]

print(f'Positive: {", ".join(positive_numbers)}')
print(f'Negative: {", ".join(negative_numbers)}')
print(f'Even: {", ".join(even_numbers)}')
print(f'Odd: {", ".join(odd_numbers)}')
