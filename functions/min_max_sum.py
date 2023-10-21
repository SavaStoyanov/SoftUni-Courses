number = input().split()
numbers_digits = []
for numbers in number:
    numbers_digits.append(int(numbers))

minimum_number = min(numbers_digits)
maximum_number = max(numbers_digits)
sum_numbers = sum(numbers_digits)


print(f'The minimum number is {minimum_number}')
print(f'The maximum number is {maximum_number}')
print(f'The sum number is: {sum_numbers}')