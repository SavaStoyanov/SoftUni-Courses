loses = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
helmet_broken = loses // 2
sword_broken = loses // 3
shield_broken = loses // (2*3)
armor_broken = shield_broken // 2
total = (helmet * helmet_broken) + (sword_broken * sword) + (shield_broken * shield) + (armor_broken * armor)
print(f'Gladiator expenses: {total:.2f} aureus')



