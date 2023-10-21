def factorial(some_number):
    for current in range(1, some_number):
        some_number *= current
    return some_number

first_n = int(input())
second_n = int(input())
f_f = factorial(first_n)
s_f = factorial(second_n)
final = f_f / s_f
print(f'{final:.2f}')