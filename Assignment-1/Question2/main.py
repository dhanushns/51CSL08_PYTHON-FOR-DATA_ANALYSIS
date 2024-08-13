import pickle


class Student:
    def __init__(self, student_id, name, age, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.courses = {}

    def enroll(self, course):
        if course.course_id not in self.courses:
            self.courses[course.course_id] = None
            course.add_student(self)

    def add_grade(self, course, grade):
        if course.course_id in self.courses:
            self.courses[course.course_id] = grade

    def calculate_gpa(self):
        if not self.courses:
            return 0.0
        total_grade = sum(grade for grade in self.courses.values() if grade is not None)
        return total_grade / len(self.courses)

    def __str__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}, {self.email})"


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        return f"Course({self.course_id}, {self.name}, {self.credits} credits)"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name, age, email):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name, age, email)
        else:
            print(f"Student with ID {student_id} already exists.")

    def add_course(self, course_id, name, credits):
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_id, name, credits)
        else:
            print(f"Course with ID {course_id} already exists.")

    def enroll_student_in_course(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.enroll(course)
        else:
            print(f"Invalid student ID or course ID.")

    def record_grade(self, student_id, course_id, grade):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.add_grade(course, grade)
        else:
            print(f"Invalid student ID or course ID.")

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.students, self.courses), f)
        print(f"Data saved to {filename}.")

    def load_data(self, filename):
        with open(filename, 'rb') as f:
            self.students, self.courses = pickle.load(f)
        print(f"Data loaded from {filename}.")

    def display_students(self):
        for student_id, student in self.students.items():
            print(student)

    def display_courses(self):
        for course_id, course in self.courses.items():
            print(course)

    def __str__(self):
        return f"StudentManagementSystem({len(self.students)} students, {len(self.courses)} courses)"


def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Record Grade")
        print("5. Display Students")
        print("6. Display Courses")
        print("7. Save Data")
        print("8. Load Data")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            email = input("Enter student email: ")
            sms.add_student(student_id, name, age, email)

        elif choice == '2':
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            sms.add_course(course_id, name, credits)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            sms.enroll_student_in_course(student_id, course_id)

        elif choice == '4':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = float(input("Enter grade: "))
            sms.record_grade(student_id, course_id, grade)

        elif choice == '5':
            sms.display_students()

        elif choice == '6':
            sms.display_courses()

        elif choice == '7':
            filename = input("Enter filename to save data: ")
            sms.save_data(filename)

        elif choice == '8':
            filename = input("Enter filename to load data: ")
            sms.load_data(filename)

        elif choice == '9':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
