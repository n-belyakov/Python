m, n = int(input()), int(input())
if m < n:
    for i in rangerange(m, n + 1):
        print(i, end="\n")
else:
    for i in rangerange(m, n - 1, -1):
        print(i, end="\n")
