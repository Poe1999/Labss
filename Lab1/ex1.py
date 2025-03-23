a = int(input())
b = int(input())
c = int(input())
print(a, b, c)
print(max(a, b, c))  # Выводит максимальное число из 3х чисел
print(min(a, b, c))  # Выводит минимальное из 3х чисел
if a == b == c:  # Проверка равенства всех чисел
    print('YES')
else:
    print('NO')