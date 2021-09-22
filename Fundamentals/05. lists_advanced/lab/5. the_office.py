happiness_str = list(map(lambda el: int(el), input().split()))
factor = int(input())
multiplied = list(map(lambda i: i * factor, happiness_str))
avarage = sum(multiplied) / len(multiplied)
happy_employees = list(filter(lambda e: e > avarage, multiplied))
half = len(multiplied) / 2
if len(happy_employees) >= half:
    print(f'Score: {len(happy_employees)}/{len(multiplied)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(multiplied)}. Employees are not happy!')