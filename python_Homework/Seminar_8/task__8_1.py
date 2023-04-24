import csv

# Инициализация справочника
phonebook = []

# Функция создания новой записи
def create_record():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    record = {"last_name": last_name, "first_name": first_name, "phone_number": phone_number, "description": description}
    phonebook.append(record)
    print("Запись добавлена")

# Функция чтения записей
def read_record():
    filter = input("Введите фильтр по первой части фамилии: ")
    for record in phonebook:
        if record["last_name"].startswith(filter):
            print(record)

# Функция изменения записи
def update_record():
    filter = input("Введите фильтр по первой части фамилии: ")
    for record in phonebook:
        if record["last_name"].startswith(filter):
            last_name = input(f"Введите новую фамилию ({record['last_name']}): ")
            first_name = input(f"Введите новое имя ({record['first_name']}): ")
            phone_number = input(f"Введите новый номер телефона ({record['phone_number']}): ")
            description = input(f"Введите новое описание ({record['description']}): ")
            record["last_name"] = last_name or record["last_name"]
            record["first_name"] = first_name or record["first_name"]
            record["phone_number"] = phone_number or record["phone_number"]
            record["description"] = description or record["description"]
            print("Запись изменена")

# Функция удаления записи
def delete_record():
    filter = input("Введите фильтр по первой части фамилии: ")
    for record in phonebook:
        if record["last_name"].startswith(filter):
            phonebook.remove(record)
            print("Запись удалена")

# Функция экспорта данных в csv-файл
def export_csv():
    with open("phonebook.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["last_name", "first_name", "phone_number", "description"])
        for record in phonebook:
            writer.writerow([record["last_name"], record["first_name"], record["phone_number"], record["description"]])
    print("Экспорт завершен")

# Функция импорта данных из csv-файла
def import_csv():
    with open("phonebook.csv", "r") as file:
        reader = csv.reader(file)
        fields = next(reader)
        for row in reader:
            record = {"last_name": row[0], "first_name": row[1], "phone_number": row[2], "description": row[3]}
            phonebook.append(record)
    print("Импорт завершен")

# Бесконечный цикл обработки команд
while True:
    command = input("Введите команду (create/read/update/delete/export/import/exit): ")
    if command == "create":
        create_record()
    elif command == "read":
        read_record()
    elif command == "update":
        update_record()
    elif command == "delete":
        delete_record()
    elif command == "export":
        export_csv()
    elif command == "import":
        import_csv()
    elif command == "exit":
        break
    else:
        print("Команда не распознана")
