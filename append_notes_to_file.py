# Добавление заметок в файл Grade 1. Этап 4: Задание 4

# cписок заметок для добавления в файл:
notes_add = [
    {'Имя': 'Антон', 'Заголовок': 'Диссертация', 'Описание': 'Глава 1', 'Статус': 'выполнена',
     'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'},
    {'Имя': 'Антон', 'Заголовок': 'Диссертация', 'Описание': 'Глава 2', 'Статус': 'в процессе',
     'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'},
    {'Имя': 'Антон', 'Заголовок': 'Диссертация', 'Описание': 'Глава 3', 'Статус': 'новая',
     'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'},
]

class IncorrectData(Exception): # создаем класс для обработки ошибок
    pass

def append_notes_to_file(notes, filename):
    try:  # для обработки исключения файл не найден - FileNotFoundError
        with open(filename, 'r', encoding='utf-8') as file:  # блок для автоматического закрытия файла
            i = 0
            temp_str = file.readlines()  # временная строка
            if len(temp_str) == 0:  # Проверка пустого файла
                raise IncorrectData("\nФайл пуст. Необходимо добавить заметки в файл.\nРабота программы завершена.")
            else:
                file.seek(0)  # текущую позицию на начало файла
                while bool(temp_str): # цикл поиска количества строк
                    i += 1
                    temp_str = file.readline()  #
                i = i - 9 # вычисление номера строки с номером последней заметки (заметка занимает 8 строк)
                file.seek(0)  # текущую позицию на начало файла
                j = 0
                while j < i: # цикл перехода на номер строки с номером последней заметки (заметка занимает 8 строк)
                    file.readline()  #
                    j += 1
                temp_str = file.readline() # строка с номером последней заметки
                temp_str = temp_str.split() # делим строку по признаку - ' ', строки заносим в список
                temp_str = temp_str[2].split('.')  # третью строку списка делим строку по признаку - '.'
                quant_note_file = temp_str[0] # кол-во заметок в файле
                quant_note_file = int(quant_note_file)
        with open(filename, 'a+', encoding='utf-8') as file:  # блок для автоматического закрытия файла
            print(notes_add)
            for i in range(len(notes_add)):
                file.write(f'Заметка № {quant_note_file + i + 1}.\n')
                for key, value in notes_add[i].items():
                    file.write (f"{key}: {value}\n")
                file.write("-------------------------------------\n")

    except IncorrectData as e:  # обработка исключения при пустом  или неправильном формате файла
        print(e)

    except FileNotFoundError: # обработка исключения при невозможности открытия файла
        print("Файл 'Notes Manager.txt' не найден.")
        with open("Notes Manager.txt", 'x', encoding='utf-8') as file:
            print("\nСоздан новый файл 'Notes Manager.txt'.")

append_notes_to_file(notes_add, 'Notes Manager.txt')

"""def save_notes_to_file():
    file = open('Notes Manager.txt', 'w', encoding='utf-8')
    for i in range(len(notes)):
        file.write(f'Заметка №{i+1}.\n')
        for key, value in notes[i].items():
            file.write (f"{key}: {value}\n")
        file.write("-------------------------------------\n")
    file.close()"""