INSERT INTO Classes (subject, room_number, semester)
VALUES ('English', '100', 'Fall');

INSERT INTO Classes (subject, room_number, semester)
VALUES ('Physics', '305', 'Winter');

INSERT INTO Classes (subject, room_number, semester)
VALUES ('Internal Medicine', '205', 'Spring');

INSERT INTO Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, room_number, subject)
VALUES ('Michael', 'Scott', 'michaelscott@education.com', 'English', '100', 'English');

INSERT INTO Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, room_number, subject)
VALUES ('Jane', 'French', 'janefrench@education.com', 'Physics', '305', 'Quantum Physics');

INSERT INTO  Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, room_number, subject)
VALUES ('Steven', 'Strange', 'stevenstrange@education.com', 'Healthcare', '205', 'Internal Medicine');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, teacher_first_name, teacher_last_name, subject)
VALUES ('John', 'Miller', 'jmiller@mymail.com', '1998-1-3', '10', 'B', 'Michael', 'Scott', 'English');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, teacher_first_name, teacher_last_name, teacher_email, room_number, subject)
VALUES ('George', 'Smith', 'gsmith@mail.com', '1999-2-13', '10', 'B', 'Michael', 'Scott', 'michaelscott@education.com', '100', 'English');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, teacher_first_name, teacher_last_name, teacher_email, room_number, subject)
VALUES ('Kevin', 'Strong', 'kstrong@mailbox.com', '1997-5-23', '9', 'C', 'Steven', 'Strange', 'stevenstrange@education.com', '205', 'Internal Medicine')