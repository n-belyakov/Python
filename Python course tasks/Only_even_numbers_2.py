counter = 0
for _ in range(10):
    if int(input()) % 2 == 0:
        counter += 1
print("YES" if counter == 10 else "NO")
