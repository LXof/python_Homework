# 2.2[12]: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.

# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

# Примечание.
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети. 
# Обойдите дополнительной проверкой возможность комплексных решений. 
#Можно игнорировать то, что получаться рациональные решения вместо натуральных.

# Для вычисления квадратного корня используйте возведение в степень 0.5 или (*) 
#Усложнение. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.

# x^2 + bx + c = 0
    # x1 + x2 = -b
    # x1 * x2 = c   -->     x2 = c / x1

    # x^2 + bx + c = 0
    # d = b^2 - 4c

    # x1 = (-b + sqrt(d)) / 2
    # x2 = c / x1

b = int(input("Сумма: s = "))
c = int(input("Произведение: p = "))
print(f"x1 + x2 = {-b}")
print(f"x1 * x2 = {c}\n")

# x^2 + xb + c = 0
d = (b * b - 4 * c) ** 0.5
x1 = abs((-b + d) / 2)
x2 = c / x1

print(f"x1 = {x1}; x2 = {x2}")