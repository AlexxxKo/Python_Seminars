# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

with open('Task04.txt', 'w') as data:
    data.write('0\n')
    data.write('2\n')
    data.write('3\n')
    data.write('5\n')
    data.write('2\n')

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое положительное число: '))
            if num > 0:
                is_num = True
            else:
                print('Число не положительное\n')
        except ValueError:
            print('Не целое число\n')
    return num

def set_list(num):
    list = []
    for i in range(-num, num + 1):
        list.append(randint(-num, num))
    return list

def get_data_from_file(path):
    data = open(path, 'r')
    filelist = [int(line.strip()) for line in data]
    data.close()
    return filelist

def get_mult(list, positionlist):
    mult = 1
    for i in positionlist:
        if i <= len(list) - 1:
            mult *= list[i]
    return mult

num = get_number()
list = set_list(num)
path = 'Task04.txt'
filelist = get_data_from_file(path)

print(num)
print(list)
print(get_mult(list, filelist))