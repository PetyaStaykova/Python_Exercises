n = int(input())
word = input()
list_of_all = []
special_list = []

for i in range(n):
  frase = input()
  list_of_all.append(frase)
  
  if word in frase:
    special_list.append(frase)

print(list_of_all)
print(special_list)