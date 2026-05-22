# Lesson 4 - Math Operators
a = 10
b = 3

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b:.2f}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponent: {a ** b}")

# Real life example
marks = 450
total = 500
percentage = (marks / total) * 100
print(f"My percentage is {percentage:.1f}%")

# Chocolate problem
chocolates = 100
friends = 7
each = chocolates // friends
leftover = chocolates % friends
print(f"Each friend gets {each} chocolates")
print(f"Leftover chocolates: {leftover}")
