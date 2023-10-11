lenght = int(input())
width = int(input())
height = int(input())
percentage_occupied = float(input()) / 100

volume = lenght * width * height
volume_in_Litres = volume * 0.001
volume_with_water = volume_in_Litres * (1-percentage_occupied)

print(f'{volume_with_water} litres')