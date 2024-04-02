class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(sum(self.grades.values(), [])) / grades_count
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating:.2f}\n'\
               f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'\
               f'Звершенные курсы: {', '.join(self.finished_courses)}'


    def __lt__(self, other):
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(sum(self.grades.values(), [])) / grades_count
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'

    def __lt__(self, other):
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    """метод выставления оценок студентам от ревьюеров"""
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

'''  ПОЛЕВЫЕ ИСПЫТАНИЯ'''

# создаем список студентов, завершенные курсы и курсы в процессе изучения
student1 = Student('Ruoy', 'Eman', 'man')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Компьтерная грамотность']

student2 = Student ('Emma', 'Stoun', 'woman')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Компьтерная грамотность']


# создаем лекторов и закрепляем за ними курс
lecturer1 = Lecturer('Ivan', 'Ivanov')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Semen', 'Semenov')
lecturer2.courses_attached += ['Git']

# создаем ревьюеров и закрепляем за ними курс
reviewer1 = Reviewer('Petr', 'Petrov')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Vasiliy', 'Vasilev')
reviewer2.courses_attached += ['Git']

# выставление ревьюерами оценок студентам за домашние задания
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student1, 'Git', 6)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 8)
reviewer2.rate_hw(student2, 'Git', 5)
reviewer2.rate_hw(student2, 'Git', 8)

# выставление студентами оценок лекторам за лекции
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer2, 'Git', 8)
student1.rate_lecturer(lecturer2, 'Git', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 10)
student2.rate_lecturer(lecturer2, 'Git', 9)
student2.rate_lecturer(lecturer2, 'Git', 10)


# вызов реализованных методов
print(f'Спиксок проверящих преподователей:\n{reviewer1}\n{reviewer2}\n\n')
print(f'Список лекторов:\n{lecturer1}\n{lecturer2}\n\n')
print(f'Список студентов:\n{student1}\n{student2}\n\n')
print(f'Сравнение студентов по средней оценке за домашние задания: '
      f'{student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1 > student2}')
print(f'Сравнение лекторов по средней оценке за лекции: '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname} = {lecturer1 > lecturer2}')

# содание списков студентов и лекторов
student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]

# функия для рассчета средней оценки студетов
def average_rating_students(student_list, course):
    summ_grades = 0
    count_grades = 0
    for student in student_list:
        if course in student.courses_in_progress:
            summ_grades += student.average_rating
        count_grades += 1
    res = summ_grades / count_grades
    return f'{res:.2f}'

# функция для рассчета средней оценки лекторов
def average_rating_lecturer(lecturer_list, course):
    summ_grades = 0
    count_grades = 0
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            summ_grades += lecturer.average_rating
            count_grades += 1
    res = summ_grades / count_grades
    return f'{res:.2f}'

print(f'Средняя оценка студентов по курсу {'Python'}: {average_rating_students(student_list, 'Python')}')
print(f'Средняя оценка  студентов по курсу {'Git'}: {average_rating_students(student_list, 'Git')}')

print(f'Средняя оценка лекторов по курсу {'Python'}: {average_rating_lecturer(lecturer_list, 'Python')}')
print(f'Средняя оценка лекторов по курсу {'Git'}: {average_rating_lecturer(lecturer_list, 'Git')}')