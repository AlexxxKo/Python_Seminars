# Напишите программу, которая будет преобразовывать десятичное число в двоичное
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

def decimal_binary(num):
    rest = ''
    while num > 0:
        rest = str(num % 2) + rest
        num //= 2
    return int(rest)

number = get_number()
print(number)
print(decimal_binary(number))


