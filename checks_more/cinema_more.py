type_of_cinema = input()
rows = int(input())
columns = int(input())
price_ticket = 0

cinema_capacity = rows * columns

if type_of_cinema == 'Premiere':
    price_ticket = 12
elif type_of_cinema == 'Normal':
    price_ticket = 7.50
elif type_of_cinema == 'Discount':
    price_ticket = 5

income = price_ticket * cinema_capacity
print(f'{income:.2f}')
