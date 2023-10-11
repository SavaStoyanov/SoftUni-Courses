age = int(input())
price = float(input())
toy_price = int(input())

saved_money = 0
toys_count = 0
brother = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        saved_money += int(year/2) * 10
        brother += 1
    else:
        toys_count += 1

toys_total = toys_count * toy_price
money = toys_total + saved_money - brother
diff = abs(money - price)

if money > price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')