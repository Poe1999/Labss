import pandas as pd
import matplotlib.pyplot as plt

sales = {'товар': ['пикми-указка', 'киндер буэно', 'дэка', 'пикми-указка', 'лабуба', 'подвеска', 'киндер буэно'], "кол-во":[1000, 5435, 78, -1, 345, 0, 56], "цена":["", 70, "", "",234, 5679, 64]}
df = pd.DataFrame(sales)
#print(df.head())


df['цена'] = pd.to_numeric(df['цена'])
m_price = df['цена'].median()
df['цена'] = df['цена'].fillna(m_price)

#print(df.head())

outlier_condition = (df['кол-во'] < 1) | (df['кол-во'] > 1000)
outliers = df[outlier_condition]
print("Выбросы")
print(outliers)

dfcl = df[~outlier_condition].copy()
print('Без выбросов')
print(dfcl)


dfcl['общая_стоимость'] = dfcl['цена']*df['кол-во']

#print(df.head())

asdgj = dfcl.groupby('товар')['общая_стоимость'].sum()
print(asdgj)


plt.bar(dfcl['товар'], dfcl['общая_стоимость'], color = 'darkred')
plt.show()

