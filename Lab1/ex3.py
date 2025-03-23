n = int(input())
print(n)
while n >= 1:          # Выводит все числа от n до 1
    for i in range(n):
        print((n-i))
    break
l = 1        # Выводит факториал всех чисел от 1 до n
while n >= 0:
    if n != 0:
        for i in range(1, n + 1):
            l *= i
        print(l)
        break
    else:
        print(1)
        break



