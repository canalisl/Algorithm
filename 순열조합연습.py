from itertools import permutations, combinations

array = [1, 2, 4, 20, 5, 30, 29, 0, 6, 7, 11]

data = permutations(array, 3)
answer = []
for i in data:
  if sum(i) == 40:
    answer.append(i)
    print(i)
print(len(answer))