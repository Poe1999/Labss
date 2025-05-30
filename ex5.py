import pandas as pd
import matplotlib.pylab as plt

students = pd.read_csv('students.csv')

fig, ax = plt.subplots(1,2)


x = students['Score']
ax[0].hist(x, bins= 10, color = 'darkred')
ax[0].set_title('Score')

grouped = students.groupby('Group')['Score'].mean()
ax[1].bar(grouped.index,grouped.values, color = '#FFD700')
ax[1].set_title('')

plt.show()