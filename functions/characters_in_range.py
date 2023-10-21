def all_the_characters(first:str, second:str):
    characters = []
    for  current_char in range(ord(first) + 1, ord(second)):
      characters.append(chr(current_char))
    return characters

first_char = input()
sec_char = input()
final_result = all_the_characters(first_char, sec_char)
print(' '.join(final_result))