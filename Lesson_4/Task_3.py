"""
3. Задайте последовательность чисел.
   Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""

from random import randint
seq = [randint(1, 20) for _ in range(1, 10)]
print(f'исходный список  -> {seq}')
new_seq = set(seq)
seq.clear()
for i in new_seq:
    seq.append(i)
print(f'найденный список -> {seq}')
