budget = float(input())
videocard_bought = int(input())
processor_bought = int(input())
ram_bought = int(input())

videocard_cost = videocard_bought * 250
ram_cost = ram_bought * (videocard_cost * 0.10)
processor_cost = processor_bought * (videocard_cost * 0.35)

total = videocard_cost + ram_cost + processor_cost

if videocard_bought > processor_bought:
    total = total * 0.85

if budget > total:
    money_left = budget - total
    print(f'You have {money_left:.2f} leva left!')

else:
    money_needed = total- budget
    print(f'Not enough money! You need {money_needed:.2f} leva more!')



