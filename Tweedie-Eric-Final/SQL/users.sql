DROP USER 'admin_user'@'%';
CREATE USER 'admin_user'@'%'
IDENTIFIED BY 'admin_admin';

DROP USER 'read_user'@'%';
CREATE USER 'read_user'@'%'
IDENTIFIED BY 'read_read';

DROP USER 'modify_user'@'%';
CREATE USER 'modify_user'@'%'
IDENTIFIED BY 'modify_modify';