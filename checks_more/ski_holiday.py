days_spent = int(input())
type_room = input()
feedback = input()

price_per_night = 0
total = 0
discount = 0
final_total = 0

if type_room == 'room for one person':
    price_per_night = 18
elif type_room == 'apartment':
    price_per_night = 25
    if days_spent < 10:
        discount = price_per_night * (days_spent - 1) * 0.30
    elif 10 <= days_spent >= 15:
        discount = price_per_night * (days_spent - 1) * 0.35
    else:
        discount = (price_per_night * (days_spent - 1)) * 0.50
else:
    price_per_night = 35
    if days_spent < 10:
        discount = (price_per_night * (days_spent - 1)) * 0.10
    elif 10 <= days_spent >= 15:
        discount = (price_per_night * (days_spent - 1)) * 0.15
    else:
        discount = (price_per_night * (days_spent - 1)) * 0.20

total = price_per_night * (days_spent - 1) - discount

if feedback == 'positive':
    final_total = total * 1.25
else:
    final_total = total * 0.90


print(f'{final_total:.2f}')

