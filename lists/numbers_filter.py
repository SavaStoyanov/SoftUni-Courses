n = int(input())
numbers = []

for _ in range(n):
    curr_n = int(input())
    numbers.append(curr_n)

command = input()

filtered = []

if command == 'even':
        for number in numbers:
            if number % 2 == 0:
                filtered.append(number)
elif command == 'odd':
        for number in numbers:
            if number % 2 != 0:
                filtered.append(number)
elif command == 'positive':
        for number in numbers:
            if number >= 0:
                filtered.append(number)
elif command == 'negative':
        for number in numbers:
            if number < 0:
                filtered.append(number)

print(filtered)

