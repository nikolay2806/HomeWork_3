#Задачи на циклы и оператор условия------
#----------------------------------------
'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6

Найти сумму цифр числа.

    Пример:

    254314

    Сумма цифр числа - 19(2+5+4+3+1+4)

'''
print('Задача 1')

num = str(254314)
lenght = len(num)
sum = 0
for i in range(lenght):
    sum += int(num[i])
print('Сумма чисел 254314 равна ',sum)

'''
Задача 7

Найти произведение цифр числа.

    Пример:

    254314

    Произведение цифр числа - 480(2*5*4*3*1*4)
'''
print('Задача 2')

num = str(254314)
lenght = len(num)
proizv = 1
for i in range(lenght):
    proizv *= int(num[i])
print('Произведение чисел 254314 равна ',proizv)

'''
Задача 8

Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".
'''
print('Задача 5')
i = 0
n = input("Введите целое число: ")
lenght = len(n)
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число: ")
n = str(n)

for i in range(lenght):
    num = n[i]
if num == '5':
    print('Цифра 5 есть числе')
else:
    print('Цифра 5 нет числе')

#Решение 2

number = input("Введите число: ")
if '5' in number:
    print("Цифра 5 есть в числе")
else:
    print("Цифры 5 нет в числе")

'''
Задача 9

Найти максимальную цифру в числе

Пример:

    354359688

    'Цифра - 9 максимальная в числе 354359688'
'''

num = int(input("Введите число: "))
max_digit = 0

for digit in str(num):
    if digit.isdigit() and int(digit) > max_digit:
        max_digit = int(digit)

print("Максимальная цифра в числе", num, "равна", max_digit)

'''
Задача 10

Найти количество цифр 5 в числе

    Пример:

        543231235643

        'В числе 2 5-ки.'
'''
n = input("Введите число:")
lenght = len(n)
count = 0
for i in range(lenght):
    if n[i] == '5':
        count = count + 1
print("Количество цифр 5 равно:", count)