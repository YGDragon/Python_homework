"""
5. (Усложненное). Даны два файла, в каждом из которых находится запись многочлена.
   Задача - сформировать файл, содержащий сумму многочленов.
   Выделите необходимые действия, этапы алгоритма.
   Посмотрите какие из них уже решены в предыдущей задаче.
   Оформите необходимые функции в виде модуля и импортируйте.
   Примечание:
              Многочлены в файлах могут быть разной степени
"""

from functions import write_file as w
from functions import read_file as r
from functions import find_cof
s1 = find_cof(r('polynom_file1.txt').strip(' = 0').split(' + '))
s2 = find_cof(r('polynom_file2.txt').strip(' = 0').split(' + '))
print(s1)
print(s2)
sum_cof = []
if len(s1) > len(s2):
    for i in range(1, len(s2) + 1):
        sum_cof.append(s1[-i][0] + s2[-i][0])
    for i in range(len(s2), len(s1)):
        sum_cof.append(s1[-i - 1][0])
if len(s1) < len(s2):
    for i in range(1, len(s1) + 1):
        sum_cof.append(s2[-i][0] + s1[-i][0])
    for i in range(len(s1), len(s2)):
        sum_cof.append(s2[-i - 1][0])
result = str(list(reversed(sum_cof)))
w('sum_polynom.txt', result)
