import random


class Student:
    def __init__(self, fullname: str, group_num: int, marks: list):
        self.fullname = fullname
        self.group_num = group_num
        self.marks = marks

    def __repr__(self):
        return 'Студент {}, группа {}. Оценки {} (средний балл {})'.format(self.fullname, self.group_num, self.marks,
                                                                           self.average_marks())

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


def create_students_list():
    names = ['Иван', 'Алексей', 'Михаил', 'Владимир', 'Дмитрий', 'Сергей', 'Игорь', 'Роман', 'Пётр', 'Валерий', 'Олег']
    surnames = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Романов', 'Воробьёв', 'Галкин', 'Сорокин', 'Котов']
    students = list()

    for _ in range(10):
        student = Student('{} {}'.format(random.choice(names), random.choice(surnames)),
                          random.randint(1, 10), [random.randint(2, 5) for _ in range(5)])
        students.append(student)

    return students


for i_student in sorted(create_students_list(), key=lambda student: student.average_marks()):
    print(i_student)
