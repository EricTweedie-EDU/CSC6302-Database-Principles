# View layer
import PySimpleGUI as sg
from .BLL import BLL

sg.theme('lightgreen4')

# read view function 
def read_view(username, password):
    # table for all customers
    headings = ['Customer ID', 'Customer Name', 'Email Address', 'Phone Number', 'Address']
    customer_data = BLL.call_customers(username, password)
    tab1_layout = [
        [sg.Table(values=customer_data, headings=headings,
                  max_col_width=35, auto_size_columns=True,
                  display_row_numbers=False, justification='left',
                  num_rows=10,key='CUSTOMERTABLE', row_height=60, 
                  enable_events=True, tooltip='All Customers'),
                  sg.Button('Exit Customer Table')]
    ]

    # table for all orders
    heading2 = ['Order ID', 'Customer ID', 'Item', 'Quantity', 'Price']
    order_data = BLL.call_orders(username, password)
    tab2_layout = [
        [sg.Table(values=order_data, headings=heading2,
                  max_col_width=35, auto_size_columns=True,
                  display_row_numbers=False, justification='left', 
                  num_rows=10, key='ORDERTABLE', row_height=60, 
                  enable_events=True, tooltip='All Orders'),
                  sg.Button('Exit Order Table')]
    ]

    # tab group layout
    tab_group = sg.TabGroup([[sg.Tab('Customers', tab1_layout),
                              sg.Tab('Orders', tab2_layout)]],
                              selected_title_color='Yellow', selected_background_color='Red')
    
    layout = [[tab_group]]
    window = sg.Window('Tweedies Toy Store', layout)

    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Exit Customer Table' or 'Exit Order Table':
                if sg.popup_yes_no('Are you sure you want to Exit?') == 'Yes':
                    break # go back to login window
        except Exception as e:
            sg.popup_error(f"An error occurred: {str(e)}")
            break

    window.close()
    login_view()
# function for the modify view
def modify_view(username, password):
    # customer constant keys
    CUSTOMER_FIRST = '-CUSTOMER_FIRST-'
    CUSTOMER_LAST = '-CUSTOMER_LAST-'
    EMAIL_ADDRESS = '-EMAIL_ADDRESS-'
    PHONE_NUMBER = '-PHONE_NUMBER-'
    ADDRESS = '-ADDRESS-'

    # order constant keys
    CUSTOMERID = '-CUSTOMERID-'
    ITEM = '-ITEM-'
    QUANTITY = '-QUANTITY-'
    PRICE = '-PRICE-'

    # shipping constant keys
    CUSTOMERSHIPID = '-CUSTOMERSHIPID-'
    ORDERID = '-ORDERID-'
    WEIGHT = '-WEIGHT-'
    PACKAGEHANDLER = '-PACKAGEHANDLER-'
    ZIPCODE = '-ZIPCODE-'

    # tab for adding customer
    tab1_layout = [
        [sg.Text('Add New Customer')],
        [sg.Text('First Name: '), sg.InputText(key=CUSTOMER_FIRST)],
        [sg.Text('Last Name: '), sg.InputText(key=CUSTOMER_LAST)], 
        [sg.Text('Email Address: '), sg.InputText(key=EMAIL_ADDRESS)],
        [sg.Text('Phone Number (no dashes): '), sg.InputText(key=PHONE_NUMBER)],
        [sg.Text('Shipping Address: '), sg.InputText(key=ADDRESS)],
        [sg.Button('Add Customer')]
    ]
    
    # tab for adding new order
    tab2_layout = [
        [sg.Text('Add Customer Order')],
        [sg.Text('Customer ID Number (ex 1): '), sg.InputText(key=CUSTOMERID)],
        [sg.Text('Item: '), sg.InputText(key=ITEM)],
        [sg.Text('Quantity: '), sg.InputText(key=QUANTITY)],
        [sg.Text('Price (ex 10.99): '), sg.InputText(key=PRICE)],
        [sg.Button('Add Order')]
    ]

    # tab for adding shipping information
    tab3_layout = [
        [sg.Text('Add Shipping Information')],
        [sg.Text('Customer ID Number (ex 1): '), sg.InputText(key=CUSTOMERSHIPID)], 
        [sg.Text('Order ID Number (ex 2): '), sg.InputText(key=ORDERID)],
        [sg.Text('Package Weight (whole number): '), sg.InputText(key=WEIGHT)], 
        [sg.Text('Delivery Service: '), sg.InputText(key=PACKAGEHANDLER)],
        [sg.Text('Add Zip Code: '), sg.InputText(key=ZIPCODE)], 
        [sg.Button('Add Shipping Info'), sg.Button('Exit')]
    ]

    # tab group layout
    tab_group = sg.TabGroup([[sg.Tab('New Customer', tab1_layout),
                              sg.Tab('New Order', tab2_layout),
                              sg.Tab('Shipping Info', tab3_layout)]],
                              selected_title_color='Yellow', selected_background_color='Red')
    
    # Window layout
    layout = [[tab_group]]
    window = sg.Window('Tweedies Toy Store Data', layout)

    # lists to store the data being used
    customer_list = []
    order_list = []
    shipping_list = []

    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Exit':
                if sg.popup_yes_no('Are you sure you want to Exit?') == 'Yes':
                    break
            if event == 'Add Customer':
                customer_list = [values[CUSTOMER_FIRST], values[CUSTOMER_LAST],
                                 values[EMAIL_ADDRESS], values[PHONE_NUMBER],
                                 values[ADDRESS]]
                BLL.call_add_customer(username, password, customer_list)
                # clear the input fields
                for key in (CUSTOMER_FIRST, CUSTOMER_LAST, EMAIL_ADDRESS, PHONE_NUMBER, ADDRESS):
                    window[key].update('')
                sg.popup('New Customer added')
                customer_list = []
            
            if event == 'Add Order':
                order_list = [values[CUSTOMERID], values[ITEM],
                              values[QUANTITY], values[PRICE]]
                BLL.call_add_order(username, password, order_list)
                for key in (CUSTOMERID, ITEM, QUANTITY, PRICE):
                    window[key].update('')
                sg.popup('New Order added')
                order_list = []
            
            if event == 'Add Shipping Info':
                shipping_list = [values[CUSTOMERSHIPID], values[ORDERID],
                                 values[WEIGHT], values[PACKAGEHANDLER],
                                 values[ZIPCODE]] 
                BLL.call_add_shipping(username, password, shipping_list)
                for key in (CUSTOMERSHIPID, ORDERID, WEIGHT, PACKAGEHANDLER, ZIPCODE):
                    window[key].update('')
                sg.popup('Shipping Label Added')
                shipping_list = []

        except Exception as e:
            sg.popup_error(f"An error occurred: {str(e)}")
            break

    window.close()
    login_view()
# Login window function

def login_view():
    # constant keys
    USERNAME = '-USERNAME-'
    PASSWORD = '-PASSWORD-'

    # window layout
    layout = [
        [sg.Text('Enter User Credentials')],
        [sg.Text('Enter Username: '), sg.InputText(key=USERNAME)],
        [sg.Text('Enter Password: '), sg.InputText(key=PASSWORD)],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]
    window = sg.Window('Login Window', layout)

    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Exit':
                if sg.popup_yes_no('Are you sure you want to Exit?') == 'Yes':
                    break
            
            if event == 'Submit':
                user = values[USERNAME]
                pw = values[PASSWORD]
                if user == 'read_user' and pw == 'read_read':
                    read_view(user, pw)
                elif user == 'modify_user' and pw == 'modify_modify':
                    modify_view(user, pw)
                else:
                    sg.popup('Access Denied')
        
        except Exception as e:
            sg.popup_error(f"An error occurred: {str(e)}")
            break

    window.close()

if __name__ == '__main__':
    login_view()