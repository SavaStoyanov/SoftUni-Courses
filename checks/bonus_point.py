start_bonus = int(input())
bonus_points = 0

if start_bonus <= 100:
    bonus_points = 5

elif 1000 > start_bonus > 100:
    bonus_points = start_bonus * 0.20

elif start_bonus >= 1000:
    bonus_points = start_bonus * 0.10

if start_bonus % 2 == 0:
    bonus_points = bonus_points + 1

elif start_bonus % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(start_bonus + bonus_points)

