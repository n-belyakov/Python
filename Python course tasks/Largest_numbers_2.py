n = int(input())
largest = 0
largest2 = 0
for _ in range(n):
    m = int(input())
    if m >= largest:
        largest2 = largest
        largest = m
    elif m >= largest2:
        largest2 = m
print(largest, largest2, sep="\n")
