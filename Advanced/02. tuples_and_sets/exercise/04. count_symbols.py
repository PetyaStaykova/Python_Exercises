text = input()
letters = {}

for ch in text:
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

for letter, count in sorted(letters.items()):
    print(f'{letter}: {count} time/s')