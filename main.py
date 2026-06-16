import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "School_data.json"
data = {"Students": [], "Teachers": []}

if Path(database).exists():
    with open(database, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)

class persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass
    
    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        return False
    
class Student(persons):

    def get_roles(self):
        return "Student"
    
    def register(self):
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        email = input("Enter Student Email: ")
        roll_number = input("Enter Student Roll Number: ")

        if not persons.validate_email(email):
            print("Email is invalid.")
            return
        
        for i in data['Students']:
            if i['roll_number'] == roll_number:
                print("Roll number already exists.")
                return

        data['Students'].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_number": roll_number,
            "grades": []
        })
        save()
        print("Student registered successfully.")

    def show_details(self):
        roll_number = input("Enter Student Roll Number: ")
        for i in data['Students']:
            if i['roll_number'] == roll_number:
                print(f"Name: {i['name']}")
                print(f"Age: {i['age']}")
                print(f"Email: {i['email']}")
                print(f"Roll Number: {i['roll_number']}")
                print("Grades:")
                for grade in i['grades']:
                    print(f"{grade['subject']}: {grade['grade']}")
                return

    def add_grades(self):
        roll_number = input("Enter Student Roll Number: ")
        for i in data['Students']:
            if i['roll_number'] == roll_number:
                subject = input("Enter Subject: ")
                grade = input("Enter Grade: ")
                i['grades'].append({"subject": subject, "grade": grade})
                save()
                print("Grade added successfully.")
                return
        print("Student not found.")       

class Teacher(persons):

    def get_roles(self):
        return "Teacher"
    
    def register(self):
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        email = input("Enter Student Email: ")
        subject = input("Enter Subject: ")
        emp_id = input("Enter Employee ID: ")

        if not persons.validate_email(email):
            print("Email is invalid.")
            return
        
        for i in data['Teachers']:
            if i['emp_id'] == emp_id:
                print("Employee ID already exists.")
                return
        
        data['Teachers'].append({
            "name": name,
            "age": age,
            "email": email,
            "subject": subject,
            "emp_id": emp_id
        })
        save()
        print("Teacher registered successfully.")

    def show_details(self):
        emp_id = input("Enter Employee ID: ")
        for i in data['Teachers']:
            if i['emp_id'] == emp_id:
                print(f"Name: {i['name']}")
                print(f"Age: {i['age']}")
                print(f"Email: {i['email']}")
                print(f"Subject: {i['subject']}")
                print(f"Employee ID: {i['emp_id']}")
                return

student = Student()
teacher = Teacher()


print("Press 1 to register a Student")
print("Press 2 to register a Teacher")
print("Press 3 to add Grades")
print("Press 4 to show a Student details")
print("Press 5 to show a teacher details")

choice = int(input("Enter your choice: "))

if choice ==1:
    student.register()

elif choice == 2:
    teacher.register()

elif choice == 3:
    student.add_grades()
    
elif choice == 4:
    student.show_details()

elif choice == 5:
    teacher.show_details()