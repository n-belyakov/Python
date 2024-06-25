n = int(input())
counter_3 = 0
counter_last_digit = 0
counter_div_2 = 0
summ_more_5 = 0
product_more_7 = 1
counter_0_5 = 0
first_last_digit = n % 10
while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        counter_3 += 1
    if last_digit == first_last_digit:
        counter_last_digit += 1
    if last_digit % 2 == 0:
        counter_div_2 += 1
    if last_digit > 5:
        summ_more_5 += last_digit
    if last_digit > 7:
        product_more_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        counter_0_5 += 1
    n = n // 10
print(
    counter_3,
    counter_last_digit,
    counter_div_2,
    summ_more_5,
    product_more_7,
    counter_0_5,
    sep="\n",
)
