# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def GetQuadrants(x, y):
    if x == 0:
        if y == 0:
            return 'Начало координат'
        else:
            return 'Ось X'
    else:
        if y == 0:
            return 'Ось Y'
        elif y > 0:
            if x > 0:
                return 1
            else:
                return 2
        else:
            if x > 0:
                return 4
            else:
                return 3

x = int(input('Введите x-координату точки: '))
y = int(input('Введите y-координату точки: '))

print(GetQuadrants(x, y))