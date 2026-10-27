"""Case Study 3: Hospital Billing and Patient Classification
Calculate a simple hospital bill and classify the patient by total charges.
"""

consultation_fee = float(input("Consultation fee (₹): "))
bed_days = int(input("Number of bed-days: "))
daily_charge = float(input("Daily bed charge (₹): "))

if consultation_fee < 0 or bed_days < 0 or daily_charge < 0:
    print("Invalid input. Values cannot be negative.")
else:
    total = consultation_fee + bed_days * daily_charge
    if total < 5000:
        category = "Basic"
    elif total <= 15000:
        category = "Standard"
    else:
        category = "Premium"

    print(f"Total hospital bill: ₹{total:.2f}")
    print(f"Patient billing category: {category}")
