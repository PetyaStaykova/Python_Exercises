working_day_events = input().split('|')
energy = 100
coins = 100
not_broken = True

for event in working_day_events:
    event_type, value = event.split('-')
    value = int(value)
    if event_type == 'rest':
        energy += value
        if energy > 100:
            energy -= value
            value = 0

        print(f'You gained {value} energy.')
        print(f'Current energy: {energy}.')
    elif event_type == 'order':
        energy -= 30
        coins += value
        if energy >= 0:
            print(f'You earned {value} coins.')
        else:
            energy += 80
            coins -= value
            print(f'You had to rest!')
    else:
        if coins > value:
            coins -= value
            print(f'You bought {event_type}.')
        else:
            coins += value
            print(f'Closed! Cannot afford {event_type}.')
            not_broken = False
            break

if not_broken:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')