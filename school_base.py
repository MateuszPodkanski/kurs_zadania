import sys

class Student:
    def __init__(self,name,group):
        self.name = name
        self.group = group

    def __repr__(self):
        return(f"Student: {self.name} in group: {self.group}")

class Teacher:
    def __init__(self,name,subject,groups):
        self.name = name
        self.subject = subject
        self.groups = groups
    
    def __repr__(self):
        return(f"Teacher: {self.name} teaching: {self.subject} in groups: {','.join(self.groups)}")
    
class Supervising_Teacher:
    def __init__(self,name,groups):
        self.name = name
        self.groups = groups

    def __repr__(self):
        return(f"Supervising teacher: {self.name} has groups: {','.join(self.groups)}")   


students = []
teachers = []
s_teachers = []

program_end = False

while program_end == False:
    operation = input("Please enter type of user(student, teacher, supervising teacher or end): ")

    if operation == "student":
        student_name = input("Please enter student's name: ")
        student_group = input("Please enter student's group: ")
        new_student = Student(name = student_name, group = student_group)
        students.append(new_student)
        print(new_student)
    
    elif operation == "teacher":
        teacher_name = input("Please enter teacher's name: ")
        teacher_subject = input("Please enter teacher's subject: ")
        end_input = False
        teacher_groups = []
        while end_input == False:
            teacher_group = input("Please enter teacher's group: ")
            if teacher_group == "":
                end_input = True
            else:
                teacher_groups.append(teacher_group)

        new_teacher = Teacher(name = teacher_name, subject = teacher_subject, groups = teacher_groups)
        teachers.append(new_teacher)
        print(new_teacher)
    
    elif operation == "supervising teacher":
        s_teacher_name = input("Please enter supervising teacher's name: ")
        end_input = False
        s_teacher_groups = []
        while end_input == False:
            s_teacher_group = input("Please enter supervising teacher group: ")
            if s_teacher_group == "":
                end_input = True

            else:
                s_teacher_groups.append(s_teacher_group)

        new_s_teacher = Supervising_Teacher(name = s_teacher_name, groups = s_teacher_groups)
        s_teachers.append(new_s_teacher)
        print(new_s_teacher)
    
    elif operation == "end":
        program_end = True

    else:
        print("Incorrect operation: ")

if len(sys.argv) > 2:
    operation = " ".join(sys.argv[1:])

else:
    operation = sys.argv[1]

# stworzyłem tutaj rozpoznawanie typu uzytkownika 
def id_type(operation):
    for student in students:
        if operation == student.name:
            return "student"
    
    for teacher in teachers:
        if operation == teacher.name:
            return "teacher"
    
    for s_teacher in s_teachers:
        if operation == s_teacher.name:
            return "s_teacher"
    
    if len(operation) == 2:
        return "group"
    else:
        return "nieznany"
        
operation_type=id_type(operation)

def results ():
    if operation_type == "group":
        for student in students:
            if operation == student.group:
                print(f"{student.name}")
        for s_teacher in s_teachers:
            for group in s_teacher.groups:
                if operation == group:
                    print(f"{s_teacher.name}")


    elif operation_type == "s_teacher":
        for s_teacher in s_teachers:
            if operation == s_teacher.name:
                groups = s_teacher.groups
                for group in groups:
                    for student in students:
                        if student.group == group:
                            print(f"{student.name}")

    elif operation_type == "teacher":
        for teacher in teachers:
            if operation == teacher.name:
                t_groups = teacher.groups
                for t_group in t_groups:
                    for s_teacher in s_teachers:
                        s_groups = s_teacher.groups
                        for s_group in s_groups:
                            if s_group == t_group:
                                print(f"{s_teacher.name}")


    elif operation_type == "student":
        for student in students:
            if operation == student.name:
                for teacher in teachers:
                    for group in teacher.groups:
                        if group == student.group:
                            print(f"{teacher.subject}")
                            print(f"{teacher.name}")

    else:
        print("Wrong operation - person/group not found!")

results()











        
