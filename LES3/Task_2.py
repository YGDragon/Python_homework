"""
2. Напишите программу, которая найдёт произведение пар чисел списка.
   Парой считаем первый и последний элемент, второй и предпоследний и т.д.
   Пример:
   [2, 3, 4, 5, 6] => [12, 15, 16];
   [2, 3, 5, 6] => [12, 15]
"""


# проверка ввода числа
def inp_check(numb):
    while not numb.isdigit():
        print('ошибка ввода!')
        numb = input('-> повторный ввод длины списка: ')
    return numb


len_lst = int(inp_check(input('ввод длины списка: ')))
new_lst = []
prod_lst = []
pair_lst = []
for i in range(len_lst):
    from random import randint
    new_lst.append(randint(1, len_lst))
print(f'исходный список -> {new_lst}')
for i in range(int(len_lst/2)):
    prod_lst.append(new_lst[i] * new_lst[(len_lst - 1) - i])
    pair_lst.append(str(new_lst[i]) + '*' + str(new_lst[(len_lst - 1) - i]))
print(f'{pair_lst} -> {prod_lst}')
