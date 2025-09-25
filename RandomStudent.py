#!env python

import random

default_roster = ["Brian", "Leon", "Andrew"]
coma_sep_student_list = input("Roll Call: (seperate names with comas) ")
if len(coma_sep_student_list) == 0:
    student_roster = default_roster
else:
    student_roster = coma_sep_student_list.split(',')
print(student_roster)
print()

while len(student_roster) > 0:
    student = input("Press pick a specific student (or just enter to pick random student) ")
    if student == "":
        student = random.choice(student_roster)
    elif student not in student_roster:
        print(f"Unknown student. Known students: {student_roster}")
        continue
    print(student)
    student_roster.remove(student)
