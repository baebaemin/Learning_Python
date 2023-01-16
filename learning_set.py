dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)
sum = set()

for i in dice1:
    for j in dice2:
        sum.add(i + j)
print(sum)