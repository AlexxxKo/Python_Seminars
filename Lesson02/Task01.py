# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def get_number():
    num = input('Введите вещественное число: ')
    return num

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        print('Не число\n')
        return False

def set_int(number):
    number = float(number)
    while number % 10 != 0:
        number *= 10
    return int(number)

def sum_digit(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum

while True:
    x = get_number()
    if is_number(x):
        print(f'{x} - число')
        y = set_int(x)
        sum = sum_digit(y)
        print(f'{sum} - сумма цифр')
        break