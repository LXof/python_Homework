# 1.3[6]. 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

# (*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор


# Решение со срезами
transport_Ticket = '385916'

condition_1 = int(transport_Ticket[0]) + int(transport_Ticket[1]) + int(transport_Ticket[2])
condition_2 = int(transport_Ticket[3]) + int(transport_Ticket[4]) + int(transport_Ticket[5])

print(f"{transport_Ticket} >>> {'yes' if condition_1 == condition_2 else 'no'}")

# Решение с математикой.
transport_Ticket = 385916

condition_1 = ((transport_Ticket // 1000) // 100) + (((transport_Ticket // 1000) // 10) % 10) + ((transport_Ticket // 1000) % 10)
condition_2 = ((transport_Ticket % 1000) // 100) + (((transport_Ticket % 1000) // 10) % 10) + ((transport_Ticket % 1000) % 10)

print(f"{transport_Ticket} >>> {'yes' if condition_1 == condition_2 else 'no'}")

