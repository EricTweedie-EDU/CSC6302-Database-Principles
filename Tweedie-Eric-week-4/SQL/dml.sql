-- Classes
INSERT INTO Classes (subject, room_number, semester)
VALUES ('Math', '404', 'Fall');

INSERT INTO Classes (subject, room_number, semester)
VALUES ('Science', '610', 'Spring');

INSERT INTO Classes (subject, room_number, semester)
VALUES ('History', '120', 'Winter');

INSERT INTO Classes (subject, room_number, semester)
VALUE ('English', '100', 'Summer');

-- Teachers
INSERT INTO Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, class_id)
VALUES ('Linda', 'Johnson', 'ljohnson@education.com', 'Mathematics', '1');

INSERT INTO Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, class_id)
VALUES ('Carl', 'Upton', 'cupton@education.com', 'Science', '2');

INSERT INTO Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, class_id)
VALUES ('Martha', 'Lincoln', 'mlincoln@education.com', 'History', '3');

INSERT INTO Teacher (teacher_first_name, teacher_last_name, teacher_email, dept, class_id)
VALUES ('Michael', 'Scott', 'michaelscott@education.com', 'English', '4');

-- Math students 1
INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Matthew', 'Stone', 'mattstone@mailbox.com', '1995-4-12', '9', 'B', '1', '1', 'Linda', 'Johnson', 'ljohnson@education.com', 'Mathematics');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Jason', 'Bourne', 'jbourne@housemail.com', '1996-12-3', '9', 'A', '1', '1', 'Linda', 'Johnson', 'ljohnson@education.com', 'Mathematics');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Robert', 'Kraftington', 'robkraft@fastmail.com', '1995-6-30', '9', 'C', '1', '1', 'Linda', 'Johnson', 'ljohnson@education.com', 'Mathematics');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Sam', 'Samuels', 'samsam@mailtime.com', '1994-8-20', '9', 'C', '1', '1', 'Linda', 'Johnson', 'ljohnson@education.com', 'Mathematics');

-- Science Students 2
INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Veronica', 'Mars', 'marsvern@mail.com', '1993-5-28', '8', 'A', '2', '2', 'Carl', 'Upton', 'cupton@education.com', 'Science');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Ashley', 'Madison', 'ashmadison@emailme.com', '1996-8-23', '8', 'B', '2', '2', 'Carl', 'Upton', 'cupton@education.com', 'Science');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Taylor', 'Longbottom', 'taylong@instantmail.com', '1992-12-9', '8', 'A', '2', '2', 'Carl', 'Upton', 'cupton@education.com', 'Science');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Jennifer', 'Quick', 'jennyquick@fastmail.com', '1998-9-26', '8', 'C', '2', '2', 'Carl', 'Upton', 'cupton@education.com', 'Science');

-- History Students 3
INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Francis', 'Silver', 'silverfrank@emailme.com', '1991-4-20', '11', 'B', '3', '3', 'Martha', 'Lincoln', 'mlincoln@education.com', 'History');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Oliver', 'Bend', 'bendo@mailmail.com', '1990-11-11', '11', 'A', '3', '3', 'Martha', 'Lincoln', 'mlincoln@education.com', 'History');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Roxanne', 'Highstepper', 'roxystep@mailbox.com', '1992-7-25', '11', 'D', '3', '3', 'Martha', 'Lincoln', 'mlincoln@education.com', 'History');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Thomas', 'Bounce', 'tbounce@inbox.com', '1991-6-12', '11', 'A', '3', '3', 'Martha', 'Lincoln', 'mlincoln@education.com', 'History');

-- English Students 4
INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Mandy', 'Maple', 'maplemandy@mailtime.com', '1997-10-2', '10', 'B', '4', '4', 'Michael', 'Scott', 'michaelscott@education.com', 'English');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Jessica', 'Storm', 'jstorm@instantmail.com', '2000-3-23', '10', 'C', '4', '4', 'Michael', 'Scott', 'michaelscott@education.com', 'English');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Joan', 'Salt', 'saltyjoan@mymail.com', '1999-5-10', '10', 'B', '4', '4', 'Michael', 'Scott', 'michaelscott@education.com', 'English');

INSERT INTO Student (first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id, 
						teacher_first_name, teacher_last_name, teacher_email,dept)
VALUES ('Marie', 'Croissant', 'croissant4marie@inbox.com', '1998-3-2', '10', 'A', '4', '4', 'Michael', 'Scott', 'michaelscott@education.com', 'English');
