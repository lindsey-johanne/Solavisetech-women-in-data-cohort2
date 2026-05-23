# SECTION 2: OPERATORS

# 1. Simple Calculator
a = 20
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 2. Area of Shapes
pi = 3.14159
radius = 5
print(f"Circle area: {pi * radius ** 2}")
length, width = 8, 4
print(f"Rectangle area: {length * width}")
base, height = 6, 3
print(f"Triangle area: {0.5 * base * height}")

# 3. Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# 4. Student Grade Percentage
scored = 75
total = 100
print(f"Percentage: {(scored/total) * 100}%")

# 5. BMI Calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

# 6. Power & Modulus
print(f"2 to the power of 8: {2 ** 8}")
print(f"17 modulus 5: {17 % 5}")
