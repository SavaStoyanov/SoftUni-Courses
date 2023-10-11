n_comps = int(input())
st_points = int(input())
points = 0
wins = 0

for _ in range(n_comps):
    success = input()

    if success == 'W':
        points += 2000
        wins += 1
    elif success == 'F':
        points += 1200
    elif success == 'SF':
        points += 720

    total_points = st_points + points
    average_points = points / n_comps
    percent_win = wins / n_comps * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points:.0f}')
print(f'{percent_win:.2f}%')