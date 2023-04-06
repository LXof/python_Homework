# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def Get_number_degree(a, b, num):
    if b == 0:
        return 1
    if b == 1:
        return num
    num *= a
    return Get_number_degree(a, b - 1, num)

number = 2
degree = 4
num_degree = number
print(Get_number_degree(number, degree, num_degree))    # 16
