# 3.3[20]: 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы и заранее известно какой алфавит надо использовать.

# Примеры/Тесты:
# Input:   ноутбук
# Output:  12

# Input:   notebook
# Output:  14

# (*) Примечание.
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, 
# чтобы просто проверять в какую группу попадает буква, а также просто накапливать сумму очков.

print("Добро пожаловать в игру 'Scrabble'!!!\n")
print("Выберите действие:\n")
print("\t1 : Начать игру на Английском (English).")
print("\t2 : Начать игру на Русском (Russion)")
print("\t3 : Выйти из игры,")

cmd =  input("Ваш выбор: ")
points = 0

def Count_Point(d, word, point):
    for k, v in d.items():
        if word in v:
            point += k
    return point

def Print_Point(points):
    print(f"Количество очков: {points}")

def Add_Dictionary(my_dict, key, value):
    my_dict[key] = (value) 
    return my_dict

    
if cmd == "1": 

    key = 1, 2, 3, 4, 5, 8, 10
    value = "A E I O U L N S T R", "D G", "B C M P", "F H V W Y", "K", "J X", "Q Z"
    d = dict()
    count_value = 0
    for i in key:
        Add_Dictionary(d, i, value[count_value])
        # print(Add_Dictionary(d, i, value[count_value]))
        count_value += 1

    print("Each letter has a certain value!")
    word = input("Input word: ").upper() 
    for i in word:
        points = Count_Point(d, i, points)
    Print_Point(points)

elif cmd == "2":
    key = 1, 2, 3, 4, 5, 8, 10
    value = "А В Е И Н О Р С Т", "Д К Л М П У", "Б Г Ё Ь Я", "Й, Ы", "Ж З Х Ц Ч", "Ш Э Ю", "Ф Щ Ъ"

    d = dict()
    count_value = 0
    for i in key:
        Add_Dictionary(d, i, value[count_value])
        count_value += 1

    print("Каждая буква имеет определенную ценность!")
    word = input("Введите слово: ").upper() 
    for i in word:
        points = Count_Point(d, i, points)
    Print_Point(points)

elif cmd == "3":
    print("Вы вышли из игры!")
    exit()

else:
    print(f"{cmd}\n Команда не существует!!!")
    
