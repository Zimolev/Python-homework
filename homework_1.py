# Задача 2: Найдите сумму цифр трехзначного числа.
def task2():
    n = input("Введите трехзначное число: ")
    number = int(n)
    print(number // 100 + number // 10 % 10 + number % 100 % 10)
   
#task2()

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
def task4():
    s = int(input("Введите количество журавликов: "))
    if s < 6 or s % 6 != 0: 
        print("нельзя определить исходя из условмй задачи")
    else:
        print(f"Петя и Сережа сделали по {s / 6}")
        print(f"Катя сделала {4 * s / 6}")

#task4()

#Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

def taks6():
    lucky_ticket = int(input("Введите шестизначный номер билета: "))
    lucky_ticket_1 = lucky_ticket // 1000
    lucky_ticket_2 = lucky_ticket % 1000
    if (lucky_ticket_1 // 100 +
        lucky_ticket_1 // 10 % 10 +
        lucky_ticket_1 % 100 % 10) == (lucky_ticket_2 // 100 +
                                       lucky_ticket_2 // 10 % 10 +
                                       lucky_ticket_2 % 100 % 10):
       print("Your ticket is a lucky")
    else: 
        print("your ticket isnt a lucky")
   

taks6()

#Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.
def taks8():
    n = int(input("Введите длину шоколадки в дольках: "))
    m = int(input("Введите ширину шоколадки в дольках: "))
    k = int(input("Введите сколько хотите потломить долек: "))
    if k % n == 0 or k % m == 0:
        print('Yes')
    else: print('No')

#taks8()

