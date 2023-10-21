def smallest(some_numbers:list):
    return min(some_numbers)

first_n = int(input())
second_n = int(input())
third_n = int(input())
smallest_element = smallest([first_n, second_n, third_n])

print(smallest_element)