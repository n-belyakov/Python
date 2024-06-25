s_list = []
n = int(input())
for _ in range(n):
    s = input()
    s_list.append(s)
k = int(input())
for i in range(n):
    letter_order = s_list[i]
    if len(letter_order) < k:
        continue
    letter_order = letter_order[k - 1]
    print(letter_order, end="")
