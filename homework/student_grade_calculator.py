"""
@Project: jomnum-tech-python
@Path: homework
@File: student_grade_calculator.py
@Author: Sattya Piseth
@Created: 11/9/2025 3:54 PM
@Description: Student Grade Calculator - Calculates average score and displays grade
"""

# Get student name
student_name = input("Enter student name: ")

# Get five subject scores
java_score = float(input("Enter score for Java: "))
python_score = float(input("Enter score for Python: "))
linux_score = float(input("Enter score for Linux: "))
springboot_score = float(input("Enter score for Spring Boot: "))
nextjs_score = float(input("Enter score for Next.js: "))

# Calculate average score
average_score = (java_score + python_score + linux_score + springboot_score + nextjs_score) / 5

# Display student name and average
print(f"\nStudent Name: {student_name}")
print(f"Average Score: {average_score:.2f}")

# Determine and display grade using if-elif-else
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
