# Lesson 9 - Lists

# Basic list operations
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))

# Loop through list
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Add and remove
fruits.append("grapes")
print(fruits)
fruits.remove("banana")
print(fruits)

# List with maths
marks = [85, 90, 78, 95, 88]
print(f"Highest mark: {max(marks)}")
print(f"Lowest mark: {min(marks)}")
print(f"Total marks: {sum(marks)}")
print(f"Average mark: {sum(marks)/len(marks):.1f}")

# Add new mark
marks.append(92)
print(f"Updated marks: {marks}")
print(f"New average: {sum(marks)/len(marks):.1f}")

# Student report system
students = ["Mariya", "Arya", "Sara", "Priya"]
marks = [95, 78, 88, 92]

print("--- Class Report ---")
print(f"Total Students: {len(students)}")
print(f"Class Average: {sum(marks)/len(marks):.1f}")
print(f"Highest Mark: {max(marks)}")
print(f"Lowest Mark: {min(marks)}")
print("\n--- Individual Report ---")

for i in range(len(students)):
    if marks[i] >= 90:
        grade = "A+"
    elif marks[i] >= 80:
        grade = "A"
    elif marks[i] >= 70:
        grade = "B"
    else:
        grade = "C"
    print(f"{students[i]} : {marks[i]} marks : Grade {grade}")
