# Задача 22: Даны два неупорядоченных набора целых чисел 
#(может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

def task22():
    size_one = int(input("Введите размер первого массива: "))
    massiv_one = [randint(0, 10) for _ in range(size_one)]
    size_two = int(input("Введите размер второго массива: "))
    massiv_two = [randint(0, 10) for _ in range(size_two)]
    print(massiv_one)
    print(massiv_two)

# 1 вариант
    massiv_one_set = set(massiv_one)
    massiv_two_set = set(massiv_two)
    print(massiv_one_set.union(massiv_two_set))

# 2 Вариант
    for i in massiv_two:
        massiv_one.append(i)

    print(set(massiv_one))

# 3 Вариант
   # пробовал через set(massiv_one.extend(massiv_two)) не вышло


task22()
