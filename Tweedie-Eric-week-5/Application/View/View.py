# Eric Tweedie CSC 6302 week 5
# View Layer
# Eric Tweedie CSC 6302 week 5
# View Layer
import PySimpleGUI as sg
from BLL import BLL 

# Define constants for keys
FIRST_NAME = '-FIRST_NAME-'
LAST_NAME = '-LAST_NAME-'
EMAIL = '-EMAIL-'
DOB = '-DOB-'
STUDENT_GRADE = '-STUDENT_GRADE-'
CLASS_GRADE = '-CLASS_GRADE-'
CLASS_ID = '-CLASS_ID-'
TEACHER_ID = '-TEACHER_ID-'

sg.theme('DarkBlue13')

# Multi tab window layouts
headings = ['First Name', 'Last Name', 'Email Address', 'Teacher', 'Course', 'Grade']
student_data = BLL.see_all_students()  # Call the function to get the data
tab1_layout = [
    [sg.Table(values=student_data, headings=headings,
              max_col_width=35, auto_size_columns=True,
              display_row_numbers=True, justification='left',
              num_rows=10, key='STUDENTTABLE', row_height=60,
              enable_events=True, tooltip='all students in database'),
              sg.Button('Exit')]
]

tab2_layout = [
    [sg.Text('Add Student to database')],
    [sg.Text('First Name: '), sg.InputText(key=FIRST_NAME)],
    [sg.Text('Last Name: '), sg.InputText(key=LAST_NAME)],
    [sg.Text('Email Address: '), sg.InputText(key=EMAIL)],
    [sg.Text('Date of Birth: '), sg.InputText(key=DOB)],
    [sg.Text('Student Grade: '), sg.InputText(key=STUDENT_GRADE)],
    [sg.Text('Class Grade: '), sg.InputText(key=CLASS_GRADE)],
    [sg.Text('Class ID: '), sg.InputText(key=CLASS_ID)],
    [sg.Text('Teacher ID: '), sg.InputText(key=TEACHER_ID)],
    [sg.Button('Add Student'), sg.Button('Exit')]
]

# tab group for layouts
tab_group = sg.TabGroup([[sg.Tab('All Students', tab1_layout), 
                         sg.Tab('Add Student', tab2_layout)]],
                         selected_title_color='Green', selected_background_color='Yellow')
layout = [[tab_group]]
window = sg.Window('Student Management System', layout)

# empty list to hold the student info
student_info = []

while True:
    try:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            if sg.popup_yes_no('Are you sure you want to Exit?') == 'Yes':
                break
        if event == 'Add Student':
            student_info = [
                values[FIRST_NAME], values[LAST_NAME], values[EMAIL],
                values[DOB], values[STUDENT_GRADE], values[CLASS_GRADE],
                values[CLASS_ID], values[TEACHER_ID]
            ]
            # add the student to the database
            BLL.addStudentfunc(student_info)
            # clear the input fields
            for key in (FIRST_NAME, LAST_NAME, EMAIL, DOB, STUDENT_GRADE, CLASS_GRADE, CLASS_ID, TEACHER_ID):
                window[key].update('')
            sg.popup('Student added successfully!')
            # Refresh the student data table
            student_data = BLL.see_all_students()
            window['STUDENTTABLE'].update(values=student_data)
            student_info = []
    except Exception as e:
        sg.popup_error(f"An error occurred: {str(e)}")
        break

window.close()