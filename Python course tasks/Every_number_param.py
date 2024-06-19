num = int(input())
lnum = num
summ = 0
counter = 0
prod = 1
while num > 0:
    last_n = num %  10
    summ = summ + last_n
    counter += 1
    prod = prod * last_n
    num =  num  //  10
avg = summ  /  counter
first_n = (lnum % 10**counter) // 10**(counter - 1)
summ2 = lnum % 10 + first_n
print(summ, counter, prod, avg, first_n, summ2, sep="\n")
