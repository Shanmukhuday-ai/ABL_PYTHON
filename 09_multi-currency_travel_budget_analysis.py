"""Case Study 9: Multi-Currency Travel Budget Analysis
Convert travel expenses from a foreign currency to INR and compare them with a budget.
"""

budget_inr = float(input("Travel budget in INR (₹): "))
foreign_expenses = float(input("Expenses in foreign currency: "))
exchange_rate = float(input("INR per 1 foreign-currency unit: "))

if budget_inr < 0 or foreign_expenses < 0 or exchange_rate <= 0:
    print("Invalid input.")
else:
    expenses_inr = foreign_expenses * exchange_rate
    remaining = budget_inr - expenses_inr
    print(f"Expenses in INR: ₹{expenses_inr:.2f}")
    if remaining >= 0:
        print(f"Within budget. Balance: ₹{remaining:.2f}")
    else:
        print(f"Over budget by: ₹{-remaining:.2f}")
