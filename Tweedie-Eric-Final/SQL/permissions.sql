DROP ROLE IF EXISTS 'admin_role';
CREATE ROLE IF NOT EXISTS 'admin_role';
GRANT ALL PRIVILEGES ON *.* TO 'admin_role' WITH GRANT OPTION;
GRANT 'admin_role' TO 'admin_user'@'%';
SET DEFAULT ROLE 'admin_role' TO 'admin_user';

DROP ROLE IF EXISTS 'read_role';
CREATE ROLE IF NOT EXISTS 'read_role';
GRANT SELECT ON *.* TO 'read_role';
GRANT EXECUTE ON PROCEDURE Tweedies_Toys.allOrders TO 'read_role';
GRANT EXECUTE ON PROCEDURE Tweedies_Toys.allCustomers TO 'read_role';
GRANT 'read_role' TO 'read_user'@'%';
SET DEFAULT ROLE 'read_role' TO 'read_user';

DROP ROLE IF EXISTS 'modify_role';
CREATE ROLE IF NOT EXISTS 'modify_role';
GRANT UPDATE, ALTER ON *.* TO 'modify_role';
GRANT EXECUTE ON PROCEDURE Tweedies_Toys.addCustomer TO 'modify_role';
GRANT EXECUTE ON PROCEDURE Tweedies_Toys.addOrder TO 'modify_role';
GRANT EXECUTE ON PROCEDURE Tweedies_Toys.addShipping TO 'modify_role';
GRANT 'modify_role' TO 'modify_user'@'%';
SET DEFAULT ROLE 'modify_role' TO 'modify_user';

FLUSH PRIVILEGES;
-- Flush privileges to have them take effect immediately