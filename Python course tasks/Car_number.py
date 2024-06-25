s = input()
letter = "АВЕКМНОРСТУХ"
num = "1234567890"
s_l = s[0] + s[4:6]
s_n = s[1:4] + s[7:]
if (
    s[0] in letter
    and s[4] in letter
    and s[5] in letter
    and s_n.isdigit() == True
    and s[6] == "_"
) and 5 <= len(s_n) <= 6:
    print("YES")
else:
    print("NO")
