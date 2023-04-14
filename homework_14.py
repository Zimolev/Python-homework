# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

number = int(input("Введите число: "))
count = 1
while True:
    two_degree = 2 ** count
    if two_degree > number:
        break
    count += 1
    print(two_degree)
    