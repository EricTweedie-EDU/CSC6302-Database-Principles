CREATE ROLE 'admin_role';
GRANT ALL PRIVILEGES ON *.* TO 'admin_role' WITH GRANT OPTION;
GRANT 'admin_role' TO 'admin_user'@'%';
SET DEFAULT ROLE 'admin_role' TO 'admin_user';

CREATE ROLE 'read_role';
GRANT SELECT ON *.* TO 'read_role';
GRANT 'read_role' TO 'read_only'@'%';
SET DEFAULT ROLE 'read_role' TO 'read_user';

CREATE ROLE 'modify_role';
GRANT UPDATE, ALTER ON *.* TO 'modify_role';
GRANT 'modify_role' TO 'modify_user'@'%';
SET DEFAULT ROLE 'modify_role' TO 'modify_user';