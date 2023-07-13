#Задача №3

#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

#Решение :

n = int(input("Введите число:"))
for i in range(n):
    power_of_two = 2 ** i
    if power_of_two <= n:
        print(power_of_two)
   
        

