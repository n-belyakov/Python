n = int(input())
for i in range(1, n + 1):

    for k in range(1, i):
        print(k, end=" ")

    for r in range(i, 0, -1):

        print(r, end="")
    print()
