# список словарей с заметками, каждый словарь представляет одну заметку
notes = [{'Имя': 'Павел', 'Заголовок': 'Новый Год', 'Описание': 'Нарядить ёлку'} , {'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'},
{'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}]
#notes = [] # пустой список для проверки
empty = len(notes) # переменная для проверки пустого списка получает длину списка

# Создание функции вывода заметок на экран for i in range(len(notes)):
def output_notes(notes):
        #if notes.index(0) == 0:
        if empty != 0: # проверка пустого списка
            print("\nСписок заметок.")
            for i in range(len(notes)):
                print(f"\nЗаметка № {i+1}: ")
                for key,value in notes[i].items():
                    print(key, "-", value )
        else: # пустой список
            print("\nСписок заметок пуст.\nРабота программы завершена.")

output_notes(notes) # вывод заметок на экран с помощью функции output_note()

# Создание функции удаления заметок

if empty != 0: # проверка пустого списка
    while True:
        # переменная критерия для удаления заметки:
        criteria_del = input("\nВведите критерий (Имя пользователя или Заголовок) для удаления (Ввод не может быть пустым): ")
        if criteria_del.strip() == "":  # проверка пустого ввода и удаление начальных/конечных пробелов
                print("Критерий не может быть пустым. Повторите ввод.")
        else:
            break  # выход из цикла, если ввод корректный

    for i in range(len(notes)): # цикл сравнения критерия (criteria_del) с существующими элементами
        name_del = notes[i].values()
        if criteria_del.strip() in name_del:
            reserv_dict = notes.pop(i)
            print(f"\nУдалена заметка с критерием - {criteria_del.strip()}.\nОстались следующие заметки:")
            output_notes(notes)
            break
    else: # если критерий (criteria_del) не найден в существующих элементах
        print((f"Заметок с Именем пользователя или Заголовком - '{criteria_del}' не найдено."))