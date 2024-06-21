n = int(input())
counter0 = 1
counter1 = 0
for i in rangerange(n):
    summ = counter1 + counter0
    counter0 = counter1
    counter1 = summ
    print(summ, end=" ")
