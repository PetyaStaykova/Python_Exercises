from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees_capacity = [int(x) for x in input().split(', ')]

pizza_counter = 0
while orders and employees_capacity:
    current_order = orders.popleft()
    employee = employees_capacity.pop()
    if current_order > 10 or current_order <= 0:
        employees_capacity.append(employee)
        continue
    if current_order == employee:
        pizza_counter += employee
    if current_order < employee:
        pizza_counter += current_order
    else:
        orders.appendleft(current_order - employee)
        pizza_counter += employee


if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizza_counter}')
    print(f'Employees: {", ".join([str(x) for x in employees_capacity])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in orders])}')

