# Задача 16: Требуется вычислить, 
#сколько раз встречается некоторое число X в массиве A[1..N].
from random import randint

def task16():
    size = int(input("Введите размер массива: "))
    massiv = [randint(0, 10) for _ in range(size)]
    print(massiv)
    number = int(input("Введите число: "))
    count = 0
    for i in range(len(massiv)):
        if massiv[i] == number:
            count += 1
    print(count)
# второй вариант
    result1 = [massiv[i] for i in range(len(massiv)) if massiv[i] == number]
    print(result1, len(result1))
    
task16()