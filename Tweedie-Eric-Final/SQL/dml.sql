-- adding customers
INSERT INTO Customers(first_name, last_name, email_address, phone_number, address)
			VALUES ('John', 'Blue', 'bluejohn@mail.com', '3432321234', '23 Barrington Ave');
            
INSERT INTO Customers(first_name, last_name, email_address, phone_number, address)
			VALUES ('Martha', 'May', 'marthamay@inbox.com', '4442236677', '88 Lower Lane');
            
INSERT INTO Customers(first_name, last_name, email_address, phone_number, address)
			VALUES ('Joe', 'Shmoeburger', 'joeshmoe@gotmail.com', '5432158080', '212 State Circle');
            
INSERT INTO Customers(first_name, last_name, email_address, phone_number, address)
			VALUES ('Lois', 'Lane', 'superlane@email.com', '1012320099', '45 Super Terrace');
            
INSERT INTO Customers(first_name, last_name, email_address, phone_number, address)
			VALUES ('Peter', 'Parrot', 'parrotpete@mail.com', '9908761122', '86 Squawker Street');
            
-- adding orders
INSERT INTO Orders(customer_num, item, quantity, price)
			VALUES ('1', 'Harry Potter Lego set', '1', '69.99');
            
INSERT INTO Orders(customer_num, item, quantity, price)
			VALUES ('2', 'Barbie Disco', '2', '39.95');
            
INSERT INTO Orders(customer_num, item, quantity, price)
			VALUES ('3', 'Nintendo Switch', '1', '99.99');
            
INSERT INTO Orders(customer_num, item, quantity, price)
			VALUES ('4', 'Monopoly Lego', '1', '25.00');
            
INSERT INTO Orders(customer_num, item, quantity, price)
			VALUES ('5', 'Hot Wheels F1 set', '3', '20.99');
            
-- adding shipping information
INSERT INTO Shipping(customer_num, order_num, weight, package_handler, zip_code)
			VALUES ('1', '1', '10', 'UPS', '08793');
            
INSERT INTO Shipping(customer_num, order_num, weight, package_handler, zip_code)
			VALUES ('2', '2', '3', 'USPS', '45231');
            
INSERT INTO Shipping(customer_num, order_num, weight, package_handler, zip_code)
			VALUES ('3', '3', '6', 'FEDEX', '23005');
            
INSERT INTO Shipping(customer_num, order_num, weight, package_handler, zip_code)
			VAlUES ('4', '4', '3', 'DHL', '03227');
            
INSERT INTO Shipping(customer_num, order_num, weight, package_handler, zip_code)
			VALUES ('5', '5', '5', 'UPS', '45671');
