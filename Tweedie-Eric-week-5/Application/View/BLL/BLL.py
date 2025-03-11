# Eric Tweedie 6302 week 5
# Business Logic Layer
from .DAL import DAL

# function for adding a student to the database
def addStudent(data):
    student_data = list(data.split)
    info = []
    
    for i in student_data:
        info.append(i)

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
def addStudentfunc(info):
    student_data = list(info)
    
    new_student = []
    for i in student_data:
        new_student.append(i)

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

def see_all_students():
    return DAL.show_Students()