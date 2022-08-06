# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def sum_fraction_part(list):
    if len(list) > 0:
        min = abs(list[0]) % 1
        max = abs(list[0]) % 1
        for i in range(0, len(list)):
            fraction = abs(list[i]) % 1
            if fraction < min:
                min = fraction
            if fraction > max:
                max = fraction
        return (max - min) * 100 // 1 / 100
    else:
        return 'List is null'


list = [1.1, -1.2, 3.1, 5, 10.01]
print(sum_fraction_part(list))