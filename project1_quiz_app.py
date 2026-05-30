# 🎯 Python Quiz App — by Mariya NA

questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 12"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for floor division in Python?",
        "options": ["A) /", "B) %", "C) //", "D) **"],
        "answer": "C"
    },
    {
        "question": "What does len('Mariya') return?",
        "options": ["A) 5", "B) 7", "C) 6", "D) 4"],
        "answer": "C"
    },
    {
        "question": "Which loop is used when we don't know how many times to repeat?",
        "options": ["A) for loop", "B) while loop", "C) if loop", "D) range loop"],
        "answer": "B"
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "options": ["A) list = (1,2,3)", "B) list = {1,2,3}", "C) list = [1,2,3]", "D) list = <1,2,3>"],
        "answer": "C"
    }
]

# Quiz start
print("🐍 Welcome to Python Quiz!")
print(f"Total Questions: {len(questions)}")
print("=" * 35)

name = input("Enter your name: ").strip()
score = 0

for i, q in enumerate(questions):
    print(f"\nQ{i+1}: {q['question']}")
    for option in q['options']:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q['answer']:
        print("✅ Correct!")
        score = score + 1
    else:
        print(f"❌ Wrong! Correct answer was {q['answer']}")

# Final result
percentage = (score / len(questions)) * 100

print("\n" + "=" * 35)
print(f"🎯 Quiz Complete, {name}!")
print(f"Score     : {score}/{len(questions)}")
print(f"Percentage: {percentage:.1f}%")

if percentage >= 80:
    print("Grade     : A+ — Outstanding! 🌟")
elif percentage >= 60:
    print("Grade     : B — Good job! 😊")
else:
    print("Grade     : C — Keep practicing! 💪")
