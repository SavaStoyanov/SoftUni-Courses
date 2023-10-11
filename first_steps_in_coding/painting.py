protective_nylon_amount = int(input())
paint_amount = int(input())
paint_thinner_amount = int(input())
worker_hours = int(input())

protective_nylon_price = (protective_nylon_amount + 2) * 1.50
paint_price = (paint_amount * 1.10) * 14.50
paint_thinner_price = paint_thinner_amount * 5

total_materials = protective_nylon_price + paint_price + paint_thinner_price + 0.40
workers_per_hour = total_materials * (30 / 100)
workers = workers_per_hour * worker_hours

print(total_materials + workers)

