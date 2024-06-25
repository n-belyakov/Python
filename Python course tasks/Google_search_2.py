n = int(input())
n_list = []
for _ in range(n):
    s = input()
    n_list.append(s)
k = int(input())
k_list = []
cnt = 0
for _ in range(k):
    s1 = input()
    k_list.append(s1)
for i in range(n):
    for j in range(k):
        k_compare = k_list[j]
        n_compare = n_list[i]
        if k_compare.lower() in n_compare.lower():
            cnt += 1
    if cnt == k:
        print(n_list[i])
    cnt = 0
