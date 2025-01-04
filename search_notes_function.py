# Функция поиска заметок

# Исходный список заметок:
notes = [
    {'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю', 'Статус': 'новая', 'Дата создания': '27.11.2024', 'Дедлайн': '30.11.2024'},
    {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену', 'Статус': 'в процессе', 'Дата создания': '25.11.2024', 'Дедлайн': '01.12.2024'},
    {'Имя': 'Иван', 'Заголовок': 'План работы', 'Описание': 'Завершить проект', 'Статус': 'выполнено', 'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'},
    {'Имя': 'Сергей', 'Заголовок': 'План работы', 'Описание': 'Завершить проект', 'Статус': 'новая', 'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'}
]

status_exist = ("новая", "в процессе", "выполнено") # кортеж с возможными вариантами Статуса

# Определение функции поиска заметок
def search_notes (notes, keyword=None, status=None):
    if len(notes) == 0: # проверка наличия заметок в списке
        print("\nСписок заметок пуст.\nПоиск невозможен.")
        return
    if keyword is None and status is None:
        print("\nКлючевое слово и/или Статус не введены.\nПоиск завершен.")
    elif keyword != None and status is None:
        j = 0 # счетчик найденных заметок
        for i in range(len(notes)):
            cur_values = list(notes[i].values())  # значения словаря i заносим во временный список
            if keyword in cur_values:  # проверка Ключевого слова во временном списке
                j += 1
                if j == 1:
                    print(f"\nПо Ключевому слову - '{keyword}' найдены заметки:")
                    print(f"Заметка{j}.")
                else:
                    print(f"Заметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)
    elif keyword is None and status != None:
        j = 0  # счетчик найденных заметок
        for i in range(len(notes)):
            if status == notes[i].get('Статус'):  # проверка Статуса во временном списке
                j += 1
                if j == 1:
                    print(f"\nПо Статусу - '{status}' найдены заметки:")
                    print(f"Заметка{j}.")
                else:
                    print(f"Заметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)

    else:
        j = 0  # счетчик найденных заметок
        for i in range(len(notes)):
            cur_values = list(notes[i].values())  # значения словаря i заносим во временный список
            if keyword in cur_values and status == notes[i].get('Статус'):  # проверка Ключевого слова во временном списке
                j += 1
                if j == 1:
                    print(f"\nПо Ключевому слову - '{keyword}' и Статусу '{status}' найдены заметки:")
                    print(f"Заметка{j}.")
                else:
                    print(f"Заметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)


search_notes (notes)
search_notes (notes, keyword ='Список покупок')
search_notes (notes, status ='в процессе')
search_notes (notes, keyword ='План работы', status ='выполнено')
#search_notes (notes, keyword ='Мария', status ='yjdfz')


"""def search_notes (notes, keyword=None, status=None):
# Ввод(запрос) Ключевого слова/статуса для поиска заметки:
    keyword = input("\nВведите Ключевое слово для поиска заметки (пустой ввод - поиск только по Cтатусу): ")
    keyword = keyword.strip() # удаление начальных/конечных пробелов из Ключевого слова
    if keyword == "": # проверка пустого ввода Ключевого слова и/или Статуса
        status = input("\nВведите Статус (новая, в процессе, выполнено) для поиска заметки.\n"
                        "При пустом вводе поиск будет завершен:")
        status = status.strip()  # удаление начальных/конечных пробелов из Статуса
        if status == "":  # проверка пустого ввода Статуса
            print("Ключевое слово и/или Статус не введены.\n"
                    "Поиск завершен.")
        elif status not in status_exist: # Проверка доступного статуса заметки
            print("Такого Статуса не существует.\nПоиск завершен.")
        else:
            search_status(notes, status)

    else: # сравнение Статуса с возможными значениями
        status = input("\nВведите Статус при необходимости одновременного поиска по Ключевому слову и Статусу.\n"
                       "При пустом вводе поиск будет продолжен только по Ключевому слову: ")
        status = status.strip()  # удаление начальных/конечных пробелов из Статуса
        if status == "":  # проверка пустого ввода Статуса
            print("Поиск продолжается только по Ключевому слову.")
        elif status not in status_exist:  # Проверка доступного статуса заметки
            print("Такого Статуса не существует.\nПоиск продолжается только по Ключевому слову.")
        else:
            search_status(notes, status)

        j = 0 # счетчик найденных заметок
        for i in range(len(notes)):
            cur_values = list(notes[i].values())  # значения словаря i заносим во временный список
            if keyword in cur_values:  # проверка Ключевого слова во временном списке
                j += 1
                if j == 1:
                    print(f"\nПо ключевому слову - '{keyword}' найдены заметки:")
                    print(f"\nЗаметка{j}.")
                else:
                    print(f"\nЗаметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)
        else:
            if j > 0:
                print("\nРабота программы завершена.")
            else:
                print("\nТакого Ключевого слова в заметках не существует."
                        "Работа программы завершена.")

# функция поиска/вывода заметок по Статусу
def search_status (notes, status):
    j = 0  # счетчик найденных заметок
    for i in range(len(notes)):
        if status == notes[i].get('Статус'):  # проверка Статуса во временном списке
            j += 1
            if j == 1:
                print(f"\nПо Статусу - '{status}' найдены заметки:")
                print(f"\nЗаметка{j}.")
            else:
                print(f"\nЗаметка{j}.")
            for key, value in notes[i].items():
                print(key, "-", value)

search_notes(notes, keyword, status) # Вызов функции поиска заметок


def search_notes (notes, keyword=None, status=None):
    if keyword == None and status == None:
        print("Ключевое слово и/или Статус не введены.\n"Поиск завершен.")
    elif keyword != None and status == None:
        j = 0 # счетчик найденных заметок
        for i in range(len(notes)):
            cur_values = list(notes[i].values())  # значения словаря i заносим во временный список
            if keyword in cur_values:  # проверка Ключевого слова во временном списке
                j += 1
                if j == 1:
                    print(f"\nПо ключевому слову - '{keyword}' найдены заметки:")
                    print(f"\nЗаметка{j}.")
                else:
                    print(f"\nЗаметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)
                        

"""