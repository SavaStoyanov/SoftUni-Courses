def perfect(some_number):
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    return divisors_sum


number = int(input())
if perfect(number) == number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")