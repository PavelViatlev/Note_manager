"""создаём словарь для хранения данных заметки
note = {'Имя пользователя': '', 'Описание заметки': '', # 'Статус заметки': '',
'Дата создания заметки': '', 'Дата истечения заметки (дедлайн)': '',
'Заголовок заметки': []} """

note = {}

# Input Data from user
note["Имя пользователя"] = input("Введите имя пользователя: ")
note["Описание заметки"] = input("Введите описание заметки: ")
note["Статус заметки"] = input("Введите статус заметки: ")
note["Дата создания заметки"] = input("Введите дату создания заметки в формате 'день.месяц.год': ")
note["Дата истечения заметки"] = input("Введите дату истечения заметки (дедлайн) в формате 'день.месяц.год': ")

Title1 = input('Введите заголовок заметки №1: ') # Заголовок заметки №1
Title2 = input('Введите заголовок заметки №2: ') # Заголовок заметки №2
Title3 = input('Введите заголовок заметки №3: ') # Заголовок заметки №3
Titles=[Title1, Title2, Title3]
note["Заголовки заметок "] = Titles

for key,value in note.items():
     print(key,value )
