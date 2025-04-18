class Person:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Создание основного класса "Человек"

class Student(Person):
    def __init__(self, student_id, name, age):
        super(Student, self).__init__(name,age) #Передача значений имени и возраста из основоного класса
        self.student_id = student_id
#Создание дочернего класса "Студент"

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Id: {self.student_id}")
# Информация о студенте

class Teacher(Person):
    def __init__(self, name, age, subject):
        super(Teacher, self).__init__(name, age) #Передача значений имени и возраста из основоного класса
        self.subject = subject
        self.students = []
# Сздание дочернего класса "Учитель"

    def display_teacher_info(self):
        print(f"Teacher: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")
#Выводит информацию об учителе

    def add_student(self, student):
        if isinstance(student, Student): #Прверяем является ли студент объектом класса
            self.students.append(student)
        else:
            print('Try again')
# Добавление студента

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
# Удвъаление студетна

    def list_students(self,):
        for student in self.students:
            student.display_info()
# Вывод студентов


# Пример:
if __name__ == "__main__":
    student1 = Student(123, 'Babolat', 20)
    student2 = Student(124, 'Polinom', 20)
    student3 = Student(125, 'Serega', 40)
    # Создаем 3 объекта студент

    teacher = Teacher('Anastasia Sergeevna', 30, 'Discrete math')
    # Создаем объект учитель
    teacher.display_teacher_info()
    print('*****')
    # выводит информацию об учителе

    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.add_student(student3)
    # Добавляем 3-х студентов

    print("Students:")
    teacher.list_students()  # Выводим 3-х студетнов

    teacher.remove_student('Serega')  # Удаляем Серегу
    print('-----')

    teacher.list_students()  # Еще раз выводим студентов, но уже без Сереги
