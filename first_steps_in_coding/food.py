chicken_menus = int(input()) * 10.35
fish_menus = int(input()) * 12.40
vegeterian_menus = int(input()) * 8.15

dessert = (chicken_menus + fish_menus + vegeterian_menus) * 0.20
total = chicken_menus + fish_menus + vegeterian_menus + dessert + 2.50

print(total)

