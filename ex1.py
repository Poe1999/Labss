import pandas as pd

students = pd.read_csv('students.csv')

print('Первые 5 строк:', students.head(), sep='\n')
print('=======')
print('Информация о данных:',students.info(), sep='\n')
print('=======')
print('Статистика:', students.describe(), sep='\n')
print('=======')
avgscore = students['Score'].mean()
print('Средний балл студентов:', avgscore, sep='\n')
print('=======')
amount_of_students = students.groupby('Group')['Group'].count()
print('Количество студентов в каждой группе:',amount_of_students, sep='\n')
