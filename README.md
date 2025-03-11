# CSC6302-Database-Principles
Repo containing all the projects from the Database Principles course 

# Contents

# Module 1
Creating the database and setting up the file structure
Creating SQL folder holding all the SQL files
Creating the Application folder to hold all of the application files
Six files inside of your SQL folder.  They should be named accordingly.  users.sql, permissions.sql, ddl.sql, dml.sql, procedure_functions.sql, and query.sql.
Inside your users.sql file, create three users for your database. Permissions.sql file, create three roles for your database. Grant the corresponding role to each user.
Inside your DDL.sql file, create a database with the database name SCHOOL. Create a table in your database. Inside your DML.sql file, insert at least one tuple (DML) into your table

# Module 2
Decompose your Student table into three separate tables
Three tables should be named: Student, Teacher, and Classes
Insert some data into each table.  Add at least 3 tuples in each table.  Make sure that each student has one teacher, a teacher has a classroom.
Write some queries on your database.  (At least 3 queries) Make sure that one of the queries has a join between two of the tables.  

# Module 3
Write some more inserts to each table.  Create the 4 basic classes.  Math, Science, English, and History.  Assign a teacher to each of these and make sure that there are at least three students in each class.  Make sure each student has a grade in each class they are in.  
Write a query that shows (for each student) the first and last name, class name, teacher name, and grade they are receiving for each class.  Group this query by the student name and sort each class by the highest grade (A) to the lowest grade (F).
Create two functions and two procedures. One function should be called addStudent and insert a student into the database.  The other function should be called getTeacherId return the teacher id when searching for the teacher's first and last name.
The first procedure will be called getAllStudents and return all students in the students table.  The second procedure will be called getTeacherStudents and return all the students that are taught by a specific teacher.

# Module 4
Let's begin our Application Architecture. Pick a language that you would like to develop in.  Java, Python, or Node. 
create your Business Logic Layer, and Data Access Layer (DAL).   Create two folders inside of your application folder.  The folders should be named BLL and DAL.  Inside of your BLL and DAL, map the tables that you currently have and create each of the tables as a Class.
Get your application to connect to the database.  Use the admin_user you created in Week 1 to make the connection.  Remember, we are hardcoding the url, user, and password into the connection.
Connecting the Layers, Use the DAL to call one of the procedures on your database, Use the DAL to call one of the functions on your database.

# Module 5
Application Layer
Create a Presentation Layer, Using Toga or the  GUI of your choice (PySimpleGUI), connect your View and Business Logic Layer
Display all the Students in the Students table, Add a Student from the View Layer.

# Module 6
In your permissions.sql file, grant each role the proper procedures and functions according to their operation.  Read to read and modify to modify.  Your database should not execute procedures or functions from a role that does not have the granted permissions.
Add logic to your DAL that correctly makes the connection to your database with the correct user when your procedures are updating the database.

# Module 7
Text document with planning for final project 

# Module 8
Final project will be to create an application and database based on all you learned this semester.
Inside of your sql folder you will have 5 files, ddl.sql, which will contain your database and table relations, users.sql, this file will contain your admin, read, and write only users,
permissions.sql, this file will contain your admin, read, and write only roles, function_procedures.sql, this file will contain your procedures and functions, 
dml.sql, this file will have your insert statement to add data to your database.
Inside of your application folder you will have as many files as needed but should clearly have three main layers.
Presentation layer that is run by calling the main file. This layer can be a GUI or a CLI but should only show the functionality that is working.
Business Logic Layer, this layer should control your business logic and be the bridge between your Presentation layer and the Data access layer.
Data Access Layer, this layer should bridge functionality between the business logic layer and the database.
