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
    while True:
        place = input('Введите кооординаты: ').split()
        if len(place)!=2:
            print('Введите две координаты')
            continue

        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x,y=map(int, place)
        if not(x >= 0 and x<3 and y>=0 and y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

users_input(field)

field=[['-']*3 for _ in range(3)]
count = 0
while True:
    if count==9:
        print('Ничья')
        break
    if count%2==0:
        user = 'x'
    else:
        user = '0'
    show_field(field)
    x,y=users_input(field)
    field[x][y]=user
    count+=1
