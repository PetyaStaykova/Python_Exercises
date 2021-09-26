from collections import deque
food_quantity = int(input())
orders = deque([int(n) for n in input().split()])
biggest_order = max(orders)
print(biggest_order)
while orders:
    food_wanted = orders[0]
    if food_wanted <= food_quantity:
        food_quantity -= food_wanted
        orders.popleft()
    else:
        break
if orders:
    print(f'Orders left: {" ".join(str(n) for n in orders)}')
else:
    print(f'Orders complete')