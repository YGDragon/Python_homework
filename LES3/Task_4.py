"""
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
   Пример:
   45 -> '101101'
   3 -> '11'
   2 -> '10'

   Примечание: Результат вернуть в виде строки. Не использовать функции преобразования типов: bin
"""


# проверка ввода числа
def inp_check(numb):
    while not numb.isdigit():
        print('ошибка ввода!')
        numb = input('-> повторный ввод числа: ')
    return numb


unum = int(inp_check(input('ввод числа: ')))
line = ''
while unum >= 1:
    line = line + str(unum % 2)
    unum = int(unum / 2)
print(f'{line[::-1]} -> {type(line)}')
