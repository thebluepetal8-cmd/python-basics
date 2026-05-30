# 💰 Expense Tracker App — by Mariya NA

expenses = []

def show_menu():
    print("\n💰 Expense Tracker")
    print("=" * 30)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View summary")
    print("4. Exit")
    print("=" * 30)

def add_expense():
    name = input("Expense name: ").strip()
    amount = float(input("Amount (₹): "))
    expenses.append({"name": name, "amount": amount})
    print(f"✅ Added: {name} — ₹{amount:.2f}")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet!")
        return
    print("\n--- Your Expenses ---")
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['name']} — ₹{exp['amount']:.2f}")

def view_summary():
    if len(expenses) == 0:
        print("No expenses added yet!")
        return
    amounts = [exp['amount'] for exp in expenses]
    print("\n--- Summary ---")
    print(f"Total expenses  : {len(expenses)}")
    print(f"Total spent     : ₹{sum(amounts):.2f}")
    print(f"Highest expense : ₹{max(amounts):.2f}")
    print(f"Lowest expense  : ₹{min(amounts):.2f}")
    print(f"Average expense : ₹{sum(amounts)/len(amounts):.2f}")

# Main loop
print("👋 Welcome to Expense Tracker!")
name = input("Enter your name: ").strip()
print(f"Hello {name}! Let's track your expenses! 💰")

while True:
    show_menu()
    choice = input("Choose option (1-4): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        print(f"\nGoodbye {name}! Keep saving! 💰✨")
        break
    else:
        print("❌ Invalid choice! Please choose 1-4!")
