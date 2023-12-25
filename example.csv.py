import csv
with open("classmates.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(", ".join(row))
        # Вывод строк
        print(row["Имя"],row["Успеваемость"], row["Год рождения"])
        count += 1
    print(f'Всего в файле {count + 1} строк.')