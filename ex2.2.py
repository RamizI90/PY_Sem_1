#""" Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве. 
#Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """

a_x = int(input("Введите первый координат х: "))
a_y = int(input("Введите первый координат y: "))
b_x = int(input("Введите второй координат х: "))
b_y = int(input("Введите второй координат y: "))

lengthSegment = ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** (0.5)
print('Длина отрезка: ', format(lengthSegment, '.3f'))