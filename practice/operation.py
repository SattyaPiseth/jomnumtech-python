"""
@Project: jomnum-tech-python
@Path: practice
@File: operation.py
@Author: Sattya Piseth
@Created: 10/29/2025 8:46 PM
@Description: Arithemetic Operations
"""
# declaring variables
num1 = 12
num2 = 2.5

print(f'The sum is: {num1 + num2}')
print(f'The subtraction is: {num1 - num2}')
print(f'The multiplication is: {num1 * num2}')
print(f'The division is: {num1 / num2}')
print(f'The type of division: {type(num1 / num2).__name__}')
print(f'Division result (2 decimal places) {num1 / num2:.2f}')
print(f'The floor division is: {num1 // num2}')
print(f'The modulus is: {num1 % num2}')
print(f'The exponent is: {num1 ** num2} = {num1} ^ {num2}')


print("\n")

# Assignment Operators

# first initialization of num1
print(f'The value of num1 is: {num1}')

# second assign value to num1
num1 += num2 # num1 = num1 + num2
print(f'After adding num2 to num1, the value of num1 is: {num1}')

# third assign value to num1
num1 -= num2 # num1 = num1 - num2
print(f'After subtracting num2 from num1, the value of num1 is: {num1}')

print("\n")

# Comparison Operators
value1 = 10
value2 = 20

print(f'value1 == value2: {value1 == value2}')
print(f'value1 != value2: {value1 != value2}')

print(f'value1 > value2: {value1 > value2}')
print(f'value1 < value2: {value1 < value2}')

print(f'value1 >= value2: {value1 >= value2}')
print(f'value1 <= value2: {value1 <= value2}')

print("\n")
# MEMBERSHIP OPERATORS
colors = ['red', 'green', 'blue']
print(f'yellow in colors: {"yellow" in colors}')
print(f'yellow not in colors: {"yellow" not in colors}')
print(f'blue in colors: {"blue" in colors}')
print(f'blue not in colors: {"blue" not in colors}')
print(f'black in colors: {"black" in colors}')

print("\n")

# Identity Operators

# Example 1 — lists (mutable objects)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True  (same object)
print(a == b)   # True  (same value)
print(a is c)   # False (different objects)
print(a == c)   # True  (values equal)

"""
The line `print(id(a), id(b), id(c))` prints the identity integers for the three list objects. `id(obj)` 
returns a unique integer for that object (often related to its memory address). 
Because `b = a`, `id(a)` and `id(b)` will be the same; 
`c` has the same contents but is a different object, so `id(c)` will different.
```
"""
print(id(a), id(b), id(c))


