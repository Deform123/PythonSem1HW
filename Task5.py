#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

x1 = int(input("Введите координату X первой точки: "))
y1 = int(input("Введите координату Y первой точки: "))
x2 = int(input("Введите координату X второй точки: "))
y2 = int(input("Введите координату Y второй точки: "))

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(distance)