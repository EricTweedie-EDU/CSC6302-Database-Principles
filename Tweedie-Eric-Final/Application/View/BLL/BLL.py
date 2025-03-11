# Business Logic Layer
from .DAL import DAL

# function to call the all orders function
def call_orders(username, password):
    return DAL.all_orders(username, password)

# function to call the all customers function
def call_customers(username, password):
    return DAL.all_customers(username, password)

# function to call add customer function
def call_add_customer(username, password, values):
    return DAL.add_customer(username, password, values)

# function call add order function
def call_add_order(username, password, values):
    return DAL.add_order(username, password, values)

# function to call add shipping function
def call_add_shipping(username, password, values):
    return DAL.add_shipping(username, password, values)
