def sum_numbers(first, second):
     return  first + second

def subtract(result, third):
    return result - third

def add_and_subtract(first, second, third):
    result = sum_numbers(first, second)
    final_result = subtract(result, third)
    return final_result


first_n = int(input())
second_n = int(input())
third_n = int(input())

print(add_and_subtract(first_n, second_n, third_n))