exam_time = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam_minutes = (exam_time * 60) + minute_exam
arrival_minutes = (hour_arrival * 60) + minute_arrival
diff_min = abs(arrival_minutes - exam_minutes)

if exam_minutes < arrival_minutes:
    print('Late')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{diff_min} minutes after the start')
elif arrival_minutes == exam_minutes or diff_min <= 30:
    print('On time')
    if diff_min > 0:
        print(f'{diff_min} minutes before the start')
else:
    print('Early')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours before the start')
    else:
        print(f'{diff_min} minutes before the start')
