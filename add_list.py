# Input Data from user

Username = input('Введите имя пользователя: ') # Имя пользователя
print('Username:', Username)
Title1 = input('Введите заголовок заметки №1: ') # Заголовок заметки
print('Title:', Title1)
Title2 = input('Введите заголовок заметки №2: ') # Заголовок заметки
print('Title:', Title2)
Title3 = input('Введите заголовок заметки №3: ') # Заголовок заметки
print('Title:', Title3)
Titles=[Title1, Title2, Title3]
print("Список заголовков заметки:", "Заметка №1 -", Title1+";",
      "Заметка №2 -",Title2+";", "Заметка №3 -", Title3+".")
#print("Список заголовков заметки:", Titles)
Content = input('Введите описание заметки: ') # Описание заметки
print('Content:', Content)
Status = input('Введите статус заметки: ') # Статус заметки
print('Status:', Status)
Created_date = input('Введите дату создания заметки в формате-"день.месяц.год": ')
print('Created date:', Created_date)
#Дата создания заметки в формате-"день.месяц.год"
Issue_date = input('Введите дату истечения заметки (дедлайн)в формате-"день.месяц.год": ')
#Дата истечения заметки (дедлайн)в формате-"день.месяц.год"
print('Created date:', Issue_date)


