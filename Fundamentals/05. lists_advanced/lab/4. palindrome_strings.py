words_list = input().split()
searched = input()

all_pal = [word for word in words_list if word == word[::-1]]

print(all_pal)
print(f'Found palindrome {all_pal.count(searched)} times')