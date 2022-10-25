"""
2. Создайте программу для игры с конфетами человек против человека.
   Условие задачи:
                  На столе лежит некоторое кол-во конфет, например 220.
                  Играют два игрока делая ход друг после друга.
                  Первый ход определяется жеребьёвкой.
                  За один ход можно забрать не более чем 28 конфет.
                  Все конфеты оппонента достаются сделавшему последний ход.

Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
   Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые точно определят победу.
"""
from random import randint
from check_functions import check
from check_functions import min_max
# алгоритм - задача Баше
rand = randint(1, 2)
gamer = [rand, 1 if rand == 2 else 2]
user = {1: 'GAMER-1', 2: 'GAMER-2'}
total = 220
limit0 = 0
limit1 = 28
step = 1
move = 0
print(f'На столе {total} конфет')
print(f'Ходит {user[rand]}')
while move < total:
    for u in gamer:
        move += min_max(check(input(f'Ход №{step} -> {user[u]}: ')), limit0, limit1)
        step += 1
        res = total - move
        print(f'\t\t\t\t\t\tОсталось конфет {res}')
        if res <= limit1:
            print(f'\t\t\t\t\t\tВыйграл {user[1] if u == 2 else user[2]}')
            move = total
            break
