n = int(input())
synonym_dictionary = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonym_dictionary:
        synonym_dictionary[word] = []
    synonym_dictionary[word].append(synonym)

for word in synonym_dictionary:
    print(f'{word} - {", ".join(synonym_dictionary[word])}')