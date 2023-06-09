#  1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
#  Например для числа 145 сумма цифр будет 10: 1 + 4 + 5

#  Примеры/Тесты:
#  123 >>> Сумма чисел числа 123 равна 6
#  100 >>> Сумма чисел числа 100 равна 1
#  (*) Усложнение. Решите для числа произвольной разрядности: произвольное количество цифр в числе.
#  (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:

# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)
# Совет: Для этого используйте конкатенацию строк и срезы


# Первое решение
three_Namber = 123

first = three_Namber // 100
thied = three_Namber % 10
secod = (three_Namber % 100) // 10

print(f'Сумма чисел числа {three_Namber} равна {first + secod + thied}')


# Второе решение
number = '13579'
str = ''
count = 0
for i in number:
    count += int(i)
    str += i + ' + '

print(f'Сумма чисел числа {number} равна {count}({str}\b\b\b) ')