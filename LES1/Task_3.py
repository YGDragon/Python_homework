"""
3. Напишите программу, которая принимает на вход
   координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
   и выдаёт номер четверти плоскости, в которой находится эта точка
   (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""


def check_area(x_value, y_value):
    if x_value > 0 and y_value > 0:
        print(f'X={x_value}; Y={y_value} -> 1')
    elif x_value < 0 < y_value:
        print(f'X={x_value}; Y={y_value} -> 2')
    elif x_value < 0 and y_value < 0:
        print(f'X={x_value}; Y={y_value} -> 3')
    elif x_value > 0 > y_value:
        print(f'X={x_value}; Y={y_value} -> 4')


def check_input(name):
    num = 0
    while type(num) != float:
        try:
            num = float(input())
        except ValueError:
            print('Ошибка ввода!', end=' ')
            print(f'Для {name} требуется число : ', end='')
    return num


def check_0(num, name):
    while num == 0:
        print('Ошибка - введен ноль!', end=' ')
        print(f'Требуется повторный ввод значения для {name}: ', end='')
        num = check_input(name)
    return num


print('Ввод значения X: ', end='')
x = check_0(check_input('X'), 'X')
print('Ввод значения Y: ', end='')
y = check_0(check_input('Y'), 'Y')
check_area(x, y)
