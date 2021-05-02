import random

# 1.Поле 3*3
#
# 2. ОПрос точки
# 3. Кто выйграл
# 4. Взаимодействие блоков

#var1
field = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]
print(field)
#var2
field = [['-']*3 for _ in range(3)]
print(field)

print(*field)
#VAR_3
print('  0 1 2')
for i in range(len(field)):
    print(str(i), *field[i])
#var_4
print('  0 1 2')
for i in range(len(field)):
    print(str(i)+' '+' '.join(field[i]))
