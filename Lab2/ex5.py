l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # созданием списк чисел от 1 до 20
only_odd = list(filter(lambda x: (x%2==0), l))  # Только четные числа
decrease = list(sorted(l, key = lambda x: -x))  # убываенние
print(decrease)
add_ten = list(map(lambda x: x+10, l))  # прибавление ао всем числам 10
print(add_ten)