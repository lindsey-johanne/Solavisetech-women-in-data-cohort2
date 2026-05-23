# SECTION 4: DATA STRUCTURES

# 1. Favorite Tools List
tools = ["DHIS2", "KoboToolbox", "Tableau"]
tools.append("Python")
tools.remove("Tableau")
print(tools)

# 2. Student Scores
scores = [78, 92, 65, 88, 74]
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Average: {sum(scores)/len(scores)}")

# 3. Shopping List Manager
shopping = ["rice", "eggs", "milk"]
shopping.append("bread")
shopping.remove("eggs")
print(shopping)

# 4. Country Capitals
capitals = [("Cameroon", "Yaoundé"), ("Nigeria", "Abuja"), ("Ghana", "Accra")]
for country, capital in capitals:
    print(f"The capital of {country} is {capital}")

# 5. Unique Visitors
visitors = {"Alice", "Bob", "Alice", "Carol", "Bob"}
print(f"Unique visitors: {visitors}")

# 6. Common Skills
set1 = {"Python", "R", "SQL", "Tableau"}
set2 = {"R", "SQL", "Excel", "Power BI"}
print(f"Common skills: {set1 & set2}")

# 7. Student Record
student = {
    "name": "Lindsey-Johanne",
    "age": 25,
    "program": "Health Informatics",
    "grade": "A"
}
for key, value in student.items():
    print(f"{key}: {value}")

# 8. Mini Contact Book
contacts = {
    "Alice": "123-456-789",
    "Bob": "987-654-321",
    "Carol": "456-789-123"
}
search = input("Enter contact name: ")
if search in contacts:
    print(f"{search}'s number: {contacts[search]}")
else:
    print("Contact not found")
