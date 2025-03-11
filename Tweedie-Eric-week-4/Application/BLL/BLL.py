# Eric Tweedie 6302 week 4
'''I was unable to get teh import to work with the folders being in separate folders. I tried everything and nothing would work.
I was able to get the program working by merging the DAL folder into the BLL folder. If you have any suggestions for how to get it to work,
I will definitely try them out next time. - Eric'''
# Business Logic Layer
from DAL import *

# function for adding a student to the database
def addStudent():
    info = []
    print("Enter the information for the student being added.\nEnter the ID as 0, this is automatically generated.")
    print("Enter in the order you are prompted and press ENTER after each entry.")
    student_data = ['id', 'first name', 'last name', 'email address', 'date of birth (year-month-day)', 'student grade (ex 9)', 'class grade (ex B)',
                     'class id (ex 2)', 'teacher id (ex 2)', 'teacher first name', 'teacher last name', 'teacher email', 'department']
    for i in student_data:
        info.append(input(f"Enter the {i} for the student: "))

    # call the DAL function to add the student
    DAL.Student.addStudenttoDB(0, info)

# function for retrieving student information
def find_student():
    id_num = int(input("Enter the ID number for the student you are trying to find(ID's are single digit numbers): "))
    DAL.Student.read_student(0, id_num)

# function for adding a Teacher
def addTeacher():
    teacher_info = []
    print("Enter the information for the teacher being added.\nPlease enter the information in the order prompted.\nEnter the ID as 0, this is automatically generated.\nPress ENTER after each entry.")
    
    teacher_data = ['badge id', 'first name', 'last name', 'email address', 'department', 'class id (ex 2)']
    for i in teacher_data:
        teacher_info.append(input(f"Enter the {i} for the teacher: "))

    # call the DAL function to add the teacher
    DAL.Teacher.addTeachertoDB(0, teacher_info)

# function for retrieving teacher information
def find_teacher():
    teach_id = int(input("Enter the ID number for the teacher you are trying to find(ID's are single digit numbers): "))
    DAL.Teacher.read_teacher(0, teach_id)

# function for adding a class
def add_class():
    class_info = []
    print("Enter the information for the class as prompted to add to database.\nEnter the class ID as 0, this is automatically generated.\nPress ENTER after each entry.")

    class_data = ['class id (ex 3)', 'subject name', 'room number', 'semester (ex Fall)']
    for i in class_data:
        class_info.append(input(f"Enter the {i} for the class: "))

    # call the DAL function to add the class
    DAL.Classes.addClasstoDB(0, class_info)

# function for retrieving class information

def find_class():
    class_id = int(input("Enter the ID number for the class you are trying to find(ID's are single digit numbers): "))
    DAL.Classes.read_class(0, class_id)


# function for calling the MySQL function for adding a student
def addStudentfunc():
    print("""Please enter the information of the student being added to the database.
          \nEnter in the order you are prompted and press ENTER after each entry.""")
    student_data = ['first name', 'last name', 'email address', 'date of birth (year-month-day)', 'student grade (ex 3)', 'class grade (ex B)',
                     'class id (ex 1)', 'teacher id (ex 1)', 'teacher first name', 'teacher last name', 'teacher email', 'department']
    new_student = []
    for i in student_data:
        new_student.append(input(f"Enter the {i} for the student: "))

    # call the DAL function to add the student
    DAL.call_addStudent(new_student)

def teacher_id():
    firstname = input("Enter the first name of the teacher you are trying to find: ")
    lastname = input("Enter the last name of the teacher you are trying to find: ")

    DAL.get_teacher_id(firstname, lastname)

def search_all_students():
    print("Enter the name of the procedure to get all of the students in the database.")
    procedure = input("Enter the procedure name: ")

    DAL.call_getAllStudents(procedure)

# main program

def main():
    print("Welcome to the Student Information Management System!")
    while True:
        print("""Choose an option:\n 1. Add a student\n 2. Find a student\n 3. Add a teacher\n 4. Find a teacher\n 5. Add a class\n 6. Find a class\n 7. Add Student without ID number\n 8. Find teacher by ID #\n 9. Show all students\n 0. To exit""")
        choice = int(input("Enter your option: "))
        if choice == 1:
            addStudent()
        elif choice == 2:
            find_student()
        elif choice == 3:
            addTeacher()
        elif choice == 4:
            find_teacher()
        elif choice == 5:
            add_class()
        elif choice == 6:
            find_class()
        elif choice == 7:
            addStudentfunc()
        elif choice == 8:
            teacher_id()
        elif choice == 9:
            search_all_students()
        elif choice == 0:
            print("Thank you for using the Student Information Management System!")
            break

if __name__ == "__main__":
    main()
