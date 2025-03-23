n = int(input())
print(n)
for i in range(n):  # Выводит все числа от 1 до n
    print((i+1))
for i in range(n):  # Выводит квадраты всех чисел от 1 до n
    print((i+1)**2)
l = 0               # Выводит сумму всех чисел от 1 до n
for i in range(1, n+1):
    l += i
print(l)