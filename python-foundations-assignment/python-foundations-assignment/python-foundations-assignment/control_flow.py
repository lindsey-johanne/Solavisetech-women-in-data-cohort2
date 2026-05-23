# SECTION 3: CONTROL FLOW

# 1. Age Eligibility Checker
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# 2. Password Validator
password = input("Enter password: ")
if len(password) < 6:
    print("Weak password")
elif len(password) < 10:
    print("Moderate password")
else:
    print("Strong password")

# 3. Grade Classification
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 4. Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 5. Number Guessing Game
secret = 7
guess = int(input("Guess the number (1-10): "))
while guess != secret:
    print("Wrong, try again!")
    guess = int(input("Guess again: "))
print("Correct!")

# 6. Countdown Timer
for i in range(10, 0, -1):
    print(i)
print("Done!")

# 7. ATM Withdrawal
balance = 500
amount = float(input("Enter withdrawal amount: "))
if amount > balance:
    print("Insufficient funds")
elif amount <= 0:
    print("Invalid amount")
else:
    balance -= amount
    print(f"Successful! Remaining balance: {balance}")

# 8. Login System
correct_username = "lindsey"
correct_password = "health123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid credentials")
