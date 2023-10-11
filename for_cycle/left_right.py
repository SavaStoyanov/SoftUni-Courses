n = int(input())
first_sum = 0
current_number = 0

for _ in range(0, n)
    current_number = int(input())
    first_sum = first_sum + current_number

second_sum = 0
for _ in range(0, n):
    current_number = int(input())
    second_sum = second_sum + current_number

if first_sum == second_sum:
    print(f'Yes, sum = {abs(first_sum)}')
else:
    print(f'No, diff = {abs(first_sum - second_sum)}')

