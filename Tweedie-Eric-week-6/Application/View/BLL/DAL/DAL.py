# Eric Tweedie 6302 week 5
# Data Access Layer
import mysql.connector

# Connection to database function

def connect_to_database(user_name, pw):
    # Connect to MySQL database with provided username and password
    cnx = mysql.connector.connect(user=user_name, password=pw,
                                        host='127.0.0.1', port='3305',
                                        database='SCHOOL')
    return cnx

# Class for the Student table
class Student:
    def __init__(self, id, firstname, lastname, email, date_of_birth, student_grade, class_grade, class_id, teacher_id,):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.date_of_birth = date_of_birth
        self.student_grade = student_grade
        self.class_grade = class_grade
        self.class_id = class_id
        self.teacher_id = teacher_id

    def addStudenttoDB(self, student_data, user_name, pw):
        # Create connection object to connect to MySQL database
        # connection needs to be done with the Modify user
        if user_name != 'modify_user' and pw != 'modify1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()

        # Adding a student to the Student table
        sql = ("INSERT INTO Student" 
               "(id, first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
        val = (student_data)
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Student record inserted.")

        cursor.close()
        cnx.close()

    def read_student(self, student_id, user_name, pw):
        # Create connection object to connect to MySQL database
        # connection needs to be done with the Read Only user
        if user_name != 'read_only' and pw !='read1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()

        # Read a student from the Student table
        sql = f"SELECT * FROM Student WHERE id = {student_id}"
        cursor.execute(sql)
        print(cursor.fetchone())

        cursor.close()
        cnx.close()

        
# Class for the Teacher table
class Teacher:
    def __init__(self, badge_id, teacher_first_name, teacher_last_name, teacher_email, dept, class_id):
        self.badge_id = badge_id
        self.teacher_first_name = teacher_first_name
        self.teacher_last_name = teacher_last_name
        self.teacher_email = teacher_email
        self.dept = dept
        self.class_id = class_id

    def addTeachertoDB(self, teacher_data, user_name, pw):
        # Create connection object to connect to MySQL database
        # connection needs to be done with the Modify user
        if user_name != 'modify_user' and pw != 'modify1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()
        # Adding a teacher to the Teacher table
        sql = ("INSERT INTO Teacher" 
               "(badge_id, teacher_first_name, teacher_last_name, teacher_email, dept, class_id)" 
               "VALUES (%s, %s, %s, %s, %s, %s)")
        val = (teacher_data)
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Teacher record inserted.")

        cursor.close()
        cnx.close()

    def read_teacher(self, teacher_id, user_name, pw):
        # Create connection object to connect to MySQL database
        # connection needs to be done with the Read Only user
        if user_name != 'read_only' and pw !='read1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()
        # Read a teacher from the Teacher table
        sql = f"SELECT * FROM Teacher WHERE badge_id = {teacher_id}"
        cursor.execute(sql)
        print(cursor.fetchone())

        cursor.close()
        cnx.close()

# Class for the Classes table
class Classes:
    def __init__(self, course_id, subject, room_number, semester):
        self.course_id = course_id
        self.subject = subject
        self.room_number = room_number
        self.semester = semester

    def addClasstoDB(self, class_data, user_name, pw):
        # Create connection object to connect to MySQL database
        # connection needs to be done with the Modify user
        if user_name != 'modify_user' and pw != 'modify1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()
        # Adding a class to the Classes table
        sql = ("INSERT INTO Classes" 
               "(course_id, subject, room_number, semester)"
                "VALUES (%s, %s, %s, %s)")
        val = (class_data)
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Class record inserted.")

        cursor.close()
        cnx.close()

    def read_class(self, class_id, user_name, pw):
        # Create connection object to connect to MySQL database
        # connection needs to be done with the Read Only user
        if user_name != 'read_only' and pw !='read1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()
        # Read a class from the Classes table
        sql = f"SELECT * FROM Classes WHERE course_id = {class_id}"
        cursor.execute(sql)
        print(cursor.fetchone())

        cursor.close()
        cnx.close()

# Function to call stored function in SCHOOL database
def call_addStudent(params, user_name, pw):
    # Create connection object to connect to MySQL database
    # connection needs to be done with the Modify user
        if user_name == 'read_only' and pw == 'read1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
    # Create cursor object for connection
        cursor = cnx.cursor(buffered=True)
        sql = "SELECT addStudent (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = params
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Student added to Student Table.")

        cursor.close()
        cnx.close()

# Function to get teacher id
def get_teacher_id(fname, lname, user_name, pw):
    # Create connection object to connect to MySQL database
    # connection needs to be done with the Read Only user
        if user_name != 'read_only' and pw !='read1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                return "Failed to connect to database."
    # Create cursor object for connection
        cursor = cnx.cursor()
        sql = "SELECT getTeacherId (%s, %s)"
        val = (fname, lname)
        cursor.execute(sql, val)
        id_num = cursor.fetchone()

        cursor.close()
        cnx.close()
        
        return id_num

# Function to call stored procedure in SCHOOL database
def call_getAllStudents(user_name, pw):
    # Create connection object to connect to MySQL database
    # connection needs to be done with the Read Only user
        if user_name != 'read_only' and pw !='read1234':
            return "Access denied. Invalid Credentials."
        else:
            cnx = connect_to_database(user_name, pw)
            if cnx is None:
                print("Failed to connect to database.")
        # Create cursor object for connection
        cursor = cnx.cursor()
        student_list = []
        cursor.callproc('getAllStudents')
        for result in cursor.stored_results():
                for row in result.fetchall():
                    students = [
                        row[0], # first name
                        row[1]] # last name
                    student_list.append(students)

        cursor.close()
        cnx.close()
        return student_list

def show_Students():
    # Create connection object to connect to MySQL database
    # hardcoded credentials due to the function only showing data
    user_name = 'modify_user'
    pw ='modify1234'    
    cnx = connect_to_database(user_name, pw)
    
    # Create cursor object for connection
    cursor = cnx.cursor()
    cursor.callproc('showAllStudents')
    students = []
    for result in cursor.stored_results():
        for row in result.fetchall():
            student_data = [
                row[0],  # First Name
                row[1],  # Last Name
                row[2],  # Email Address
                row[3],  # Teacher
                row[4],  # Course
                row[5]   # Grade
            ]
            students.append(student_data)
    
    cursor.close()
    cnx.close()
    return students