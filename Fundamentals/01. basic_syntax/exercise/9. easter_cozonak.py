budget = float(input())
one_kg_flour = float(input())
price_eggs = 0.75 * one_kg_flour
price_milk = (one_kg_flour + 0.25 * one_kg_flour) * 0.25
price_cozonac = one_kg_flour + price_eggs + price_milk
cozonac_count = 0
colored_eggs_count = 0
money_left = budget

while budget >= price_cozonac:
    money_left -= price_cozonac
    cozonac_count += 1
    colored_eggs_count += 3
    if cozonac_count % 3 == 0:
        colored_eggs_count -= (cozonac_count - 2)
    budget = money_left
print(f'You made {cozonac_count} cozonacs! Now you have {colored_eggs_count} eggs and {money_left:.2f}BGN left.')