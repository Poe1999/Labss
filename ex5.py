class Student:
    name = None
    student_id = None
    grades = None
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
# Создание атрибутов класса с помощью конструктора инит

    def add_grade(self, grade):
        while 0 <= grade <= 10:
            self.grades.append(grade)
            break
# Добавление оценки

    def get_average(self):
        return sum(self.grades) / len(self.grades)
# Нахождение среднего балла студента

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Id: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average()}")
# Вывод информации о студенте

    def __str__(self):
        return f"Student: {self.name}, Id: {self.student_id}, Grades: {self.grades}, Average: {self.get_average()}"
# Строковое представление

    def __eq__(self, other):
        return self.student_id == other.student_id
# Сравнение по id студентов

    def __len__(self):
        return len(self.grades)
# Длина списка grades т.е кол-во оценок

# Пример:
if __name__ == "__main__":
    Student1 = Student('Babolat', 123)
    Student2 = Student('Polinom', 123)  # Добавляем 2-го студента
    Student3 = Student('Pipipupu', 124)  # Добавляем 3-го студента
    Student1.add_grade(grade=4)
    Student1.add_grade(grade=9)
    Student1.add_grade(grade=0)
    Student1.display_info()
    # Работа Дополнения:
    print('-----')
    print(Student1)  # Выводим сторку
    print(len(Student1))  # Выводим кол во оценок
    print(Student1 == Student2)  # Сравниваем id по студента 1 и студента 2
    print(Student1 == Student3)  # Сравниваем id по студента 1 и студента 3

