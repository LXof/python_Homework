# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def Get_sum_2_Not_minus_number(a, b):
    if (a or b) < 0: return None
    if b == 0:
        return a
    return Get_sum_2_Not_minus_number(a + 1, b - 1)

def check_Not_minus_number(a, b):
    if (a or b) < 0:
        return False
    return True
        

a = 3
b = 8
if check_Not_minus_number(a, b):
    print(Get_sum_2_Not_minus_number(a, b))

