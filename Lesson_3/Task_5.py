"""
5. Задайте число.
   Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
   Пример:
   - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


# проверка ввода числа
def inp_check(numb):
    while not numb.isdigit():
        print('ошибка ввода!')
        numb = input('-> повторный ввод количества идексов: ')
    return numb


def neg_fib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return neg_fib(n + 2) - neg_fib(n + 1)


def fib(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


result_lst = []
unum = int(inp_check(input('ввод количества идексов: ')))
for i in range(-unum, unum + 1):
    if i < 0:
        result_lst.append(neg_fib(i))
    else:
        result_lst.append(fib(i))
print(f'количество индексов = {unum} -> список чисел {result_lst}')
