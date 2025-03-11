DROP USER 'admin_user'@'%';
CREATE USER 'admin_user'@'%'
IDENTIFIED BY 'admin1234';

DROP USER 'read_only'@'%';
CREATE USER 'read_only'@'%'
IDENTIFIED BY 'read1234';

DROP USER 'modify_user'@'%';
CREATE USER 'modify_user'@'%'
IDENTIFIED BY 'modify1234';