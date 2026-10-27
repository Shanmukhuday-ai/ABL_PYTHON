"""Case Study 7: Retail Billing with Multiple Discount Rules
Calculate a retail bill with a discount based on purchase amount.
"""

amount = float(input("Enter purchase amount (₹): "))

if amount < 0:
    print("Invalid amount.")
else:
    if amount >= 5000:
        rate = 10
    elif amount >= 2000:
        rate = 5
    else:
        rate = 0

    discount = amount * rate / 100
    payable = amount - discount
    print(f"Discount rate: {rate}%")
    print(f"Discount amount: ₹{discount:.2f}")
    print(f"Final amount: ₹{payable:.2f}")
