num = int(input())
counter = 0
if num < 5:
    while num != 0:
        num -= 1
        counter += 1
elif num < 10:
    while num != 0:
        if num > 4:
            num -= 5
            counter += 1
        else:
            num -= 1
            counter += 1
elif num < 25:
    while num != 0:
        if num >= 10:
            num -= 10
            counter += 1
        elif num > 4:
            num -= 5
            counter += 1
        else:
            num -= 1
            counter += 1
elif num >= 25:
    while num != 0:
        if num >=25 :
            num -= 25
            counter += 1
        elif num >=10:
            num -= 10
            counter += 1
        elif num >=5:
            num -= 5
            counter += 1
        else:
            num -= 1
            counter += 1
print(counter)


    
