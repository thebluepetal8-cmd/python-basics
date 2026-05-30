# Lesson 10 - Dictionaries

# Basic dictionary
student = {
    "name": "Mariya",
    "age": 22,
    "course": "BCA AI and ML",
    "university": "Shoolini University",
    "year": 2026
}

# Access values
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Course: {student['course']}")

# Loop through dictionary
print("\n--- Student Details ---")
for key, value in student.items():
    print(f"{key} : {value}")

# Add new key
student["city"] = "Solan"
print(f"\nUpdated Dictionary: {student}")

# List of dictionaries
students = [
    {"name": "Mariya", "marks": 95, "grade": "A+"},
    {"name": "Arya",   "marks": 78, "grade": "B"},
    {"name": "Sara",   "marks": 88, "grade": "A"},
    {"name": "Priya",  "marks": 92, "grade": "A+"}
]

print("\n--- Class Report ---")
for student in students:
    print(f"{student['name']} → {student['marks']} marks → Grade {student['grade']}")
