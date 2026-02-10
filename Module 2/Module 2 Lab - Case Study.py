'''
Module 2 Lab - Case Study
Levi Melangton

Academic Honors Calculator

This app will take a student's last name, first name, and their GPA as a float.
It will then determine if the student has made the Dean's List or the Honor Roll,
and will print a statement saying which they made, if either.

last_name = the student's last name.
first_name = the student's first name.
GPA = the student's GPA.
'''

last_name = input('What is your last name?("ZZZ" to quit): ') # Last name - used to enter and exit the loop

while last_name != "ZZZ": # Loop to continue asking for student names and GPAs
    first_name = input('What is your first name?: ') # Get student first name
    GPA = input('What is your GPA?: ') # Get student GPA
    GPA = float(GPA) # Convert input string to a float
    
    if GPA >= 3.5: # Check if GPA makes Dean's List
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif GPA >= 3.25: # Check if GPA makes Honor Roll
        print(f"{first_name} {last_name} has made the Honor Roll!")
    else: # Encouraging print statement for those that didn't make any academic honors
        print(f"{first_name} {last_name} did not make any academic honors. Keep trying!")
    last_name = input('What is your last name?("ZZZ" to quit): ') # Get last name for next student or exit the loop


# https://github.com/LeviZm/SDEV220.git