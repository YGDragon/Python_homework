"""
4. Напишите программу, которая по заданному номеру четверти,
   показывает диапазон возможных координат точек в этой четверти (x и y).
"""


def check_area(value):
    area_list = ['1', '2', '3', '4']
    while value not in area_list:
        print('Неверный ввод!', end=' ')
        value = input('Требуется ввод номера от 1 до 4: ')
    if value in area_list[0]:
        print(f'Четверть №{value} -> (x > 0; y > 0)')
    elif value in area_list[1]:
        print(f'Четверть №{value} -> (x < 0; y > 0)')
    elif value in area_list[2]:
        print(f'Четверть №{value} -> (x < 0; y < 0)')
    elif value in area_list[3]:
        print(f'Четверть №{value} -> (x > 0; y < 0)')


check_area(input('Ввод номера четверти: '))
