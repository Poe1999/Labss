a = int(input())
b = int(input())
c = int(input())
counter1 = 0
counter2 = 0
if a >= b:
    counter1 += b
else:
    counter1 +=a
if counter1 >= c:
    counter2 += c
else:
    counter2 += counter1
print(counter2)


