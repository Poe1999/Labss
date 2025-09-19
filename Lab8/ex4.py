import numpy as np

a = np.random.randint(0,10,(5,5))
b = np.random.randint(0,10,(5,5))
#print(a)
#print(b)

print('Поэлементное произведение матриц.')
print(a*b)

print('Матричное произведение.')
print(a@b)

oprA = np.linalg.det(a)
print('Определитель матрицы A.')
print(oprA)

trans = np.transpose(b)
print('Транспонированную матрицу B.')
print(trans)

opr = np.linalg.det(a)
if opr !=0:
    inv = np.linalg.inv(a)
    print(inv)
else:
    print("ооэпрэр ты айпадкид, определитель равен нулю")

C = a.sum(axis=1)
x = np.linalg.solve(a, C)
print(a)
print(C)
print(x)


