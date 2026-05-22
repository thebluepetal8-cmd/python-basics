name = input("Enter student name: ").strip()
marks = float(input("Enter marks out of 100: "))

percentage = (marks / 100) * 100
student_id = ("STU-" + name + "-2026").upper()

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"\n--- Report Card ---")
print(f"Name       : {name}")
print(f"Student ID : {student_id}")
print(f"Marks      : {marks}/100")
print(f"Percentage : {percentage:.1f}%")
print(f"Grade      : {grade}")
