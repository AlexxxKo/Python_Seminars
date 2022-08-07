# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k

import random

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите натуральную степень k: '))
            if num and num > 0:
                is_num = True
        except ValueError:
            print('Нужно ввести целое положительное число\n')
    return num

def get_random_list(num):
    rand_list = [random.randint(0,101) for i in range(num + 1)]
    return rand_list

def get_str(num):
    b = ''
    rand_list = get_random_list(num)
    for i in range(num + 1):
        if rand_list[i] != 0:
            if i == 0:
                b = str(rand_list[i])
            elif i == 1:
                b = f'{rand_list[i]}x + {b}'
            else:
                b = f'{rand_list[i]}x^{i} + {b}'
    b += ' = 0'
    return(b)

def write_file(st):
    with open('Homework04_Task04.txt', 'w') as data:
        data.write(st)

write_file(get_str(get_number()))