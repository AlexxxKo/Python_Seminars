# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

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

def negafib_fib(num):
    list = []
    a, b = 1, 1
    for i in range(num-1):
        list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(num):
        list.insert(0, a)
        a, b = b, a - b
    return list

number = get_number()
print(number)
print(negafib_fib(number))