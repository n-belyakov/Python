mx = -(10**6) - 1
s = 0
counter = 0
for i in range(10):
    x = int(input())
    if x < 0:
        counter += 1
        s += x
    if x < 0 and x > mx:
        mx = x
if counter == 0:
    print("NO")
else:
    print(s)
    print(mx)
