CREATE USER 'admin_user'@'%'
IDENTIFIED BY 'admin1234';

CREATE USER 'read_only'@'%'
IDENTIFIED BY 'read1234';

CREATE USER 'modify_user'@'%'
IDENTIFIED BY 'modify1234';

SELECT * FROM mysql.user;