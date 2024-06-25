s = input()
if (
    s[0] == "@"
    and s[1:] == s[1:].lower()
    and 5 <= len(s) <= 15
    and s[1:].isalnum() == True
):
    print("Correct")
else:
    print("Incorrect")
