"""
@Project: jomnum-tech-python
@Path: homework
@File: variable_and_datatypes_251025.py
@Author: Piseth Sattya
@Created: 10/25/2025 7:25 PM
@Description: Practice using Python variables, follow naming conventions, and understand basic data types.
"""

# declare variables
name = "Piseth Sattya" # store value as string
age = 23 # store value as integer
height_in_meters = 1.75 # store value as float
is_student = True # store value as boolean

# print data types of variables
print("-"*35)
print("Homework: Variables & Data Types")
print("-"*35)
print("DATATYPES OF VARIABLES")
print("-"*35)
print("- name:", type(name).__name__)
print("- age:", type(age).__name__)
print("- height_in_meters:", type(height_in_meters).__name__)
print("- is_student:", type(is_student).__name__)

# print personal information
print("-"*35)
print("PERSONAL INFORMATION")
print("-"*35)
print(f'- name: {name}')
print(f'- age: {age}')
print(f'- height_in_meters: {height_in_meters}m')
print(f'- is_student: {is_student}')
print("-"*35)