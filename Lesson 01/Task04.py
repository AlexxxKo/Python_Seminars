# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant = int(input('Введите номер четверти: '))

if quadrant == 1:
    print('Возможные координаты: x = (0, infinity), y = (0, infinity)')
elif quadrant == 2:
    print('Возможные координаты: x = (0, -infinity), y = (0, infinity)')
elif quadrant == 3:
    print('Возможные координаты: x = (0, -infinity), y = (0, -infinity)')
elif quadrant == 4:
    print('Возможные координаты: x = (0, infinity), y = (0, -infinity)')
else:
    print('Такой четверти на плоскости ещё не придумали')