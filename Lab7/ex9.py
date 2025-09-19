import random
l1 = [random.randint(-10, 10) for i in range(15)]
l2 = list(filter(lambda x: x > 0, l1))
l3 = list(map(lambda x: x ^ 2, l1))
print(l1)
print(l2)
print(l3)
