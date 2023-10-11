number_of_pens = int(input())
number_of_markers = int(input())
number_of_cleaners = int(input())
discount = int(input()) / 100

pens = number_of_pens * 5.80
markers = number_of_markers * 7.20
cleaners = number_of_cleaners * 1.20
total = pens + markers + cleaners

print(total - (total * discount))