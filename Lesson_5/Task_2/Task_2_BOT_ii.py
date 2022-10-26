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
user = {1: 'BOT', 2: 'GAMER'}
total = 220
lim0 = 1
lim1 = 28
step = 1
move = 0
u_gamer = 0
print(f'На столе {total} конфет')
print(f'Ходит {user[rand]}')
while move < total:
    for u in gamer:
        if u == 1:
            if step == 1:
                n_bot = total % (lim1 + lim0)
            elif step == 2:
                n_bot = (total - u_gamer) % (lim1 + lim0)
            else:
                n_bot = (lim1 + lim0 - u_gamer)
            move += n_bot
            print(f'Ход №{step} -> {user[1]}: {n_bot}')
        elif u == 2:
            u_gamer = min_max(check(input(f'Ход №{step} -> {user[u]}: ')), lim0, lim1)
            move += u_gamer
        step += 1
        res = total - move
        print(f'\t\t\t\t\t\tОсталось конфет {res}')
        if res <= lim1:
            print(f'\t\t\t\t\t\tВыйграл {user[1] if u == 2 else user[2]}')
            move = total
            break
