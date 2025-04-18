class Student:
    name = None
    student_id = None
    grades = None
    def __init__(self, name: str, student_id: int):
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

#Пример:
if __name__ == "__main__":
    Student1 = Student('Babolat', 123)
    Student1.add_grade(grade=4)
    Student1.add_grade(grade=9)
    Student1.add_grade(grade=0)
    Student1.display_info()





