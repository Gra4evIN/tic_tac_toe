import random

# 1.Поле 3*3
#
# 2. ОПрос точки
# 3. Кто выйграл
# 4. Взаимодействие блоков

#var1 переменная с отртсовкой поля
field = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]
print(field)
#var2
#field = [['-']*3 for _ in range(3)]
#print(field)

#print(*field)
#VAR_3
#print('  0 1 2')
#for i in range(len(field)):
#    print(str(i), *field[i])
#var_4
#print('  0 1 2')
#for i in range(len(field)):
#    print(str(i)+' '+' '.join(field[i]))

#var with 'a b c'
#num=' a b c'
#print(num)
#for row, i in zip(field,num.split()):
#    print(f"{i} {' '.join(str(j) for j in row)}")

#функция отрисовки поля
def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))
show_field(field)

#опрос пользователя
def users_input(f):
    place = input('Введите кооординаты: ').split()
    if len(place)!=2:
        print('Ввведите две координаты')
        continue
users_input(field)
