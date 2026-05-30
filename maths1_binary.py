# Maths Class 1 - Number Systems & Binary

# Decimal to Binary
numbers = [5, 8, 15, 20]
for num in numbers:
    print(f"{num} in binary = {bin(num)[2:]}")

# Complete binary table 0-10
print("\n--- Binary Table ---")
for i in range(11):
    print(f"{i} in binary = {bin(i)[2:]}")

# Binary to Decimal
print("\n--- Binary to Decimal ---")
print(int('1101', 2))   # 13
print(int('1010', 2))   # 10

# House price predictor - Linear equation y = mx + c
print("\n--- House Price Predictor ---")
def predict_price(rooms):
    price = 50 * rooms + 10000
    return price

for rooms in range(1, 6):
    print(f"{rooms} rooms → Price = {predict_price(rooms)}")
