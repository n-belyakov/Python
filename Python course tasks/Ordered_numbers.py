num = int(input())
num_reverse = 0
flag = "YES"
while flag == "YES" and num > 0:
    last_digit = num % 10
    if last_digit >= num_reverse:
        flag ="YES"
        num_reverse = last_digit
    else:
        flag = "NO"
    num = num // 10
print(flag)