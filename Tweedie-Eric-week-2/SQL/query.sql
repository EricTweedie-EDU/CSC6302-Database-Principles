SELECT *
FROM Student
WHERE teacher_last_name = 'Scott';

SELECT *
FROM Teacher AS t
RIGHT JOIN Student AS s ON t.subject = s.subject;

SELECT *
FROM Classes AS c
RIGHT JOIN Student AS s on c.room_number = s.room_number
WHERE semester = 'Fall';