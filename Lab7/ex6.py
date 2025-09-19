student = {"name": 'Полинка', "age": 18 , "course": 'Китайский язык', "grades": [5,5,5,5,5,5] }
print('Имя студента и курс, на котором он обучается:',student['name'],student['course'])
avg = sum(student['grades'])//len(student['grades'])
print('Средний балл',avg)
student['grades'].append(5)
print(student)