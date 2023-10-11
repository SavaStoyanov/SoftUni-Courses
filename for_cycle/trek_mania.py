n_groups = int(input())
total_climbers = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for _ in range(n_groups):
    current_n_group = int(input())
    total_climbers += current_n_group

    if current_n_group <= 5:
        musala += current_n_group
    elif 6 <= current_n_group <= 12:
        monblan += current_n_group
    elif 13 <= current_n_group <= 25:
        kilimandjaro += current_n_group
    elif 26 <= current_n_group <= 40:
        k2 += current_n_group
    elif current_n_group >= 41:
        everest += current_n_group

musala_sum = musala / total_climbers * 100
monblan_sum = monblan / total_climbers * 100
kilimandjaro_sum = kilimandjaro / total_climbers * 100
k2_sum = k2 / total_climbers * 100
everest_sum = everest / total_climbers * 100

print(f'{musala_sum:.2f}%')
print(f'{monblan_sum:.2f}%')
print(f'{kilimandjaro_sum:.2f}%')
print(f'{k2_sum:.2f}%')
print(f'{everest_sum:.2f}%')
