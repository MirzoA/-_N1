grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)  #  Из множество создаём список
list_students.sort()  #  Список сортируем в алфавитном порядке
grades1 = []
for i in grades:  #  Расчёт среднего бала студентов
    sum_ = 0
    count_ = 0
    for j in i:
        sum_ += j
        count_ += 1
    average = sum_ / count_
    grades1.append(average)
print(list_students)  # Сортированный список студентов по алфавиту
print(grades1)  #  Усреднённые оценки студентов
average_grades = dict(zip(list_students, grades1))  #  Создание словаря из двух списков
print(average_grades)  #  Словарь учеников с их балами

