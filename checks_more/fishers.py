budget = int(input())
season = input()
number_fishers = int(input())
price = 0
discount = 0
bonus_discount = 0

wrong_data = False

if season == 'Summer':
    price = 4200
elif season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600
elif season == 'Spring':
    price = 3000
else:
    wrong_data = True

if not season == 'Autumn' and number_fishers % 2 == 0:
     bonus_discount = 0.05

if number_fishers <= 6:
    discount = 0.10
elif 7 <= number_fishers <= 11:
    discount = 0.15
else:
    discount = 0.25

total_discount = discount + bonus_discount
total = price * (1 - total_discount)
money_status = abs(budget - total)

if wrong_data:
    print('Error')
elif budget > total:
    print(f"Yes! You have {money_status:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_status:.2f} leva.")





