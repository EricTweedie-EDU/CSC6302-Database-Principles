CREATE DATABASE IF NOT EXISTS SCHOOL;

USE SCHOOL;
CREATE TABLE IF NOT EXISTS Student(id INT AUTO_INCREMENT PRIMARY KEY, first_name varchar(50), last_name varchar(50), email_address varchar(100), 
                                date_of_birth Date, student_grade INT, class_grade varchar(1), teacher_first_name varchar(50), teacher_last_name varchar(50), teacher_email varchar(100),
                                room_number INT, subject varchar(100), FOREIGN KEY (teacher_first_name) REFERENCES Teacher(teacher_first_name),
                                FOREIGN KEY (teacher_last_name) REFERENCES Teacher(teacher_last_name), FOREIGN KEY (teacher_email) REFERENCES Teacher(teacher_email),
                                FOREIGN KEY (room_number) REFERENCES Classes(room_number), FOREIGN KEY (subject) REFERENCES Classes(subject));
/* I chose to use the student id as the primary key because it is the variable that is going to stay unique no matter what. The id number of the student will always
reference that given student regardless if there is a match in first or last name. The id value is a simple way to keep track of the uniqueness of each student but it allows for 
an easier access point when cross referencing within different tables. */
/* The super keys and candidate keys for the Student table are:
Super Keys - {id}, {id, first_name}, {id, first_name, last_name}, {id, first_name, email_address}, {id, last_name}, {id, email_address}, {id, date_of_birth}, {id, last_name. email_address},
{first_name, last_name}, {first_name, email_address}, {id, student_grade}, {first_name, last_name, date_of_birth}, {last_name, email_address}, {last_name, date_of_birth}, 
email_address, date_of_birth}
Candidate keys - {id}, {email_address} */

CREATE TABLE IF NOT EXISTS Teacher(badge_num INT AUTO_INCREMENT PRIMARY KEY, teacher_first_name varchar(50), teacher_last_name varchar(50), teacher_email varchar(100),
                                room_number INT, subject varchar(100), dept varchar(50), FOREIGN KEY (room_number) REFERENCES Classes(room_number),
                                FOREIGN KEY (subject) REFERENCES Classes(subject));
/* I chose to use the badge_num value for the primary key because it is also a simlar situation as the student table. The value will remain unique throughout and 
there will not be any duplication of the value as the table grows. Also there should really only be one badge number that corresponds to each teacher. */
/* The super keys and the candidate keys for the Teacher table are:
Super Keys - {badge_mum}, {badge_num, teacher_email}, {badge_num, teacher_first_name}, {teacher_email}, {teacher_email, room_number}. {teacher_email, subject}, 
{teacher_email, course_code}, {teacher_email, dept}, {badge_num, teacher_first_name, teacher_last_name}, {teacher_email, teacher_first_name, teacher_last_name}, 
{teacher_email, teacher_first_name}
Candidate keys - {badge_num}, {teacher_email} */

CREATE TABLE IF NOT EXISTS Classes(course_code INT AUTO_INCREMENT PRIMARY KEY, subject varchar(100), room_number INT, semester varchar(50),
									dept varchar(50), FOREIGN KEY (dept) REFERENCES Teacher(dept));
/* I decided to choose the course_code as the primary key because it is also a value that will hold its uniqueness over the long term since each code will correspond
to only one class, reducing the chance of duplication and the need for more specification when looking for that class. */
/* The super keys and candidate keys for the Classes table are:
Super keys - {course_code}, {course_code, room_number}, {course_code, subject}, {course_code, semester},
{course_code dept}, {course_code, room_number, subject, {course_code, semester}
Candidate keys - {course_code} */