DROP DATABASE IF EXISTS SCHOOL;

CREATE DATABASE IF NOT EXISTS SCHOOL;

USE SCHOOL;
CREATE TABLE IF NOT EXISTS Student(id INT AUTO_INCREMENT PRIMARY KEY, first_name varchar(50), last_name varchar(50), email_address varchar(100), 
                                date_of_birth Date, student_grade INT, class_grade varchar(1), class_id INT, teacher_id INT);


CREATE TABLE IF NOT EXISTS Teacher(badge_id INT AUTO_INCREMENT PRIMARY KEY, teacher_first_name varchar(50), teacher_last_name varchar(50), 
									teacher_email varchar(100),dept varchar(50), class_id INT, student_id INT);


CREATE TABLE IF NOT EXISTS Classes(course_id INT AUTO_INCREMENT PRIMARY KEY, subject varchar(100), room_number INT, semester varchar(50));

ALTER TABLE Student ADD CONSTRAINT FOREIGN KEY (teacher_id) REFERENCES Teacher(badge_id),
					ADD CONSTRAINT FOREIGN KEY (class_id) REFERENCES Classes(course_id);
                    
ALTER TABLE Teacher ADD CONSTRAINT FOREIGN KEY (class_id) REFERENCES Classes(course_id),
					ADD	CONSTRAINT FOREIGN KEY (student_id) REFERENCES Student(id);