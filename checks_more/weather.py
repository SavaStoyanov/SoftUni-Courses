temperature = int(input())
time_of_day = input()
outfit = ''
shoes = ''

wrong_data = False

if time_of_day == 'Morning':
    if 10 <= temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        wrong_data = True

if time_of_day == 'Afternoon':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temperature >= 25:
        outfit = 'Swimsuit'
        shoes = 'Barefoot'
    else:
        wrong_data = True

if time_of_day == 'Evening':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        wrong_data = True

if wrong_data:
    print('Error')
else:
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
