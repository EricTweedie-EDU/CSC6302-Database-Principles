DROP DATABASE IF EXISTS Tweedies_Toys;

CREATE DATABASE IF NOT EXISTS Tweedies_Toys;

USE Tweedies_Toys;
DROP TABLE IF EXISTS Customers;

CREATE TABLE IF NOT EXISTS Customers(customer_id INT AUTO_INCREMENT PRIMARY KEY, first_name varchar(50), last_name varchar(50), email_address varchar(50),
									phone_number BIGINT, address varchar(50));

DROP TABLE IF EXISTS Orders;

CREATE TABLE IF NOT EXISTS Orders(order_id INT AUTO_INCREMENT PRIMARY KEY, customer_num INT, item varchar(50), quantity INT, price DECIMAL(4,2), 
							CONSTRAINT FOREIGN KEY (customer_num) REFERENCES Customers(customer_id));

DROP TABLE IF EXISTS Shipping;

CREATE TABLE IF NOT EXISTS Shipping(shipping_id INT AUTO_INCREMENT PRIMARY KEY, customer_num INT, order_num INT, weight INT, package_handler varchar(50), zip_code INT, 
									CONSTRAINT FOREIGN KEY (customer_num) REFERENCES Customers(customer_id), CONSTRAINT FOREIGN KEY (order_num) REFERENCES Orders(order_id));
