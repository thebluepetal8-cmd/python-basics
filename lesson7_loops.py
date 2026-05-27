# Lesson 7 - For Loops

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Print name 5 times
for i in range(5):
    print("Mariya")

# Countdown
for i in range(10, 0, -1):
    print(i)
print("Blast off! 🚀")

# Name with number
for i in range(1, 6):
    print(f"{i}. Mariya NA — BCA AI and ML")

# Multiplication table of 3
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# Sum of 1 to 10
total = 0
for i in range(1, 11):
    total = total + i
print(f"Sum of 1 to 10 = {total}")
