number_of_pages = int(input())
number_of_pages_per_hour = int(input())
days_to_read = int(input())

number_of_hours = number_of_pages / number_of_pages_per_hour
hours_per_day = number_of_hours / days_to_read

print(int(hours_per_day))