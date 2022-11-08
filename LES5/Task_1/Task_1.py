"""
1. Напишите программу, удаляющую из текста все слова, содержащие "abc".
   Примечание Текст находится в файле.
              Его надо считать, текст исправить, исправленный текст записать в новый файл.
              Использовать вложенный менеджер контекста
"""
# исходный текс
# Mondayabc, abcTuesday, Wednesdayabc, abcThursday, Fridayabc
from funcs import write_file as w
from funcs import read_file as r
temp_str = r('Correct_text.txt').replace('abc', '')
w('Correct_text.txt', temp_str)
