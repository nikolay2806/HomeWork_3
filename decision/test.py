

print('Задача 5')

num = input('Введите число: ')

length = len(num)
integers = []
i = 0 # индекс текущего символа

while i < length:
    num_int = '' # строка для нового числа
    while i < length and '0' <= num[i] <= '9':
        num_int += num[i]
        i += 1
    i += 1
    if num_int != '':
        integers.append(int(num_int))

print(integers)