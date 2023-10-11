import math

videocard_price =int(input())
transmiter_price = int(input())
energy_per_day = float(input())
profit_per_day = float(input())

vc_t = videocard_price * 13
tr_t = transmiter_price * 13
total = vc_t + tr_t + 1000
profit = profit_per_day - energy_per_day
profit_t = profit * 13
days_needed = math.ceil(total / profit_t)

print(total)
print(days_needed)