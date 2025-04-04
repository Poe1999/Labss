try:
    a = float(input())
    b = float(input())
    product = a/b
    print(product)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except ValueError:
    print('Введено нечисловое значение!')

