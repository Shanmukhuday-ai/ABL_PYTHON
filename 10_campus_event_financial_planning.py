"""Case Study 10: Campus Event Financial Planning
Estimate event costs, total funds available, and surplus or shortfall.
"""

attendees = int(input("Expected attendees: "))
cost_per_attendee = float(input("Cost per attendee (₹): "))
fixed_cost = float(input("Fixed event cost (₹): "))
sponsorship = float(input("Sponsorship/funds available (₹): "))

if attendees < 0 or cost_per_attendee < 0 or fixed_cost < 0 or sponsorship < 0:
    print("Invalid input. Values cannot be negative.")
else:
    variable_cost = attendees * cost_per_attendee
    total_cost = variable_cost + fixed_cost
    balance = sponsorship - total_cost
    print(f"Variable cost: ₹{variable_cost:.2f}")
    print(f"Total event cost: ₹{total_cost:.2f}")
    if balance >= 0:
        print(f"Surplus funds: ₹{balance:.2f}")
    else:
        print(f"Additional funds required: ₹{-balance:.2f}")
