class Student:
    def __init__(self, name, roll_number, marks, age):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Age:", self.age)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def load_data(self):
        try:
            with open('student_data.txt', 'r') as file:
                for line in file:
                    student_data = line.strip().split(',')
                    name, roll_number, marks, age = student_data
                    student = Student(name, roll_number, marks, age)
                    self.students[roll_number] = student
        except FileNotFoundError:
            self.students = {}

    def save_data(self):
        with open('student_data.txt', 'w') as file:
            for roll_number, student in self.students.items():
                file.write(
                    f"{student.name},{student.roll_number},{student.marks},{student.age}\n"
                )

    def insert_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = input("Enter marks: ")
        age = input("Enter age: ")
        student = Student(name, roll_number, marks, age)
        self.students[roll_number] = student
        print("Student data inserted successfully!")

    def search_student(self):
        roll_number = input("Enter roll number to search: ")
        student = self.students.get(roll_number)
        if student:
            print("Student found:")
            student.display_info()
        else:
            print("Student not found.")

    def edit_student(self):
        roll_number = input("Enter roll number to edit: ")
        student = self.students.get(roll_number)
        if student:
            print("Enter new data:")
            name = input("Name: ")
            marks = input("Marks: ")
            age = input("Age: ")
            student.name = name
            student.marks = marks
            student.age = age
            print("Student data updated successfully!")
        else:
            print("Student not found.")

    def delete_student(self):
        roll_number = input("Enter roll number to delete: ")
        student = self.students.get(roll_number)
        if student:
            del self.students[roll_number]
            print("Student data deleted successfully!")
        else:
            print("Student not found.")

    def display_students(self):
        if self.students:
            print("Student records:")
            for student in self.students.values():
                student.display_info()
                print("---------------")
        else:
            print("No student records found.")

    def main_menu(self):
        while True:
            print("\nStudent Management System")
            print("1. Insert student data")
            print("2. Search student data")
            print("3. Edit student data")
            print("4. Delete student data")
            print("5. Display all students")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.insert_student()
            elif choice == '2':
                self.search_student()
            elif choice == '3':
                self.edit_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.display_students()
            elif choice == '6':
                self.save_data()
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.load_data()
    sms.main_menu()
