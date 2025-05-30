import pandas as pd

students = pd.read_csv('students.csv')

score = students[students['Score'] > 80]
print('Студенты с баллом выше 80', score, sep='\n')
print('=======')
descending_score = score.sort_values(by='Score', ascending=False)
print(descending_score)
print('=======')
oldest = students['Age'].max()
print('Самый старший:', oldest, sep='\n')
print('=======')
youngest = students['Age'].min()
print('Самый младший:', youngest, sep='\n')
print('=======')

