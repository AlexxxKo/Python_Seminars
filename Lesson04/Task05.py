# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

def get_number(text):
    is_num = False
    while not is_num:
        try:
            num = int(input(f'Введите натуральную степень {text} многочлена: '))
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
    return b

def write_file(st, file_name):
    with open(file_name, 'w') as data:
        data.write(st)

def read_file(file_name):
    with open(file_name, 'r') as data:
        st = data.readline()
    return st

def set_terms_degrees(st):
    st_list = st.replace(' ', '').split('=')
    st_list = st_list[0].split('+')
    for i in range(len(st_list)):
        st_list[i] = (st_list[i].split('x^'))
    return st_list

def sum_poly(lst1, lst2):
    lst1_terms = []
    lst2_terms = []
    for i in lst1:
        if len(i) == 2:
            lst1_terms.append(i[1])
    for i in lst2:
        if len(i) == 2:
            lst2_terms.append(i[1])
    max_degree = int(max(lst1_terms))
    if max(lst1_terms) < max(lst2_terms): max_degree = int(max(lst2_terms))

    for i in lst1:
        if len(i) == 1:
            if (i[0][-1]) == 'x':
                i.append('1')
                i[0] = i[0][:-1]
            else:
                i.append('0')
    
    for i in lst2:
        if len(i) == 1:
            if (i[0][-1]) == 'x':
                i.append('1')
                i[0] = i[0][:-1]
            else:
                i.append('0')

    lst1_terms = []
    lst2_terms = []
    for i in range(max_degree, -1, -1):
        m = 0
        for k in lst1:
            if int(k[1]) == i:
                m = k[0]
                del k
        lst1_terms.append(int(m))
        m = 0
        for k in lst2:
            if int(k[1]) == i:
                m = k[0]
                del k
        lst2_terms.append(int(m))

    list_final = []
    for i in range(len(lst1_terms)):
        list_final.append(lst1_terms[i] + lst2_terms[i])
    list_final.reverse()
    
    b = ''
    for i in range(max_degree + 1):
        if i == 0:
            b += f'{list_final[i]}'
        elif i == 1:
            b = f'{list_final[i]}x + {b}'
        else:
            b = f'{list_final[i]}x^{i} + {b}'
    b += f' = 0'
    return b


write_file(get_str(get_number('первого')), 'Homework04_Task05_01.txt')
write_file(get_str(get_number('второго')), 'Homework04_Task05_02.txt')

write_file(sum_poly(set_terms_degrees(read_file('Homework04_Task05_01.txt')), set_terms_degrees(read_file('Homework04_Task05_02.txt'))), 'Homework04_Task05_end.txt')

# Можно проще, но оставлю на ближайшее будущее