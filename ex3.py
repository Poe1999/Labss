from abc import ABC, abstractmethod
# из библиотеки (abc) импортируем класс ABC для создания абстрактоного класса и abstractmethod для указания абстрактности метода
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# Создаем абстрактный класс Shape и методы для нахождения плащади и периметра
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
# Создаем класс Прмямоугольник и назначем атрибуты
    def area(self):
        return self.a * self.b
# Нахождение площади
    def perimeter(self):
        return 2*self.a + 2*self.b
# Нахождение периметра

class Circle(Shape):
    def __init__(self, R):
        self.R = R
# Создаем класс Круг и назначаем атрибуты

    def area(self):
        return 3.14 * self.R * self.R
# Нахожднеи площади

    def perimeter(self):
        return 2 * 3.14 * self.R
# Нахождение периметра

class Triangle(Shape):
    def __init__(self, a, b, c, ha):
        self.a = a
        self.b = b
        self.c = c
        self.ha = ha
# Создаем класс Треугольник и назначаем атрибуьы

    def area(self):
        return 0.5 * self.a * self.ha
# Нахождение площади

    def perimeter(self):
        return self.a + self.b + self.c
# Нахождение периметра

def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
# Фунцкия! для вывода информации

# пример:
if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    circle = Circle(4)
    triangle = Triangle(4, 5, 6, 2)
    # Создаем 3 объекта

    print('Rectangle:')
    print_shape_info(rectangle)
    print('-----')

    print('Circle:')
    print_shape_info(circle)
    print('-----')

    print('Triangle:')
    print_shape_info(triangle)
    print('-----')

