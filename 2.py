n = int(input())  # считываем количество студентов

# считываем курсы первого студента и преобразуем в множество
courses = set(input().split())

for i in range(n - 1):
    student_courses = set(input().split())
    courses = courses.intersection(student_courses)  
print(len(courses))

#Пример
'''
3
История Биология Программирование
Биология Программирование Физика
Программирование История Биология
'''
