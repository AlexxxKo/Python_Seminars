# Вычислить число pi c заданной точностью d

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите точность числа pi (количество знаков после запятой). Максимум 48: '))
            if num and 0 < num < 49:
                is_num = True
        except ValueError:
            print('Нужно ввести целое положительное число\n')
    return num

def set_pi():
    k = 1
    s = 0
    for i in range(1000000):
        if i % 2 == 0:
            s += 4 / k
        else:
            s -= 4 / k
        k += 2
    return s

print(f'{set_pi(): .{get_number()}f}')