quantity = int(input())
days = int(input())
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15
total_cost = 0
spirit = 0

for day in range(1, days +1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += price_ornament_set * quantity
        spirit += 5
    if day % 3 == 0:
        total_cost += (price_tree_skirt + price_tree_garlands) * quantity
        spirit += 13
    if day % 5 == 0:
        total_cost += price_tree_lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += price_tree_skirt + price_tree_garlands + price_tree_lights
        if day == days:
            spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')