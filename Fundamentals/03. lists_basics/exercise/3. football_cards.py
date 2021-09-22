A_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

red_cards = input().split()
terminated = False

for i in red_cards:
    card_info = i.split('-')
    team = card_info[0]
    player = int(card_info[1])
    if team == "A" and player in A_team:
        A_team.remove(player)
    elif team == "B" and player in B_team:
        B_team.remove(player)
    if len(A_team) < 7 or len(B_team) < 7:
        terminated = True
        break
print(f'Team A - {len(A_team)}; Team B - {len(B_team)}')

if terminated:
    print('Game was terminated')
