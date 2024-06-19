##n = int(input())
##counter0 = 1
##counter1 = 0
##for i in range(n):
##    summ = counter1 + counter0
##    counter0  = counter1
##    counter1 = summ
##    print(summ, end=' ')
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))