class Student:
    name = None
    group = None
    grades = None
    def __init__(self,name,group,grades):
        self.name = name
        self.group = group
        self.grades = grades

    def __repr__(self):
        return f"Student(name='{self.name}',group='{self.group}',grades={self.grades})"

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        if Student.average_grade(self) >= 4.5:
            return True
        else:
            return False


Students = []
with open('students.txt', 'r', encoding='utf-8') as st:
    for line in st:
        data = line.strip().split(";")
        if len(data) >= 3:
            name = data[0]
            group = data[1]
            grades = list(map(int, data[2].split(',')))
            student = Student(name,group,grades)
            Students.append(student)
for student in Students:
    print(student)

with open('excellent_students.txt', 'w', encoding='utf-8') as botans:
    for student in Students:
        student.average_grade()
        if student.average_grade() == 5:
            botans.write(f'{student.name},{student.group}\n')

avg_for_each_group = {}
for student in Students:
    if student.group not in avg_for_each_group:
        avg_for_each_group[student.group] = []
        avg_for_each_group[student.group].append(student.average_grade())

for group,averages in avg_for_each_group.items():
    avg_for_group = sum(averages) / len(averages)
    print(f'{group}:{avg_for_group}')







