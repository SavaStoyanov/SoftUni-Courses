import math

series_name = str(input())
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
relax_time = break_lenght / 4

time_free = break_lenght - lunch_time - relax_time
time_left = abs(time_free - episode_lenght)
time_left_real = math.ceil(time_left)

if time_free >= episode_lenght:
    print (f'You have enough time to watch {series_name} and left with {time_left_real} minutes free time.')

else:
    print (f"You don't have enough time to watch {series_name}, you need {time_left_real} more minutes.")
