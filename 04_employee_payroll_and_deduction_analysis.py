"""Case Study 4: Employee Payroll and Deduction Analysis
Compute an employee's net salary after simple percentage deductions.
"""

name = input("Employee name: ")
salary = float(input("Basic salary (₹): "))
deduction_percent = float(input("Deduction percentage (0–100): "))

if salary < 0 or not 0 <= deduction_percent <= 100:
    print("Invalid salary or deduction percentage.")
else:
    deduction = salary * deduction_percent / 100
    net_salary = salary - deduction
    print(f"Employee: {name}")
    print(f"Gross salary: ₹{salary:.2f}")
    print(f"Deduction: ₹{deduction:.2f}")
    print(f"Net salary: ₹{net_salary:.2f}")
