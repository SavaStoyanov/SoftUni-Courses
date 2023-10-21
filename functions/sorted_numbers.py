number = input().split()
numbers_digits = []
for numbers in number:
    numbers_digits.append(int(numbers))
print(sorted(numbers_digits))