actor_name = input()
points_academy = float(input())
evaluators = int(input())

for _ in range(evaluators):
    name = input()
    ev_points = float(input())
    lenght = len(name)

    points = (lenght * ev_points) / 2

    points_academy += points
    if points_academy >= 1250.5:
        break

if points_academy >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points_academy:.1f}!')
else:
        print(f'Sorry, {actor_name} you need {1250.5 - points_academy:.1f} more!')

