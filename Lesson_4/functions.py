# функция записи строки-полинома в файл
def write_file(filename, sum_polynom):
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(sum_polynom)


# функция чтения строки-полинома из файла
def read_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        polynom = file.read()
    return polynom


# функция вычисления коэффициентов полинома
def find_cof(lst):
    s = []
    for i in range(len(lst)):
        num = [int(el) for el in lst[i] if el.isdigit()]
        print(num)
        # проверка для степени x^2 и >
        if len(num) >= 2 and lst[i].count('x^') == 1:
            n0 = num.pop(len(num) - 1)
            n1 = int(''.join([str(el) for el in num if str(el).isdigit()]))
            num = [n1, n0]
        elif len(num) == 1 and lst[i].count('x^') == 1:
            num.insert(0, 1)
        # проверка для степени 0
        elif len(num) == 1 and lst[i].count('x') == 0:
            num.insert(1, 0)
        elif len(num) >= 2 and lst[i].count('x') == 0:
            n = int(''.join([str(el) for el in num if str(el).isdigit()]))
            num = [n, 0]
        # проверка для степени x
        elif len(num) == 0:
            num.insert(0, 1)
            num.insert(1, 1)
        elif len(num) == 1 and lst[i].count('x') == 1:
            num.insert(1, 1)
        elif len(num) >= 2 and lst[i].count('x') == 1:
            n = int(''.join([str(el) for el in num if str(el).isdigit()]))
            num = [n, 1]
        s.append([num[0], num[1]])
    return s
