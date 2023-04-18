# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X . 
# Если таких значений больше одного, вывести первый найденный.

from random import randint

def task18():
    size = int(input("Введите размер массива: "))
    massiv = [randint(0, 10) for _ in range(size)]
    print(massiv)
    number = int(input("Введите число: "))
    diff_modulus = number
    x = 0
    for i in range(len(massiv)):
        if diff_modulus > abs(massiv[i] - number):
            diff_modulus = abs(massiv[i] - number)
            x = i
    print(massiv[x])

task18()
