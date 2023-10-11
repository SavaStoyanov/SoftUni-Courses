world_record = float(input())
distance = float(input())
seconds_for_meter = float(input())

water_resistance = distance // 15 * 12.5

total_time = seconds_for_meter * distance + water_resistance
time_needed = total_time - world_record

if total_time < world_record:
 print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')

else:
 print(f'No, he failed! He was {time_needed:.2f} seconds slower.')


