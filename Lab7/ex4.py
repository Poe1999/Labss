start = int(input())
end = int(input())
ll = []
for i in range (start, end+1):
    if i % 2 == 0:
        ll.append(i)
    else:
        print( "В этом диапазоне нет чётных чисел.")
print(ll)