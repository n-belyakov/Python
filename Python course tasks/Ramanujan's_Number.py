a, b, c, d = int(), int(), int(), int()
counter = 0
for a in range(1, 33):
    for c in range(1, a):
        for d in range(1, c):
            for b in range(1, d):
                if a**3 + b**3 == c**3 + d**3:
                    print(a**3 + b**3)
