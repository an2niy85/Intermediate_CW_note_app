import csv

with open("file.csv", encoding='utf-8') as file:
    csvfilereader = csv.reader(file, delimiter=";")

    # Счетчик

    i = 0

    for r in csvfilereader:

        # Для заголовков

        if i == 0:

            print(f'Файл содержит столбцы: {";".join(r)}')

        # Для строк

        else:

            print(f'{r[0]} {r[1]} {r[2]} - {r[3]} '
                  f'родился в городе {r[4]}.')

        i += 1

print(f'В файле {i} строк.')