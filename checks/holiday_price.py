holiday_cost = float(input())
puzzles_sold = int(input())
dolls_sold = int(input())
bears_sold = int(input())
minions_sold = int(input())
trucks_sold = int(input())

total_sold = puzzles_sold + dolls_sold + bears_sold + minions_sold + trucks_sold

puzzles_total = puzzles_sold * 2.60
dolls_total = dolls_sold * 3
bears_total = bears_sold * 4.10
minions_total = minions_sold * 8.20
trucks_total = trucks_sold * 2

total_profit = puzzles_total + dolls_total + bears_total + minions_total + trucks_total
if total_sold >= 50:
    total_profit = total_profit * 0.75

clean_profit = total_profit * 0.90
money_left = clean_profit - holiday_cost
money_needed = holiday_cost - clean_profit

if clean_profit > holiday_cost:
    print(f'Yes!{money_left: .2f} lv left.')

else:
    print(f'Not enough money!{money_needed: .2f} lv needed.')

