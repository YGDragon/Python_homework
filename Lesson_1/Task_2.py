"""
2. Напишите программу для проверки истинности утверждения
   ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""


def check_predicate(data):
    print()
    print(f'Для X = {data[0]}, Y = {data[1]}, Z = {data[2]}')
    if (not (data[0] or data[1] or data[2])) == \
       (not data[0] and not data[1] and not data[2]):
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')


def fill_list():
    num_list = []
    i = 0
    while i < 3:
        try:
            v = int(input('Ввод числа X, Y, Z: '))
        except ValueError:
            v = -1
        num_list.append(v)
        i += 1
    return num_list


values = fill_list()
check_predicate(values)
