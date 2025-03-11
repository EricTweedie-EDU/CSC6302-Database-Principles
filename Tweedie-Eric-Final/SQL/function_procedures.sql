-- procedure to show all orders
-- read user 
DROP PROCEDURE IF EXISTS allOrders;
delimiter $$
CREATE PROCEDURE allOrders()
BEGIN
	SELECT o.order_id, 
			CONCAT(c.first_name, ' ', c.last_name) AS Customer,
            o.item,
            o.quantity,
            o.price
	FROM Orders AS o
    JOIN Customers AS c ON o.customer_num = c.customer_id;
END $$
delimiter ;

-- procedure to show all the customers
-- read user
DROP PROCEDURE IF EXISTS allCustomers;
delimiter $$
CREATE PROCEDURE allCustomers()
BEGIN
	SELECT customer_id, 
    CONCAT(first_name, ' ', last_name) AS Customer,
    email_address, phone_number, address
    FROM Customers;
END $$
delimiter ;

-- procedure to add customers
-- modify user
DROP PROCEDURE IF EXISTS addCustomer;
delimiter $$
CREATE PROCEDURE addCustomer(p_first_name varchar(50), p_last_name varchar(50), p_email_address varchar(50),
									p_phone_number BIGINT, p_address varchar(50))
BEGIN
	INSERT INTO Customers(first_name, last_name, email_address, phone_number, address)
				VALUES(p_first_name, p_last_name, p_email_address, p_phone_number, p_address);
	
END $$
delimiter ;

-- procedure to add orders
-- modify user
DROP PROCEDURE IF EXISTS addOrder;
delimiter $$
CREATE PROCEDURE addOrder(p_customer_num INT, p_item varchar(50), p_quantity INT, p_price INT)
BEGIN
    INSERT INTO Orders(customer_num, item, quantity, price)
    VALUES (p_customer_num, p_item, p_quantity, p_price);
    
END $$
delimiter ;

-- procedure to add shipping information
-- modify user
DROP PROCEDURE IF EXISTS addShipping;
delimiter $$
CREATE PROCEDURE addShipping(p_customer_num INT, p_order_num INT, p_weight INT, p_package_handler varchar(50), p_zip_code INT)
BEGIN
    INSERT INTO Shipping(customer_num, order_num, weight, package_handler, zip_code)
    VALUES (p_customer_num, p_order_num, p_weight, p_package_handler, p_zip_code);
    
END $$
delimiter ;

