def validator(pas):
   list_of_errors = []
   if len(pas) < 6 or len(pas) > 10:
       list_of_errors.append('Password must be between 6 and 10 characters')
   if not pas.isalnum():
        list_of_errors.append('Password must consist only of letters and digits')
   digits_counter = 0
   for character in pas:
       if character.isdigit():
           digits_counter += 1
   if digits_counter < 2:
               list_of_errors.append('Password must have at least 2 digits')
   return list_of_errors

password = input()
valid_password = validator(password)
if len(valid_password) == 0:
    print('Password is valid')
else:
    print('\n'.join(valid_password))