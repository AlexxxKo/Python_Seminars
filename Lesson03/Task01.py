# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_list(list):
    sum = 0
    for i in range(0, len(list)):
        if i % 2:
            sum += list[i]
    return sum

list = [1, 2, 9, 15, 28, 17, 98]
print(sum_list(list))