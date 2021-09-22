def calculate_factorial(number):
    factorial = 1
    for n in range(2, number + 1):
        factorial *= n
    return factorial


def factorial_division(factorial_1, factorial_2):
    return factorial_1 / factorial_2


num_1 = int(input())
num_2 = int(input())
f_1 = calculate_factorial(num_1)
f_2 = calculate_factorial(num_2)
result = factorial_division(f_1, f_2)
print(f'{result:.2f}')