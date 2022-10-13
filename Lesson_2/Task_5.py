# # 5. Реализуйте алгоритм перемешивания элементов списка.
# # Без функции shuffle из модуля random, другие методы использовать можно.

# проверка ввода числа
def inp_check(value):
    while type(value) == str:
        try:
            int(value)
        except ValueError:
            print('Ошибка ввода!')
            print(f'-> требуется ввод целого числа: -> ', end='')
            value = input()
        else:
            break
    return int(value)


# проверка ввода числа
def n0_check(value):
    while value <= 0:
        print('Ошибка ввода!')
        print(f'-> требуется ввод числа > 0: -> ', end='')
        value = inp_check(input())
    return int(value)


# алгоритм перемешивания элементов списка
def mix(data, size):
    data_1 = [i for i in range(0, size)]
    from random import choice
    for i in range(size):
        num = choice(data)
        idx = data.index(num)
        data_1[i] = num
        data.pop(idx)
    return data_1

num = n0_check(inp_check(input('ввод длины списка: ')))
lst = [i for i in range(0, num)]
print(f'....исходный список -> {lst}')
print(f'перемешанный список -> {mix(lst, num)}')
