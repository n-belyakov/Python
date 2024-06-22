a = int(input())
divider = 0
for j in range(1, a + 1):
    for i in range(1, j + 1):
        if j % i == 0:
            divider += 1
    print(i, divider * "+", sep=" ")
    divider = 0
