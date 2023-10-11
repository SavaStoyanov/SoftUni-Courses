movie_budget = float(input())
number_of_actors = int(input())
costume_cost = float(input())

decor = movie_budget * 0.10
costume_price = number_of_actors * costume_cost

if number_of_actors >= 150:
 costume_price = costume_price * 0.90

total_cost = decor + costume_price
money_left = movie_budget - total_cost
money_needed = total_cost - movie_budget

if movie_budget > total_cost:
 print(f'Action!')
 print(f'Wingard starts filming with{money_left: .2f} leva left.')

else:
 print(f'Not enough money!')
 print(f'Wingard needs{money_needed: .2f} leva more.')
