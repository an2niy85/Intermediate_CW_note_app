import os, re, json


def phone_format(n):  # форматирование телефонного номера
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):  # Функция вывода записной книги в консоль
    noteBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Date        Title          Text")
    print(splitLine)
    id = 1

    for note in data:
        date, title, text = note.rstrip().split(",")
        noteBook.append(
            {
                "ID": id,
                "Date": date, # форматирование при выводе
                "Title": title,
                "Text": text,
            }
        )
        id += 1

    for note in noteBook:
        id, date, title, text = note.values()
        print(f"{id:>2}. {date:<15} {title:<10} -- {text:<15}")

    print(splitLine)


def showNotes(fileName):  # Функция открытия записной книги
    os.system("cls")
    noteBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- press any key ---")


def addNote(fileName):  # Функция добавления новой заметки в записную книгу
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Input a Date of Note: ") + ","
        res += input("Input a Title of Note: ") + ","
        res += input("Input a Text of Note: ")

        file.write(res + "\n")

    input("\nNote was successfully added!\n--- press any key ---")

#

def findNote(fileName):  # Функция поиска заметки в записной книге
    os.system("cls")
    target = input("Input Item of Note for searching: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for note in data:
            if target in note:
                result.append(note)
                break

    if len(result) != 0:
        printData(result)
    else:
        print(f"There is no Note with this Item '{target}'.")

    input("--- press any key ---")

def findNoteWithDate(fileName):  # Функция поиска заметки в записной книге
    os.system("cls")
    target = input("Input Date of Note for searching: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for note in data:
            if target in note:
                result.append(note)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"There is no Note with this Item '{target}'.")

    input("--- press any key ---")


def changeNote(fileName):  # Функция изменения информации в контакте
    os.system("cls")
    noteBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberNote = int(
            input("Input Number of Note for changing or 0 for return Main Menu: ")
        )
        print(data[numberNote - 1].rstrip().split(","))
        if numberNote != 0:
            newDate = input("Input new Date: ")
            newTitle = input("Input new Title: ")
            newText = input("Input new Text: ")
            data[numberNote - 1] = (
                newDate + "," + newTitle + "," + newText + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nNote was successfully changed!")
                input("\n--- press any key ---")
        else:
            return


def deleteNote(fileName):  # Функция удаления контакта из телефонной книги
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberNote = int(
            input("Input Number of Note for deleting or 0 for return Main Menu: ")
        )
        if numberNote != 0:
            print(f"Deleting record: {data[numberNote-1].rstrip().split(',')}\n")
            data.pop(numberNote - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- press any key ---")


def drawInterface():  # Функция рисования интерфейса главного меню
    print("#####   NOTE BOOK   #####")
    print("=" * 26)
    print(" [1] -- Show Notes")
    print(" [2] -- Add Notes")
    print(" [3] -- Find Notes")
    print(" [4] -- Find Notes with Date")
    print(" [5] -- Change Notes")
    print(" [6] -- Delete Notes")
    print("\n [0] -- Exit")
    print("=" * 26)


def main(file_name):  # Функция реализации главного меню
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Input a Number for 1 to 5 or 0 for Exit: "))

        if userChoice == 1:
            showNotes(file_name)
        elif userChoice == 2:
            addNote(file_name)
        elif userChoice == 3:
            findNote(file_name)
        elif userChoice == 4:
            findNoteWithDate(file_name)
        elif userChoice == 5:
            changeNote(file_name)
        elif userChoice == 6:
            deleteNote(file_name)
        elif userChoice == 0:
            print("Thank you!")
            return


path = "notebook.txt"

main(path)

# Ввод данных через аргументы
# Запись в файл и чтение через csv или json
# объект в класс
# SOLID ok
# MVC или MVP
# TKInter ...
#