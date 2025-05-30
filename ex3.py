import pandas as pd

students = pd.read_csv('students.csv')

gaps = students.isna()
print(gaps)
print('=======')
avgscore = students['Score'].mean()
students['Score'] = students['Score'].fillna(avgscore)
#filling_score = students['Score'].fillna(avgscore, inplace = True)
print(students.isna())
print('=======')
deleting_group = students.dropna(subset=['Group'], inplace = True)
print(students)
