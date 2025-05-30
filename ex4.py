import pandas as pd
import numpy as np

students = pd.read_csv('students.csv')

grouped = students.groupby('Group').agg(Median_Age = ('Age', 'median'), Avg_Score = ('Score', 'mean'))
print(grouped)
print('=======')
students['Passed'] = np.where(students['Score'] > 60, '1', '0')
print(students)