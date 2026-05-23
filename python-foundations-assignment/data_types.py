# SECTION 1: DATA TYPES

# 1. Personal Bio Generator
name = "Lindsey-Johanne"
age = 25
height = 1.65
favorite_tech_field = "Health Informatics"
student_status = True
print(f"Hi, I'm {name}, {age} years old, {height}m tall. My favorite tech field is {favorite_tech_field}. Currently a student: {student_status}")

# 2. Type Checker
print(type(name))
print(type(age))
print(type(height))
print(type(student_status))

# 3. Data Conversion
print(str(age))
print(int(3.9))
print(int("25"))

# 4. User Information
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_country = input("Enter your country: ")
print(f"Welcome {user_name}, age {user_age}, from {user_country}!")

# 5. Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
