# Input Data from user

inputUsername = input('Введите имя пользователя: ') # Имя пользователя
print('Username:', inputUsername)
inputTitle1 = input('Введите заголовок заметки №1: ') # Заголовок заметки
print('Title:', inputTitle1)
inputTitle2 = input('Введите заголовок заметки №2: ') # Заголовок заметки
print('Title:', inputTitle2)
inputTitle3 = input('Введите заголовок заметки №3: ') # Заголовок заметки
print('Title:', inputTitle3)
Titles=[inputTitle1, inputTitle2, inputTitle3]
print("Список заголовков заметки:", "Заметка №1 -", inputTitle1+";",
      "Заметка №2 -",inputTitle2+";", "Заметка №3 -", inputTitle3+".")
inputContent = input('Введите описание заметки: ') # Описание заметки
print('Content:', inputContent)
inputStatus = input('Введите статус заметки: ') # Статус заметки
print('Status:', inputStatus)
inputCreated_date = input('Введите дату создания заметки в формате-"день.месяц.год": ')
print('Created date:', inputCreated_date)
#Дата создания заметки в формате-"день.месяц.год"
inputIssue_date = input('Введите дату истечения заметки (дедлайн)в формате-"день.месяц.год": ')
#Дата истечения заметки (дедлайн)в формате-"день.месяц.год"
print('Created date:', inputIssue_date)


