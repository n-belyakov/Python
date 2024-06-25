numbers = [
    2,
    6,
    3,
    14,
    10,
    4,
    11,
    16,
    12,
    5,
    4,
    16,
    1,
    0,
    8,
    16,
    10,
    10,
    8,
    5,
    1,
    11,
    10,
    10,
    12,
    0,
    0,
    6,
    14,
    8,
    2,
    12,
    14,
    5,
    6,
    12,
    1,
    2,
    10,
    14,
    9,
    1,
    15,
    1,
    2,
    14,
    16,
    6,
    7,
    5,
]

length = len(numbers)
last_number = numbers[-1]
rev = numbers[::-1]
if 5 and 17 in numbers:
    flag = "YES"
else:
    flag = "NO"
del numbers[0]
del numbers[-1]
print(length, last_number, rev, flag, numbers, sep="\n")
