n = int(input())
positives = []
negatives = []
positive_count = 0

for i in range(n):
  number = int(input())
  if number >= 0:
    positives.append(number)
    positive_count += 1
  else:
    negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {positive_count}. Sum of negatives: {sum(negatives)} ')