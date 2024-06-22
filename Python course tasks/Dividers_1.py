a, b = int(input()), int(input())
divider = 0
sum = 0
for j in range(a, b + 1):
    for i in range(1, j + 1):
        if j % i == 0:
            divider += i

    if divider >= sum:
        sum = divider
        num = i
    divider = 0
print(num, sum, sep=" ")
