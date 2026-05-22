# Lesson 6 - Conditions
# Grade checker
marks = float(input("Enter your marks out of 100: "))

if marks >= 90:
    print("Grade: A+ — Outstanding!")
elif marks >= 80:
    print("Grade: A — Excellent!")
elif marks >= 70:
    print("Grade: B — Good!")
elif marks >= 60:
    print("Grade: C — Average")
else:
    print("Grade: F — Need to work harder!")

# Login system
correct_username = "Sun"
correct_password = "ABC2026"

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if username == correct_username and password == correct_password:
    print(f"Welcome, {username}! Login successful!")
else:
    print("Wrong password! Access denied!")
