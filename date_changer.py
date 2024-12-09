from datetime import datetime as dt
created_date = "19.01.2024"
issue_date = "19.05.2024"
temp_created_date = dt.strptime(created_date, '%d.%m.%Y')
#print(created_date, temp_created_date)
temp_issue_date = dt.strptime(issue_date, '%d.%m.%Y')
#print(issue_date, temp_issue_date)

created_date = temp_created_date.strftime('%d.%m.')
issue_date=temp_issue_date.strftime('%d.%m.')
print('Сreated date:', created_date)
print('Issue date:',issue_date)

