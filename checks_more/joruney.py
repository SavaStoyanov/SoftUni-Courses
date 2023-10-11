budget = float(input())
season = input()
place = ''
type = ''
price = 0


if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        type = 'Camp'
        price = budget * 0.30
    elif season  == 'winter':
        type = 'Hotel'
        price = budget * 0.70
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        type = 'Camp'
        price = budget * 0.40
    elif season  == 'winter':
        type = 'Hotel'
        price = budget * 0.80
elif budget > 1000:
    season == 'summer' or season == 'winter'
    place = 'Europe'
    type = 'Hotel'
    price = budget * 0.90

print(f'Somewhere in {place}')
print(f"{type} - {price:.2f}")


