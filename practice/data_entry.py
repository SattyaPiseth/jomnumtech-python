"""
@Project: jomnum-tech-python
@Path: practice
@File: data_entry.py
@Author: Sattya Piseth
@Created: 10/29/2025 8:29 PM
@Description: Collect user_id, username, age, and position via input(), converting each value to the correct data type.
"""

# collect values from users via input()
user_id = int(input("Enter your user_id: "))
username = input("Enter your username: ")
age = int(input("Enter your age: "))
position = input("Enter your position: ")

# list out data types of collected values
print(f"user_id: {type(user_id).__name__}")
print(f"username: {type(username).__name__}")
print(f"age: {type(age).__name__}")
print(f"position: {type(position).__name__}")

