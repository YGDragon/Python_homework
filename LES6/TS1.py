"""
1. Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200.
   Использовать comprehensions
"""


def gen_list(n: int) -> list:
    lst = [el for el in range(0, n) if (el ** 2 < 200 and el % 2 != 0)]
    return lst


num = 20
print(gen_list(num))
