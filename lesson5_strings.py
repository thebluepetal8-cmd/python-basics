# Lesson 5 - String Concatenation
first_name = "Sun"
last_name = "AA"
university = "ABC School"
course = "BCA AI and ML"
year = 2026

# Method 1 - using +
print("Full Name  : " + first_name + " " + last_name)

# Method 2 - using f-string
print(f"University : {university}")
print(f"Course     : {course}")
print(f"Batch      : {year}")

# Method 3 - using join
words = ["Python", "is", "fun!"]
print(" ".join(words))

# Student ID card
student_id = (first_name + "-" + last_name + "-BCA-" + str(year)).upper()
print(f"Student ID : {student_id}")

# String tricks
name = "sun AA"
print(name.upper())
print(name.capitalize())
print(f"Your name has {len(name)} characters")
print("Python " * 3)
