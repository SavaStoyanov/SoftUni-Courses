def even_odd_sum(some_number:str):
    even_n = 0
    odd_n = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            even_n += int(digit)
        else:
            odd_n +=int(digit)
    return odd_n, even_n

number = input()
sum_of_odd_digits, sum_of_even_digits = even_odd_sum(number)
print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')