file = open('data.txt', 'r', encoding='cp1251')
numbers = [int(file.readline()) for i in range(10)]
print(numbers)
total = sum(numbers)
average = total/10
largest = max(numbers)
smallest = min(numbers)
result = open('result.txt', 'w+')
result.write('Сумма: ' + str(total) + '\n')
result.write('Среднее: ' + str(average) + '\n')
result.write('Максимум: ' + str(largest) + '\n')
result.write('Минимум: ' + str(smallest) + '\n')
result.close()
file.close()