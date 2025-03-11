# Data Access Layer
import mysql.connector

# connection function

def connector(username, password):
    cnx = mysql.connector.connect(user= username, password= password, 
                                  host= '127.0.0.1', port= '3305', 
                                  database= 'Tweedies_Toys')
    return cnx

# Read user functions to connect to database
# function to show all Orders
def all_orders(username, password):
    if username != 'read_user' and password != 'read_read':
        return "Access denied. Invalid credentials."
    else: 
        cnx = connector(username, password)
        cursor = cnx.cursor()
        cursor.callproc('allOrders')
        order_list = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                orders = [
                    row[0], # Order ID
                    row[1], # Customer name
                    row[2], # Item
                    row[3], # Quantity
                    row[4]  # Price
                ]
                order_list.append(orders)
    cnx.close()
    cursor.close()
    return order_list

# function to show all customers
def all_customers(username, password):
    if username != 'read_user' and password != 'read_read':
        return "Access Denied. Invalid Credentials."
    else:
        cnx = connector(username, password)
        cursor = cnx.cursor()
        cursor.callproc('allCustomers')
        customer_list = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                customers = [
                    row[0], # Customer ID
                    row[1], # Customer Name
                    row[2], # email address
                    row[3], # Phone Number
                    row[4], # Address
                ]
                customer_list.append(customers)
    cnx.close()
    cursor.close()
    return customer_list

# functions for the modify user

# function to add a new customer
def add_customer(username, password, params):
    if username != 'modify_user' and password != 'modify_modify':
        return "Access Denied. Invalid Credentials."
    else:
        cnx = connector(username, password)
        cursor = cnx.cursor()
        sql = 'CALL addCustomer (%s, %s, %s, %s, %s)'
        val = params
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Customer added successfully.")
        cnx.close()
        cursor.close()

# function to add a new order
def add_order(username, password, params):
    if username != 'modify_user' and password != 'modify_modify':
        return "Access Denied, Invalid Credentials."
    else:
        cnx = connector(username, password)
        cursor = cnx.cursor()
        sql = 'CALL addOrder (%s, %s, %s, %s)'
        val = params
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Order added successfully.")
        cnx.close()
        cursor.close()

# function add shipping information
def add_shipping(username, password, params):
    if username != 'modify_user' and password != 'modify_modify':
        return "Access Denied. Invalid Credentials."
    else:
        cnx = connector(username, password)
        cursor = cnx.cursor()
        sql = 'CALL addShipping (%s, %s, %s, %s, %s)'
        val = params
        cursor.execute(sql, val)
        cnx.commit()
        print(cursor.rowcount, "Shipping label created successfully.")
        cnx.close()
        cursor.close()

