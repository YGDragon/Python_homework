# 5. Реализуйте алгоритм перемешивания элементов списка.
# Без функции shuffle из модуля random, другие методы использовать можно.
3. Пробегаемся по всем элементам слева
от первого до последнего и меняет текущий
элемент со случайным элементом из правой части
местами.

def sequence(lst):
    from random import randint
    for i in range(6):
        lst.append(randint(0, 6))
    return lst
    
def mix(lst):
    from random import choice
    for i in range(len(lst)):
        n0 = lst[i]
        cnt = lst.count(n0)
        print(f'cnt -> {cnt}')
        lst.pop(i)
        print(f'i -> {i}', end='   ')
        print(f'n0 -> {n0}')
        print(f'промежуточный {lst}')
        n1 = 0
        idx = 0
        if n0 not in lst:
            cnt0 = 0
            n1 = choice(lst)
            idx = lst.index(n1)
            print(f'idx -> {idx}', end='   ')
            print(f'n1 -> {n1}')
            lst.insert(i, n1)
            lst.pop(idx + 1)
            lst.insert(idx  + 1, n0)
        else:
            lst.insert(i, n0)
        print(f'новый -> {lst}')
        print('')
    return lst
    
lst = []
print(lst)
print(sequence(lst))
print(f'перемешанный список -> {mix(lst)}')
