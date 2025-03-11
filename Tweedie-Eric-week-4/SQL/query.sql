-- query to show all students, their classes, teacher, and grades
SELECT CONCAT( s.first_name, ' ', s.last_name) AS student_name,
        c.subject AS class_name,
        CONCAT(t.teacher_first_name, ' ', t.teacher_last_name) AS teacher_name,
        s.class_grade AS grade
FROM Student AS s
JOIN Classes AS c ON s.class_id = c.course_id
JOIN Teacher AS t ON s.teacher_first_name = t.teacher_first_name AND s.teacher_last_name = t.teacher_last_name
GROUP BY s.first_name, s.last_name, c.subject, t.teacher_first_name, t.teacher_last_name, s.class_grade
ORDER BY c.subject, s.class_grade ASC;

-- function to add student
SELECT addStudent('Michael', 'Struessel', 'mikestreusse@inbox.com', '1995-8-12', '9', 'D', '2', '2', 'Carl', 'Upton', 'cupton@education.com', 'Science');

-- function to get the teacher ID based off first and last name
SELECT getTeacherId('Carl', 'Upton');

-- Procedure to get all the Students
CALL getAllStudents();

-- Procedure to get the students taught by a certain teacher
CALL getTeacherStudents('Michael', 'Scott');
