note = input()
to_do = [0] * 10
while note != 'End':
    importance, task = note.split('-')
    importance = int(importance) - 1
    to_do[importance] = task
    note = input()
print([task for task in to_do if task != 0])