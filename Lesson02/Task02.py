# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

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

def more_fib(num):
    if num == 1:
        return 1
    else:
        return num * more_fib(num - 1)

number = get_number()

list = []
for i in range(1, number + 1):
    list.append(more_fib(i))

print(list)
