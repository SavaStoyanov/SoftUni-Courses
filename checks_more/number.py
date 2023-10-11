dessert = input()
orders = int(input())
day = int(input())
price = 0
discount = 0

if dessert == 'Cake':
    if day <= 15:
        price = 24
    else:
        price = 28.70
elif dessert == 'Souffle':
    if day <= 15:
        price = 6.66
    else:
        price = 9.80
elif dessert == 'Baklava':
    if day <= 15:
        price = 12.60
    else:
        price = 16.98
else:
    if day <= 15:
        price = 6.66
    else:
        price = 9.80


total = price * orders

if day <= 22 and 100 <= total <= 200:
    discount = 0.85
elif day <= 22 and total > 200:
    discount = 0.75

total_new = total * discount
if day <= 15:
    total_new = total_new * 0.90


print(f'{total_new:.2f}')

