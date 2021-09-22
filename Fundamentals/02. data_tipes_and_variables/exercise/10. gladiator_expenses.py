lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        broken_helmet += 1
    if fight % 3 == 0:
        broken_sword += 1
    if fight % 6 == 0:
        broken_shield += 1
    if fight % 12 == 0:
        broken_armor += 1
money_spend = (broken_helmet * helmet_price) + (broken_sword * sword_price) + (broken_shield * shield_price) + (broken_armor * armor_price)
print(f'Gladiator expenses: {money_spend:.2f} aureus')
