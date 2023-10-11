string = input()
coffee = 0
while string != 'End':
    if string.lower() == 'coding' or string.lower() == 'cat' or string.lower() == 'dog' or string.lower() == 'movie':
        if string.islower():
           coffee += 1
        else:
           coffee += 2
    string = input()
if coffee <= 5:
    print(coffee)
else:
    print(f'You need extra sleep')