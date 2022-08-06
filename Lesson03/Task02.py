# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def sum_pair(list):
    if len(list) > 1:
        last_index = len(list) - 1
        sum_list = []
        for i in range(0, len(list)):
            if last_index - i > i:
                sum_list.append(list[i] + list[last_index - i])
        return sum_list
    else:
        return 'List length < 2'

list1 = [2, 3, 4, 5, 7]
list2 = [2, 3, 5, 7]

print(sum_pair(list1))
print(sum_pair(list2))