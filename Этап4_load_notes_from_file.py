# Функция читает заметки из текстового файла и возвращает их в виде списка словарей. Grade 1. Этап 4: Зад. 2, 3

class IncorrectData(Exception): # создаем класс для обработки ошибок
    pass
notes = []  # создание списка словарей с заметками

def load_notes_from_file():
    try: # для обработки исключения файл не найден - FileNotFoundError
        with open("Notes Manager.txt", 'r', encoding='utf-8') as file: # блок для автоматического закрытия файла
            # Блок проверки пустого файла
            temp_str = file.readlines() # для проверки пустого файла
            if len(temp_str) == 0:
                raise IncorrectData("\nФайл пуст. Необходимо добавить заметки в файл.\nРабота программы завершена.")
            else:
                file.seek(0) # установливаем на начало файла текущую позицию
                temp_str = file.readline()  # считываем текущую строку
                j = 0  # счетчик считанных заметок
                while "Заметка" in temp_str:
                    i = 0 # счетчик строк в заметке
                    list_key = ['Имя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн' ]
                    note = {}  # создание словаря для заметок
                    while i<6:
                        temp_str = file.readline() # считываем текущую строку
                        temp_str = temp_str.split(': ') # делим строку по признаку - ': ', строки заносим в список
                        temp_str = temp_str[1].split('\n') # вторую строку списка делим строку по признаку - '\n '
                        note[list_key[i]] = temp_str[0]
                        i += 1
                    else:
                        notes.append(note)  # Добавление словаря с новой заметкой в список заметок
                        j += 1
                        temp_str = file.readline()  # считываем завершающую строку ("------------")
                        temp_str = file.readline()  # считываем следующую строку

                else:
                    if j == 0:
                        raise IncorrectData("\nФайл должен начинаться со слова 'Заметка'."
                                            "\nУкажите файл с корректным содержанием. Работа программы завершена.")
                    else:
                        print(f"\nИз файла считано и создан список словарей содержащий заметок: {j}."
                              f"\nРабота программы завершена.")
                        print(notes)
                    return notes

    except IncorrectData as e:  # обработка исключения при пустом  или неправильном формате файла
        print(e)

    except FileNotFoundError: # обработка исключения при невозможности открытия файла
        print("Файл 'Notes Manager.txt' не найден.")
        with open("Notes Manager.txt", 'x', encoding='utf-8') as file:
            print("\nСоздан новый файл 'Notes Manager.txt'.")

load_notes_from_file()

