-- addStudent function
DROP FUNCTION IF EXISTS addStudent;
delimiter $$
CREATE FUNCTION addStudent(p_first_name varchar(50), p_last_name varchar(50), p_email_address varchar(100), 
							p_date_of_birth Date, p_student_grade INT, p_class_grade varchar(1), p_class_id INT,
                            p_teacher_id INT, p_teacher_first_name varchar(50), p_teacher_last_name varchar(50), 
							p_teacher_email varchar(100), p_dept varchar(50)) 
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
	DECLARE msg varchar(50);
    INSERT INTO Student(first_name, last_name, email_address, date_of_birth, student_grade, class_grade, class_id, teacher_id,
						teacher_first_name, teacher_last_name, teacher_email, dept)
    VALUES (p_first_name, p_last_name, p_email_address, p_date_of_birth, p_student_grade, p_class_grade, p_class_id, p_teacher_id,
			p_teacher_first_name, p_teacher_last_name, p_teacher_email, p_dept);
    
    SET msg = 'Student added successfully';
    RETURN msg;
END $$
delimiter ;

-- getTeacherId function
DROP FUNCTION IF EXISTS getTeacherId;
delimiter $$
CREATE FUNCTION getTeacherId(p_teacher_first_name varchar(50), p_teacher_last_name varchar(50))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE id INT;
    SELECT badge_id INTO id
    FROM Teacher AS t
    WHERE t.teacher_first_name = p_teacher_first_name AND t.teacher_last_name = p_teacher_last_name;
    
    RETURN id;
END $$
delimiter ;

-- getAllStudents procedure
DROP PROCEDURE IF EXISTS getAllStudents;
delimiter $$
CREATE PROCEDURE getAllStudents()
BEGIN
	SELECT first_name, last_name
    FROM Student;
END$$
delimiter ;

-- getTeacherStudents procedure
DROP PROCEDURE IF EXISTS getTeacherStudents;
delimiter $$
CREATE PROCEDURE getTeacherStudents(v_teacher_first_name varchar(50), v_teacher_last_name varchar(50))
BEGIN
	SET @teacherId = getTeacherId(v_teacher_first_name, v_teacher_last_name);
	SELECT @teacherId AS Teacher_ID, 
			CONCAT(t.teacher_first_name, ' ', t.teacher_last_name) AS Teacher,
			CONCAT(s.first_name, ' ', s.last_name) AS Student
    FROM Teacher AS t
    JOIN Student AS s ON t.teacher_first_name = s.teacher_first_name AND t.teacher_last_name = s.teacher_last_name
    WHERE t.teacher_first_name = v_teacher_first_name AND t.teacher_last_name = v_teacher_last_name;
END $$
delimiter ;