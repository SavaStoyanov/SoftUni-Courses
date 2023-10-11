command = input()
adult = 0
kid = 0
m_f_t = 0
m_f_s = 0

while command != 'Christmas':
    age = int(command)
    if age > 16:
        adult += 1
    else:
        kid += 1

m_f_t = kid * 5
m_f_s = adult * 15


print(f'Number of adults: {adult}')
print(f'Number of kids: {kid}')
print(f'Money for toys: {m_f_t}')
print(f'Money for sweaters: {m_f_s}')



