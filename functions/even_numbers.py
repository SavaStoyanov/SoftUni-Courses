number_as_string = input().split()
numbers_digits = []
for number in number_as_string:
    numbers_digits.append(int(number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_digits))
print(result)