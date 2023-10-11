n = int(input())
word = input()
list = []
list_2 = []

for _ in range(n):
    curr_word = input()
    list.append(curr_word)
    if word in curr_word:
        list_2.append(curr_word)

print(list)
print(list_2)
