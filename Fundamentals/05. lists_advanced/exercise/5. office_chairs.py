n_rooms = int(input())
free_seats = 0
enough_seats = True
for room in range(n_rooms):
    room_info = input().split()
    chairs = room_info[0]
    visitors = int(room_info[1])

    if len(chairs) >= visitors:
        free_seats += len(chairs) - visitors
    else:
        enough_seats = False
        seats_needed = visitors - len(chairs)
        print(f'{seats_needed} more chairs needed in room {room + 1}')
if enough_seats:
    print(f'Game On, {free_seats} free chairs left')