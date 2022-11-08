"""
3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
   Создать функцию сжатия строки и функцию восстановления строки.

   Пример:
          ABCDEFGH -> 1A1B1C1D1E1F1G1H -> ABCDEFGH
          WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR
"""


# функция жатия строки
def compress(text):
    encode = ''
    past_char = ''
    count = ''
    text += '_'
    for char in text:
        if char != past_char:
            encode += str(count) + past_char
            past_char = char
            count = 1
        else:
            count += 1
            past_char = char
    return encode


# функция восстановления строки
def restore(text):
    decode = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

row = 'CCCAAABCAADAADDAEFFHHH'
code = compress(row)
print(f'      исходная строка -> {row}')
print(f'        сжатая строка -> {code}')
print(f'восстановленая строка -> {restore(code)}')