"""Case Study 2: Progressive Electricity Billing
Calculate an electricity bill using progressive unit slabs.
"""

units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units. Enter a non-negative value.")
elif units <= 100:
    bill = units * 1.50
    print(f"Electricity bill: ₹{bill:.2f}")
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print(f"Electricity bill: ₹{bill:.2f}")
else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    print(f"Electricity bill: ₹{bill:.2f}")
