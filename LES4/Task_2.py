"""
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
   Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.

Пример:
        simple_number(147420) => [2, 3, 5, 7, 13];
        simple_number(374220) => [2, 3, 5, 7, 11];
"""


def function(n):
    u_lst = []
    if n % 2 == 0:
        u_lst = [2]
        n = n // 2
    for i in range(3, n):
        if i % 2 != 0 and n % i == 0:
            cnt = 0
            for j in range(2, i):
                if i % j == 0:
                    cnt += 1
            if cnt == 0:
                n /= i
                u_lst.append(i)
    return u_lst


inp_number = 147420
print(function(inp_number))
