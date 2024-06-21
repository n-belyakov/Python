n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit or digit == 0:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print("NO")
else:
    print(max_digit)
