"""
5. Напишите программу, которая принимает на вход координаты
   двух точек и находит расстояние между ними в 2D пространстве.
*Пример:*
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
Если вы не знаете как вычислить квадратный корень, оставьте квадрат расстояния
"""
import math


def calculate(a, b):
    result = math.sqrt((math.fabs(a[0] - b[0]) ** 2) + (math.fabs(a[1] - b[1]) ** 2))
    print(f'A ({a[0]}, {a[1]}); B ({b[0]}, {b[1]}) -> {result:<.2f}')


def fill_list():
    data = ['', '']
    i = 0
    while i < 2:
        data[i] = check_0(check_input())
        i += 1
    return data


def check_input():
    num = ''
    while type(num) != int:
        try:
            num = int(input())
        except ValueError:
            print('Ошибка ввода!', end=' ')
            print(f'Требуется ввод целого числа: ')
    return num


def check_0(num):
    while num == 0:
        print('Ошибка - введен ноль!', end=' ')
        print(f'Требуется повторный ввод числа: ', end='\n')
        num = check_input()
    return num


print('Ввод координат точки А: ')
a_dot = fill_list()
print('Ввод координат точки В: ')
b_dot = fill_list()
calculate(a_dot, b_dot)
