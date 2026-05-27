# Lesson 8 - While Loops

# Countdown using while
count = 10
while count >= 1:
    print(f"Countdown: {count}")
    count = count - 1
print("Blast off! 🚀")

# Guessing game with counter
secret = "python"
attempts = 0

guess = input("Guess the secret word: ").strip()

while guess != secret:
    attempts = attempts + 1
    print(f"Wrong! Try again! Attempts: {attempts}")
    guess = input("Guess the secret word: ").strip()

attempts = attempts + 1
print(f"🎉 Correct! You guessed it in {attempts} attempts!")
