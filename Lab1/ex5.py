import random
l = [random.randint(1, 101) for i in range(20)]  # Создает список из 20 целых чисел
print(l)
a = list(filter(lambda x: x % 2 == 0, l))  # Из сгенерированного списка (l) выводит все четные числа
print(a)
b = list(filter(lambda x: x % 3 == 0, l))  # Из сгенерированного списка (l) выводит все числа, еоторые делятся на 3
print(b)