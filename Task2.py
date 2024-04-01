import time
from functools import reduce
class Course:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}"

    def __repr__(self):
        return f"Course({self.name}, {self.grade})"
    def get_course_name(self):
        return self.name

    def get_grade(self):
        return self.grade

class Student:
    def __init__(self, name, id, courses):
        self.name = name
        self.id = id
        self.courses = [Course(course_name, grade) for course_name, grade in courses]
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Courses: {', '.join(str(course) for course in self.courses)}"
    def __repr__(self):
        return f"Student({self.name}, {self.id}, {self.courses})"
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_courses(self):
        return self.courses
    def calc_average(self):
        if not self.courses:
            return 0
        if len(self.courses) == 1:
            return self.courses[0].grade
        else:
            return sum(course.grade for course in self.courses) / len(self.courses)



def to_lower(name):
    return name.lower()
def if_file_exist(file_path):
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        return False

def copy_text_until_sign(file_path):
    students = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split('\t')
                if len(parts) != 3:
                    print("Invalid format in file.")
                    continue
                name = parts[0]
                id = int(parts[1])
                courses_str = parts[2].split(';')
                course_grades = {}
                for course_grade_str in courses_str:
                    course, grade_str = course_grade_str.split('#')
                    course_grades[course] = int(grade_str)

                unique_courses = {}
                for course, grade in reversed(course_grades.items()):
                    if course not in unique_courses:
                        unique_courses[course] = grade

                courses = [(course, grade) for course, grade in unique_courses.items()]

                students.append(Student(name, id, courses))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return students

def calc_average_for_student():
    print("Which student's average do you want to calculate?")
    name = input()
    student =list( filter(lambda student: to_lower(student.get_name()) == to_lower(name), students_list))
    if student is None:
        print("Student not found")
        return
    else:
        student = student[0]
        average = student.calc_average()
    print(f"The average for {student.name} is {average}")

def calc_average_for_course():
    course_name = input("Enter the name of the course: ")
    courses = list(reduce(lambda x, y: x + y, map(lambda student: student.courses, students_list)))
    courses = list(filter(lambda course: to_lower(course.get_course_name()) == to_lower(course_name), courses))
    courses = list(map(lambda course: course.get_grade(), courses))
    if not courses:
        print("Course not found")
        return
    else:
        average = reduce(lambda x, y: x + y, courses) / len(courses)
    print(f"The average for {course_name} is {average}")
def export_average_for_all():
    print("Enter a name for the export file:")
    file_name = input()
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    print("The values will be exported to", file_name)
    print("\n")
    with open(file_name, 'w') as file:
        lines = [f"{student.get_id()}\t{student.calc_average()}\n" for student in students_list]
        file.writelines(lines)



def exit_program():
    exit()

if __name__ == '__main__':
    print("Welcome to the Student Grade Calculator!")
    time.sleep(2)
    while True:
        file_path = input("Write the name of file you want to open: \n")
        if not file_path.endswith('.txt'):
            while not file_path.endswith('.txt'):
                file_path = input("Error. Write the name of file you want to open(.txt): \n")
        if not if_file_exist(file_path):
            print("File not found.")
        else:
            students_list = copy_text_until_sign(file_path)
            break

    menu = {
        1: calc_average_for_student,
        2: calc_average_for_course,
        3: export_average_for_all,
        4: exit_program
    }

    while True:
        print("Choose one of the following options:")
        print("1. Average for Student")
        print("2. Average for Course")
        print("3. Average for All")
        print("4. Exit")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if user_choice == 4:
            exit_program()
        if user_choice in menu:
            menu[user_choice]()
        else:
            print("Invalid choice. Please try again.")
